##### [ 一，概述](##一，概述)

##### [ 二、运行](##二、运行)

##### [ 三，配置](##三，配置)

##### [ 四，统计解析](##四，统计解析)

##### [ 五，其他](##五，其他)

## 一，概述

**QSC** 是一个基于<code>selenium</code>的<code>python</code>爬虫，用于根据时间范围统计特定 QQ 空间中说说的简单信息，其中包括：**「总评论数」**,**「评论最多的前三名用户」**,**「每日的说说数量」**,**「每条说说的文本内容及相同内容的计数」**。

**设计初衷** 是为了配合树洞，表白墙等常见学生组织统计数据之用。

**GitHub 地址** ：[https://github.com/SimpleIcomputer/QQSpace_Crawler](https://github.com/SimpleIcomputer/QQSpace_Crawler)

## 二、运行

可以通过 **[源代码(py) ](###1.源代码)** 或 **[可执行文件(exe)](###2.可执行文件)** 两种方式运行爬虫：

### 1.源代码

获取 release 中的**source_code.zip**，解压后如图：

<div align=center><img src="图 2-1-0.png" alt="图 2-1-0" style="zoom:67%;" /></div>

**1)** 使用任意编译器运行<code>main.exe</code>

**2)** 在弹出的浏览器下登录 QQ（需要有被爬取用户的空间访问权限）

<div align=center><img src="图 2-1-1.png" alt="图 2-1-1" style="zoom: 50%;" /></div>

**3）** 确认登陆成功后回到**命令行**，根据提示键入 **y** 后可以看到如图浏览器正在自动爬取信息

<div align=center><img src="图2-1-2.png" alt="图2-1-2" style="zoom:67%;" /></div>

**4)** 经过一段时间后，数据整理完成并写入**同目录**下的**result.csv**文件

<div align=center><img src="图2-1-3.png" alt="图2-1-3" style="zoom: 67%;" /></div>

### 2.可执行文件

获取 release 中的**QSC.zip**，解压后如图：

<div align=center><img src="图 2-2-0.png" alt="图 2-1" style="zoom:67%;" /></div>

**1)** 找到并运行<code>main.exe</code>

**2)** 余下遵从 **[源代码 ](###1.源代码)** 中 **2)** 之后的步骤

## 三，配置

**配置文件**为目录下的<code>config.ini</code> ,分为三个块：**[settings](###1.settings) , [user_config](###2.user_config) , [decode_gtk](###3.decode_gtk)**

### 1.settings

```ini
driver_path = chromedriver.exe
# webdriver路径,默认配置下需要谷歌浏览器
start_url = https://user.qzone.qq.com/
# QQ空间主页
base_url = https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin={}&inCharset=utf-8&outCharset=utf-8&hostUin={}&notice=0&sort=0&pos={}&num={}&cgi_host=https%3A%2F%2Fuser.qzone.qq.com%2Fproxy%2Fdomain%2Ftaotao.qq.com%2Fcgi-bin%2Femotion_cgi_msglist_v6&code_version=1&format=jsonp&need_private_comment=1&g_tk={}
```

### 2.user_config

```ini
qq_number =
# 需要爬取的QQ号
time_start =
# 时间起点，格式示例：2000-10-1
# 自此时间的零点开始，向后朝时间终点运行
time_end =
# 时间终点
including_forward = False
# 爬取的说说信息是否包括转发
```

### 3.decode_gtk

```ini
js_code =function getGTK(str){var hash = 5381;for(var i = 0, len = str.length; i < len; ++i){hash += (hash << 5) + str.charAt(i).charCodeAt();}return hash&2147483647 ;}
# 通过cookie获得特征码的js解码代码
```

## 四，统计解析

**result.csv** 文件中的统计信息如图所示：

<div align=center> <img src="图4-0-0.png" alt="图4-0-0" style="zoom: 22%;" /></div>

**(1) 评论最多的前三位用户**

**(2) 评论最多的前三位用户的评论数量**

**(3) 总评论数**

**(4) 说说文本信息**

**(5) 相同说说文本信息计数**

**(6) 日期**

**(7) 对应日期说说计数**

## 五，其他

**1.源代码依赖项**

> configparser
>
> selenium
>
> pandas
>
> execjs
>
> json

**2.是否会继续更新**

是的！:-) 也请您能在评论留下您的建议！
