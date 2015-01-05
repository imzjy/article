Ubuntu 12.04 LTS不能登录的解决
=====

昨天我用gdb来调试一个程序，总是用list来查看代码不是很方便。我就想让terminal有两个窗口，一个用Vim来查看代码，另一个用gdb来调试代码。经过Google，我安装了screen和byobu。经过一番折腾，我并不喜欢这个工具，随即我将其卸除。悲剧来了：

当我重启Ubuntu后怎么也登录不了Gnome，症状为我一输入密码并通过验证后他又返回登录窗口(dumps me back to login window)。

我Ctrl+Alt+F1进入了命令行。这时用我的账号密码是可以正常登录的。我又用Gnome的Guest账号也是可以登录的。那就说明是我装载个人配置时出了问题。这好办，我们看看home目录下都有些什么？

最先让我看到的是.xsession-errors这个文件。这个文件记录的X Windows登录失败的信息。

`cat .xsession-error`

文件中有一行：

`Can't open /usr/bin/byobu-launch`

这下找到原因了，原来是找不到byobu的启动文件。解决方案很简单：

1. 安装byobu重新F9配置byobu让其关闭`Byobu currently launches at login`
2. 安装byobu后继续使用

我选择了继续使用，原因是Emacs虽然虽然可以用buffer来打开任何东西，但是这不符合Unix思想：一个工具只做一件事。

经过熟悉，我发现byobu确实不错，是我所需要的，只是要花些时间学习而已。
