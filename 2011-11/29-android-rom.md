继续折腾Android，TouchPad, Defy
======

### 1，Android is based on Linux

Android从根本上就是一个Linux嵌入式系统，所以Linux上的知识基本上都可以搬到Android系统上来用。严格上来讲，并不存在Android系统，Android是基本Linux以上的一个Framework。只不过我们买手机/平板时都说成Android系统而已。我们来看一张Android结构图：

![](http://developer.android.com/images/system-architecture.jpg)

### 2，有关于刷机

我的手机是Defy，所以我就以Defy来示例Defy怎么刷机。

先进入Bootloader：

1. 关闭手机
2. 启动手机时，同时按住电源及音量上键。

这时你就可以插上USB线用RSD Lite来刷机了。

对于G1等手机，你可以用类似于RSD Lite的Fastboot方式来刷机。每家设备刷入Rom的方式都不一样，比如HP的TouchPad，你就需要novacom来将新的ROM拷贝至TouchPad。novacom is a program offered by HP for communicating from your computer to the TouchPad。

所谓的刷机工具，指的就是你用来在你的电脑上，与你的设备之间通讯的工具。通常就是一个自定义协议，这个协议通过USB Cable或TCP跟设置进行通讯(执行命令，传输文件，比如ROM）。由于自定义协议，所以ROM的格式也是不同的，有的是*.sdf文件，有的是*.img文件，有的是直接写入ROM存储。

比如:

```text
Defy -> RSD Lite/MotoHelper
G1   –> FastBoot
TouchPad –> novacom
```

为了解决这个麻烦和方便以后刷机，一般拿到手机后，可以刷入ClockWorkMod（刷入一个微系统至/Recorvey目录），将手机引导Recovery模式，借助于这个东西我们可以将任意ROM刷入手机。

### 3,怎么通过novacom连接TouchPad

在WebOS中重启，按住音量上键，看到一个大大的USB标示。插上USB线，用novacom –l看是否连接上。如果连接上了，用terminal连入，进行recovery。terminal可以通过点击下面的bat来启动，启动后需要点击File->Connect来连接到TouchPad：

`C:\Program Files\Palm, Inc\terminal\novaterm.bat`

### 4,有关启动

Android系统的启动，首先是Bootloader的启动，如果这时你按了一些组合键，会装载recovery.img，这样就会进入Recovery模式。

如果你没有按组合键，这时Bootloader会将Linux Kernal装载进来，进入Kernal的初始化，比如装载驱动，启动服务，挂载根文件系统等。

内核启动完成后，进入user space的初始化，`/init`命令执行`init.rc`,`init.<machine_name>.rc`，dalvik VM启动，一些系统服务启动。

接着system_server启动，activity manage启动一些核心的dalvik程序，比如桌面。


---

参考

http://blog.chinaunix.net/space.php?uid=7788581&do=blog&id=2558375

http://elinux.org/Android_Booting

http://bootloader.wikidot.com/linux:boot:android

http://vinnysoft.blogspot.com/2009/12/android-boot-process-from-power-on.html
