这是一个使用Python编写的Telegram机器人，主要功能是提供短信轰炸功能。用户通过发送`/bomb`命令并输入目标手机号，机器人将向多个短信接口发送请求，模拟轰炸效果。

## 代码结构

- **导入模块**：
  - `requests`：用于发送HTTP请求。
  - `threading`：用于创建多线程，提高请求效率。
  - `TeleBot`和`types`：用于创建和管理Telegram机器人。
- **配置**：
  - `TOKEN`：你的Telegram机器人的API token，需要替换为实际的token。
- **版权信息**：
  - 每五行代码后添加了版权信息，声明代码由散小战开发，版权所有。
- **处理`/bomb`命令**：
  - `handle_bomb`函数：处理`/bomb`命令，提示用户输入手机号，并注册下一步的处理函数`start_bombing`。
- **开始轰炸**：
  - `start_bombing`函数：验证手机号，发送请求到多个短信接口，模拟轰炸效果。
- **发送请求**：
  - `send_sms`函数：发送GET请求到指定的URL，检查请求是否成功并打印结果。
- **启动机器人**：
  - `bot.polling()`：启动机器人，开始监听和处理消息。

## 使用方法

### 1. 安装 Python 3.9

在 Ubuntu 系统上编译安装 Python 3.9 的步骤如下：

1. **更新系统包**：
   ```sh
   sudo apt update
   sudo apt upgrade -y
   ```



• 安装依赖包：

```sh
   sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
   libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
   xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
   ```



• 下载 Python 3.9 源码：

```sh
   wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tgz
   ```



• 解压源码：

```sh
   tar -xf Python-3.9.0.tgz
   cd Python-3.9.0
   ```



• 编译并安装：

```sh
   ./configure --enable-optimizations
   make -j `nproc`
   sudo make altinstall
   ```



• 验证安装：

```sh
   python3.9 --version
   ```



2.安装依赖库


• 创建`requirements.txt`文件：

```sh
   echo "requests" > requirements.txt
   echo "pyTelegramBotAPI" >> requirements.txt
   ```



• 安装依赖：

```sh
   pip3.9 install -r requirements.txt
   ```



3.运行机器人


• 保存代码：

• 将代码保存为`hztgbot.py`。


• 运行机器人：

```sh
   python3.9 hztgbot.py
   ```



注意事项


• 法律法规：请确保使用场景符合当地法律法规，不要用于非法或不当目的。

• 道德准则：尊重他人隐私，不要发送垃圾短信或进行骚扰。

• 服务接口：确保使用的短信发送接口是合法且授权的。


TG飞机✈️频道


• TG飞机✈️频道：[@SAN869CN](https://t.me/SAN869CN)

```

### 详细步骤说明

#### 1. 更新系统包

在安装 Python 3.9 之前，首先需要更新系统的包列表并升级已安装的包。这可以通过以下命令完成：

```sh
sudo apt update
sudo apt upgrade -y
```



2.安装依赖包

编译 Python 3.9 需要一些依赖包，这些包可以通过以下命令安装：


```sh
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
```



3.下载 Python 3.9.20 源码

从 Python 官方网站下载 Python 3.9.20 的源码：


```sh
wget https://www.python.org/ftp/python/3.9.20/Python-3.9.20.tgz
```



4.解压源码

解压下载的源码包，并进入解压后的目录：


```sh
tar -xf Python-3.9.20.tgz
cd Python-3.9.20
```



5.编译并安装

配置并编译 Python 3.9.20，然后安装到系统中：


```sh
./configure --enable-optimizations
make -j `nproc`
sudo make altinstall
```



6.验证安装

验证 Python 3.9.20 是否安装成功：


```sh
python3.9 --version
```


如果安装成功，你应该看到输出`Python 3.9.20`。


安装依赖库


1.创建`requirements.txt`文件

创建一个`requirements.txt`文件，列出所有需要的依赖库：


```sh
echo "requests" > requirements.txt
echo "pyTelegramBotAPI" >> requirements.txt
```



2.安装依赖

使用`pip3.9`安装`requirements.txt`文件中列出的依赖库：


```sh
pip3.9 install -r requirements.txt
```

2.运行机器人

##使用 Python 3.9 运行机器人：
```sh
python3.9 hztgbot.py
```
