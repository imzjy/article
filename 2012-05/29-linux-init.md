Linux的init
======

Linux执行完一些初始化以后，第一个启动init进程。init进程是所有进程的父进程，负责启动其它进程，这些进程大多数是服务进程(daemon)。随着时间的推移这个启动过程也在变化。但目前主要有两种：System V style的runlevel式启动和upstart代表的event-based启动。

### 1，System V style的runlevel启动

init进程会读取/etc/inittab来决定进入哪一个runlevel。

`/sbin/init => /etc/inittab => runlevel  rc script [/etc/rcN.d]`

runlevel有些类似Windows中你按下F8进入的安全模式，但比Windows划分的更细，除此之外你还可以通过配置决定每个runlevel加载一些什么服务。不同的Linux发行版对runlevel的解释会有所不同，但runlevel思想是一样的：init通过/etc/inittab决定它的runlevel，然后去/etc/rcN.d/(N代表runlevel的数字表示)去找相应的启动脚本。

### 2，upstart是的启动

通过/etc/inittab的启动已经不能满足当前的需要了，比如支持一些热插拔设备。一种event-based的init启动产生了。ubuntu中就是使用upstart来启动系统的。upstart使用/etc/init/目录来决定系统在启动时运行那些服务。你可以通过intctrl来控制upstart启动的服务。

### 3，Ubuntu对System V style runlevel的模拟

你若查看/etc/init/目录，你可以看见一个为rc.conf的脚本，这个脚本起到的作用就是对system v style runlevel的模拟。我们看下这个脚本：

```text
# rc - System V runlevel compatibility
#
# This task runs the old System V-style rc script when changing between
# runlevels.
 
description "System V runlevel compatibility"
author      "Scott James Remnant <scott@netsplit.com>"
 
emits deconfiguring-networking
emits unmounted-remote-filesystems
 
start on runlevel [0123456]
stop on runlevel [!$RUNLEVEL]
 
export RUNLEVEL
export PREVLEVEL
 
console output
env INIT_VERBOSE
 
task
 
exec /etc/init.d/rc $RUNLEVEL
```

这个脚本通过执行`/etc/init.d/rc $RUNLEVEL`来运行具体的`rc script`。这些`rc script`在`/etc/rcN.d/`目录下。由此完成了对system v style runlevel的模拟。

不仅如此，ubuntu还提供了update-rc.d命令，你可以通过此命令来完成system v style runlevel启动脚本的配置。比如你想在启动时不启动apache：

`update-rc.d apache2 disable`

ubuntu将所有启动脚本放在`/etc/init.d/`这个目录下。当你运行update-rc.d命令时update-rc.d会根据你的参数新建一些symbol link到相应的/etc/rcN.d/目录。

`/etc/init.d/`目录下的启动脚本编写也比较简单，你可以参考`/etc/init.d/skeleton`这个示例。

---

update-2015-01-05:

[浅析 Linux 初始化 init 系统](http://www.ibm.com/developerworks/cn/linux/1407_liuming_init1/index.html) 
这三篇文章讲解了linux中init系统从`init script`到`upstart`再到`systemd`的进化过程。
