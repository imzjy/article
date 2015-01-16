查看Windows中服务的状态[Daily works with Ruby]
=========

### 起因：

我时常需要查看一些Windows Service的状态，每次使用控制面板->服务这种方式来查看服务状态不仅浪费时间而且也很无聊，干脆写个Ruby脚本吧。让Ruby脚本来通知我某个Windows Service的状态是如何，并根据状态给我一些提示。

### 主要内容： 

你可以从本篇daily works with ruby中看到以下技术/工具的使用。

- 使用RubyGems来查询，安装Gem包。
- Ruby中查询Windows服务状态。
- Ruby中调用Windows API。
 

### 一，安装 RubyGems 

你可以去[RubyForge](http://rubyforge.org/frs/download.php/45906/rubygems-1.3.1.zip)下载最新的RubyGems。RubyGems是Ruby中使用的一种包管理中工具。当你安装完RubyGems后，便可以使用gem命令来查询安装别的Ruby库。下载完RubyGems安装包的zip文件解压至：`D:\Temp`目录下，执行如下命令，安装RubyGems：

```text
C:\Documents and Settings\Jerry>d:
D:\>cd Temp\rubygems-1.3.1
D:\Temp\rubygems-1.3.1>setup.rb
mkdir -p C:/Ruby/lib/ruby/site_ruby/1.8
mkdir -p C:/Ruby/bin
```

安装完成后便可以使用RubyGems来查询和安装Ruby的gem包了。

### 二，安装win32-service包

#### 1，查询 

安装RubyGems包管理器后，我们可以用gem命令来查询和安装ruby的gem包。我们访问Windows服务时，需要用到wind32-service包，现在我们在命令行了键入以下命令进行查询：


```text
D:\Temp\rubygems-1.3.1>gem query -r -n service 

*** REMOTE GEMS *** 

actionservice (0.3.0) 
actionwebservice (1.2.6) 
ar_mailer_service (0.1.1) 
contxtlservice (0.1.1) 
dot_net_services (0.4.0, 0.3.0) 
mongrel_service (0.3.4, 0.1) 
ruby_service_helper (0.1.0) 
servicemerchant (0.1.0) 
win32-service (0.7.0) 
win32_service_manager (0.1.3) 
 
D:\Temp\rubygems-1.3.1>
```

`gem query`命令是查询可用gem包的命令，你可以通过`gem --help`来得到更多的可用选项。 

其中`gem query -r -n service`表示去远端服务器[-r选项]上寻找名称[-n选项]为service的gem包。 

在上面的13行中显示了我们需要用到的包，即：`win32-service`。

#### 2，安装win32-service

执行如下命令安装win32-service包：

```text
D:\Temp\rubygems-1.3.1>gem install -r win32-service 
Successfully installed win32-service-0.7.0-x86-mswin32-60 
1 gem installed 
Installing ri documentation for win32-service-0.7.0-x86-mswin32-60 
Installing RDoc documentation for win32-service-0.7.0-x86-mswin32-60 

D:\Temp\rubygems-1.3.1>
```

在安装完win32-service之后，我们便可以查看win32-service的相关文档及API说明了。 

先从命令行执行：

```text
D:\Soft\AutoHotkey104805>gem server 
Starting gem server on http://localhost:8808/
```

之后我们就可以打开浏览器访问http://localhost:8808/，便可以访问所有的Gem包的Documents。

### 三，编写查询Windows Service状态脚本

万事俱备，只欠东风了。我们开始编写脚本。

```ruby
#!/usr/bin/evn ruby
require "win32/service"
require "Win32API"
include Win32
 
if  Service.exists?("WebClient") && Service.status("WebClient").current_state  == "running"
    beep = Win32API.new('kernel32','Beep',['I']*2,'V')
    5.times do
        beep.call(750,300)
        sleep(1)
    end
end
```

这里需要解释一下的是第7行：

`beep = Win32API.new('kernel32','Beep',['I']*2,'V')`

这里我们申明了一个Windows API,其中`Win32API.new`方法有四个参数。

1. API所在动态链接库的名称，如user32,kernel32.... 
1. API的方法名称
1. 传入参数类型:两个Integer类型的参数，常用的还有: `['P']-Pointer, ['V']-void, ['n']-number` 
1. 返回值类型

### 四，结语 

利用RubyGems来查询Ruby的库很方便。 同样地利用Ruby的一些模块，来调用Windows API完成特定任务也很简单。 

当遇到一些API不了解时，可以利用`gem server`命令打开本地www服务查看相应Gem文档。

