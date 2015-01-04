NodeJS的包管理
=====

工作到第8年，有时会错觉地以为那些能学会的东西都已经学会了，这些年一年2门语言左右从C,C++,C#, Lisp, Ruby, Python, JavaScript一路跑来觉得没有啥可以再学的了。但是我错了，最近在看NodeJS的东西，这让我又一次地知道了业界前沿的技术，也知道其实还有许多可以学的。

编辑器也是相似的，开始Notepad++，后来Vim，后来Emacs，后来回到Vim，以为以后再也不换了，直到最近我又用上了Sublime Text 2，没有多久就将Vim抛干净了。

对于有些东西我以为我再也学不会了，比如Linux Kernel，从我当上程序员的时候我就在看，发现根本看不懂，其中几次拿起Linux Kernel Source来看都是没有看懂，时间一长我就知道了，这东西像个坎，我他妈的就是不可能爬过去的。不过最近好像有所变化，我视乎对Linux Kernel并不是很迷惘了，虽然还是很朦胧，但知道从哪里下手了。

NodeJS的包管理是使用npm(是Node Package Manager的缩写)。NodeJS包的设计相对Python的pip和Ruby的gem来说有一个很大的改变就是你可以选择将包安装在当前目录还是系统目录，并且默认是安装在当前目录。显而易见的好处就是你所安装的包作用域就在本地，你可以在同一个系统上安装不同版本的包。其次，你部署的时候可以将这个项目目录部署过去就可以了，不需要在服务器端安装相应的包，这对当下的Cloud Computing来说很好用，很多云服务并不提供Root权限的，比如RedHat的OpenShift。
在NodeJS中你可以运行下面的命令来安装一个包：

`$npm install express`

当你执行完这个命令后，你的当前目录会多出一个node_modules的目录，这个目录就是你的本地包的目录。你的所安装的express只是其中的一个目录而已。当你再安装另一个包的时候，就是在这个目录下添加一个对应的目录而已。比如：

`$npm install ejs`

安装完成后我们看下现在的目录结构：

```text
$ ls node_modules/
ejs  express
```
我们可以看到只是多了一个ejs的目录而已，如果想移除某个包可以用：

`$npm uninstall ejs`

这样做有一个缺点就是同一个包需要被安装多次。如果某一个包被很多项目引用，你可以将这个包安装系统目录(全局包)，这样新的项目就可以直接引用这个包而不需要安装了。

`$npm install –g ejs`

当系统中既有本地包，也有全局包的时候，本地安装的包优先。

现在很多的设计都采取这种区分本地和全局设置的例子，比如git的配置文件就有三个等级:

```text
--local      => only effect on current project
--system   => effect on current logined user
--global    => effect on whole computer
```
