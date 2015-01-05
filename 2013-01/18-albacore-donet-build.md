Albacore--.NET下基于Rake(ruby make)的自动化构建工具
===========

微软系的工具以集成化著称，自动化构建一般也是基于Visual Studio或者它的插件。除此之外可能就是NAnt——Java中Ant的.NET版，很多开源的项目就是用NAnt来实现自动化构建的。
我个人最不喜欢Ant的是他是基于XML的，我现在对XML有着本能的反感，他不符合DRY。XML中重复又没有意义的标签太多了，前几年对XML的替代可能是YAML，但是近几年随着Web开发的普及，JSON成了替代XML的不二选择，很多语言的标准库都有JSON的parser，这进一步推动了JSON这种数据交换格式的普及。

Albacore是基于Ruby Rake的自动化构建工具，它语法和Rake保存一致，直接使用Visual Studio的solution，project文件，上手很简单。

### 1，环境的安装

#### 1.1 安装Ruby

Albacore是基于Ruby Rake的，所以先要安装Ruby，我是用Cygwin的，所以可以直接安装。如果是在Windows下安装Ruby，记得要把Ruby加到PATH中。这个网上有很多Ruby安装的教程。

#### 1.2 安装Rake和Albacore
Rake是Ruby下的构建工具，可以使用gem来安装：

`$gem install rake`

Albacore也是Ruby下的一个包，同样可以使用gem来安装：

`$gem install albacore`

### 2，一个简单的示例
假如我们有这样的目录结构：

![](http://images.cnitblog.com/blog/72292/201301/18121334-f7ba25d75b014954944f4b4c0bc55aee.png)

我们现在在项目的根目录(跟solution同目录)创建一个Rakefile(这个Rakefile类型与Makefile或Ant中的build.xml，是自动化构建的脚本），Rakefile内容是：

```ruby
require 'albacore'
 
task :default => [:build]
 
msbuild :build do |msb|
  msb.solution = "BuyLottery.sln"
  msb.targets :clean, :build
  msb.properties :configuration => :release
end
```

创建完成后我们就可以用直接在该目录下用rake命令在该目录下构建项目了。

### 3，讨论

Ruby的元编程真的很牛逼，看Rakefile的编写就知道了。Albacore直接利用了Visual Studio自带的MSBuild和项目定义文件，这不仅较少了麻烦，还减少了重复，Rakefile的功能集中与构建任务本身，而繁琐的任务还留在Visual Studio的项目文件中。

这里不得不提一下Rake，Rakefile中可以直接用Ruby脚本写你想完成的任务，比如创建目录，移动文件，等等。你所要用到的只是Ruby语言和其标准库。

Ruby在这里更像是一个平台，无论是gem, rake, albocore其实都是Ruby脚本而已。

### 4，Rakefile语法和Albacore提供的功能

#### 4.1，Rakefile
Rakefile的语法是源于Makefile，他主要有任务(task)和依赖(=>)组成。

```ruby
task :default => [:test]
 
task :test do
  ruby "test/unittest.rb"
end
```

上面的Rakefile有两个task，一个是default，如果你直接rake而不加task的名字，default task会被调用。第二个是test，在do…end直接你可以用Ruby完成任何你想完成的构建任务。对于default这个task而言他用=>指出的他的依赖项，依赖项是一个Ruby数组，这个数组列出了这个task的所有依赖项(其实也是个task)。

更详尽的Rakefile定义参见[Rakefile Format](http://rake.rubyforge.org/doc/rakefile_rdoc.html)。

#### 4.2，Albacore提供的其他功能

Albacore自定义了一些内置任务，比如我们示例中用到的msbuild，msbuild的目标是简化我们创建Rakefile task。示例中我们只要指定sln文件就可以构建一个项目了。其他的任务还包括：

```text
assemblyinfo    --版本号管理，其实就是操作AssemblyInfo.cs文件。
nunit           --NUnit测试
ncoverconsole   --
zip             --压缩打包
```

还有一些其他内置任务请参考Albacore的GitHub上的代码和示例。

### 5，参考

http://albacorebuild.net/

https://github.com/Albacore/albacore

https://github.com/Albacore/albacore/wiki/Getting-Started

http://code-magazine.com/article.aspx?quickid=1006101&page=1

http://rake.rubyforge.org/doc/rakefile_rdoc.html
