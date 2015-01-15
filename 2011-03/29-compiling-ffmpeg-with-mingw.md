在MinGW下编译ffmpeg
==========

因为需要使用ffmpeg的相关库和执行文件，所以需要编译最新的ffmpeg代码。为了能在编译成Windows native执行程序(需要在.net中调用该执行程序)，这里我们使用MinGW。

### 1，安装MinGW

下载MinGW，双击安装，我当前使用的版本是20110316的。

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201103/201103291112205235.png)

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201103/201103291112214787.png)

添加Windows环境变量：

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201103/201103291112237446.png)

BTW:对于使用Cygwin的朋友，为了不影响cygwin的HOME目录，可以在`C:\MinGW\msys\1.0\msys.bat`文件的最开头添加以下代码。

`set "HOME=C:\MinGW\bin"`

为了生成Win32下原生的Lib供使用，还需要在该文件开头添加以下代码。

`call "C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin\vcvars32.bat"`

[参考一](http://www.ffmpeg.org/general.html#SEC24)， [参考二](http://www.cnblogs.com/bruceleeliya/archive/2010/11/16/1878424.html)

### 2，下载ffmpeg源代码

ffmpeg官方网站上，下载ffmpeg源代码包，我下载的版本是2011-03-23，这个对我而言已经比较新可以使用了。如果你需要更新的代码，可以使用：

`$git clone git://git.videolan.org/ffmpeg.git  ffmpeg`

下载最新版本的源代码。

### 3,编译ffmpeg

#### 3.1 了解编译选项

将ffmpeg源代码放至/var目录下，目录是随意的，我这里只是示例。然后`./configure –help > config-options.txt`

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201103/201103291112243377.png)

然后，你可以通过查看`config-options.txt`来了解可用的选项。

#### 3.2 根据选项来编译ffmpeg

```shell
$ ./configure  --enable-memalign-hack  --enable-static --enable-shared --enable-avfilter-lavf
$make
$make install
```

编译成功后，就可以在默认路径/local/bin目录中找到exe及lib文件了，头文件位于/local/include。

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201103/201103291112253245.png)
