Ubuntu 10.10下使用电信3G网卡
=========

把我的本本换成Ubuntu后，原本的电信3G网卡却没有办法使用了。最终从官网上下载了驱动，这才使用3G网卡登上了网络。

### 1，根据网卡型号去官网上下载驱动。

http://www.vnet.cn/cwclient/download.htm

### 2，解压并安装

```text
jerry@jerry-ThinkPad-R61:~/Downloads$ ls
ChinaTelecom_huawei_linux_install.tar.gz
jerry@jerry-ThinkPad-R61:~/Downloads$ tar zxf ChinaTelecom_huawei_linux_install.tar.gz
jerry@jerry-ThinkPad-R61:~/Downloads$ ls
ChinaTelecom_huawei_linux_install.tar.gz linux_install
jerry@jerry-ThinkPad-R61:~/Downloads$ cd linux_install/
jerry@jerry-ThinkPad-R61:~/Downloads/linux_install$ ls
ChinaTelecom.tar.gz Driver install jre-1_6_0_14-linux-i586.bin readme.txt
jerry@jerry-ThinkPad-R61:~/Downloads/linux_install$ sudo ./install
```

### 3，安装成功后，就可以使用
你可以使用电信自带的Java写的拔号程序。但是比较慢。

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201103/201103152146172602.jpg)

或者，你可以System->Preference->Network Connections->Mobile Broadban自己创建一个连接。这样拨号比电信自带的拨号程序快多了。

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201103/201103152154592259.jpg)

注意，当你使用Network Connection登出后，再次连接时可能连接不上。这时你可以将modem-manager干掉，再重新连接就好了。我也不知道为什么，但这样确实有用。

`$ sudo pkill modem-manager`

后记：使用[ScribeFire写Blog](http://www.cnblogs.com/Jerry-Chou/archive/2011/03/13/1982912.html)确实没有Windows Live Writer爽。
