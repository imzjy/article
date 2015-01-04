在Amazon云上使用Dropbox来部署应用
======

我们需要将自家的应用迁到云上，也就是Amazon的EC2上，在前端我们用Load Balancing来做负载均衡，
后端用EC2的instance来提供服务。由于后端有能有很多的instance，所以在部署的时候怎么样把应用在这些instance上同步是一个问题。

最早，我们想到了自动化的Push，也就是在服务器端开个SSH或FTP服务然后写个脚本将要更新的内容Push到这个后端的instance中。
这样做有两个问题：

1. 部署过程太慢。
1. 需要打开在服务器上打开SSH或FTP端口增加了安全隐患。
1. 添加新的Instance需要修改部署脚本。

经过一段时间的自动化Push后，我突然想起以前看Twitter的更新，好像使用BT的，这样更快。这给了我一点启发：
我们可以也用现成的云服务来实现后端的自动同步，最后我选择了Dropbox。原因有两点：

1. 他可以选择文件夹同步，这样一个Dropbox账户可以给不同的应用使用。
1. Dropbx提供了Linux下的自动同步功能，你可以在CLI下用他们提供的脚本来操作Dropbox的同步服务。

### 1，创建Dropbox账户

你可以去www.dropbox.com创建一个账户，免费有2G的空间，这基本上对大多数的应用来说都够用了。

创建完成后如果你是Windows用户，请下载客户端：https://www.dropbox.com/downloading?os=win

如果你是Linux，请移步：https://www.dropbox.com/install?os=lnx

对于Linux你需要知道你是32位版本的Linux还是64位版本的Linux，你通常可以通过$uname -a或者$cat /proc/cpuinfo 来得知。

Dropbox提供了Linux下操作Linux服务的工具dropbox.py，具体的使用方式参见：http://www.dropboxwiki.com/Using_Dropbox_CLI

 

### 2，选择要同步的文件夹

在Windows上，你可以在初始化的时候选择要同步的文件夹，也可以安装后更改：

![dropbox](http://images.cnitblog.com/blog/72292/201305/10094946-cdd41207744d4821af46cc38f6e47bab.png)

在Linux，你可以$dropbox.py exclude add /path/to/ignore去掉那些你不想同步的文件夹。

设置完成后就简单了，你需要部署的时候你就直接用Visual Studio的publish，直接部署到本机dropbox文件夹，这样你的Windows EC2 instance就自动更新了。

如果你是Linux，你还可以在Windows下写应用，然后一个copy脚本将应用copy到本机dropbox的一个目录下就可以将更新的内容同步到Linux EC2 instance上了，以此来部署新的应用。

### 3，一些要注意的项

1. 将代码/文件与数据分开

在同步时，我们同步的是整个应用的文件夹，而应用生成和使用的数据我们要放到单独的文件夹，这样在同步时才可以相互不受影响。

对于需要集中的应用数据我们统一放在S3上。
