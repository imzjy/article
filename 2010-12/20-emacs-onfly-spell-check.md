Emacs即时检查单词拼写--解决Enabling Flyspell mode gave an error
===============

Emacs支持即时拼写检查，即on-the-fly spelling checking。通常只需在Emacs中运行：

`M-x flyspell-mode`

即可打开即时检查。但在输入该命令时可能会出现以下报错：

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201012/201012202216433670.png)

由于flyspell-mode是启动一个单独的小程序ispell，借用些实用工具实现单词拼写检查/纠错。对于flyspell-mode的介绍可以参考[EmacsWiki](http://www.emacswiki.org/emacs/FlySpell)。

[ispell](http://www.gnu.org/software/ispell/)这个小工具虽是GNU系统的一部分，但不是[GNU程序](http://www.gnu.org/philosophy/categories.html#TOCGNUprograms)。GNU中对应的替代程序是[aspell](http://www.gnu.org/software/aspell/)。具体区别请参考各自的网站。本例所用的是aspell。

既然Emacs靠此工具执行即时检查，我们先测试一下这个工具是否正常工作：

`jerry@ubuntu:~$ cat mistake.txt | aspell –a –l en`

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201012/201012202216486829.png)

原来是aspell没有安装，这个好办。我们安装aspell：

`jerry@ubuntu:~$ apt-get install aspell`

由于默认地Emacs使用ispell作为拼写检查程序，我们需要在.emacs文件中加入以下内容来，修改flyspell-mode的默认拼写检查程序：

`(setq-default ispell-program-name "aspell")`

一般情况下，这样就可以了。我们可以到Emacs中使用`M-x flyspell-mode`来启用即时检查。

但有时当你在Emacs执行`M-x flyspell-mode`会出现类似以下的错误：

> ispell-init-process: Error: The file "/usr/local/lib/aspell/xxxxxx   can not be opened for reading.

这是为什么呢？我们再次测试aspell是否正常工作：

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201012/201012202216503500.png)

原来是用来支持aspell的字典没有安装，执行以下命令安装字典：

`jerry@ubuntu:~$ sudo apt-get install aspell-en`

安装完成后，测试：

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201012/201012202216557149.png)

一切正常，这时我们可以再次打开Emacs，并用M-x flyspell-mode打开即时检查。

问题依旧，别发狂，如果你是在Ubuntu10.10中，请参考Stackoverflow上的这篇帖子，这是一个Bug，不是你的错 :)。接着我们删除几个多余文件：

```text
/usr/share/emacs/site-lisp/dictionaries-common/debian-ispell.el 
/usr/share/emacs/site-lisp/dictionaries-common/flyspell.el 
/usr/share/emacs/site-lisp/dictionaries-common/ispell.el

and all the .el .elc files in

/usr/share/emacs/23.1/site-lisp/dictionaries-common
```

经过此番折腾，我们再次`M-x flyspell-mode`开启即时检查。

小样，你终于出来了。

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201012/201012202216592575.png)
