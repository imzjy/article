在Visual Studio 2010[VC++]中使用ffmpeg类库
============

### 1，准备工作

很多播放器都使用了ffmpeg这个类库来编解码，使用没有关系，但总是有些人不守规则。在[耻辱榜](http://ffmpeg.org/shame.html)上我看到了腾讯(QQPlayer)，还有另一家深圳的公司。

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201103/201103311106299105.png)

我对GPL协议也不太了解，[issue tracker](https://roundup.libav.org/issue1519)中显示QQPlayer需要提供完整项目代码。我的疑问是：

> 如果是QQPlayer。其中集成了QQ的一些登陆模块，但这些代码不方便公开。但Player相关的代码已经公开。这样违反GPL吗？

NOTE:下文中`DLL`或`LIB`(大写指文件即`avcodec.dll`,`avcodec.lib`.etc.)，`dll`或`lib`(小写，指目录)。

继上篇在[MinGW中编译ffmpeg](http://www.cnblogs.com/Jerry-Chou/archive/2011/03/29/1998564.html)之后，我们便可以得到一些LIB和DLL，我们可以使用这些LIB和DLL来使用ffmpeg的相关功能函数。

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201103/201103311115087881.png)

其中头文件在`include`目录下，`LIB`及`DLL`在`bin`目录下。其实这些LIB并不是传统的静态库文件(真正的静态库文件是在lib目录下的*.a文件)，他们是dll的导出文件。

另外，C99中添加了几个新的头文件，VC++中没有，所以需要你[自己下载](http://msinttypes.googlecode.com/files/msinttypes-r26.zip)。并放至[相应目录](http://libav.org/general.html#SEC23)。对于VS2010来说通常是：`C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\include`。

### 2，示例代码

网上的ffmpeg的示例代码大多过时了，在2009年初[`img_convert`这个函数被`sws_scale`](http://dranger.com/ffmpeg/)取代了，所以可能你从网上找到的示例代码并不可以运行(但代码运作原理还是一样的)。

我这里贴出一份当前可以运行的代码。

+ View Code
 

显示代码中有几个地方需要注意一下。就是开头的宏定义部分。第一个是C99中添加了inline关键字，第二个是对ffmpeg头文件中INT64_C的模拟(可能也是为了解决与C99的兼容问题)。第三个是使用extern C在C++代码中使用C的头文件。

 

3，设置Visual Studio
在你编译，调用上面的代码之前你还要在Visual Stuido中做相应的设置，才可以正确引用ffmpeg的库。

3.1 设置ffmpeg头文件位置

右击项目->属性，添加Include文件目录位置：

image

 

3.2 设置LIB文件位置

image

 

3.3 设置所引用的LIB文件

image

 

如果一切正常，这时你便可以编译成功。

 

4，可能出现的问题
4.1 运行时出错

虽然你可以成功编译，但你F5，调试时会出现以下错误。

image

原因是，你虽然引用了LIB文件，但这并不是真正的静态库文件，而是对DLL的引用，所以当你调用ffmpeg库函数时，需要DLL文件在场。你可以用dumpbin(VS自带工具)来查看你生成的exe中引用了哪些DLL文件。你在命令行输入：

>dumpbin ffmpeg-example.exe /imports

你可以从输出中看出你实际引用以下几个的DLL文件。

avcodec-52.dll 
avformat-52.dll 
swscale-0.dll 
avutil-50.dll 

 

还有些朋友可能想将ffmpeg库进行静态引用，这样就不需要这些DLL文件了。这样做是可行的，但是不推荐的。

 

4.2 av_open_input_file失败

在VS的Command Argumetns中使用全路径。

image
