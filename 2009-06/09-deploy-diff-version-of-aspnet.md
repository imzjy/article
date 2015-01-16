IIS6.0 上布署不同版本的asp.net应用
====================

随着.net3.5的发布，当前.net已经有了好几个版本。常用的就是

- .net framework1.1;
- .net framework2.0;
- .net framework3.5;

我们在进行企业应用开发时难免会同时在几个版本的交叉。我们想要在一台server上布署多个版本asp.net应用需要注意以下方面。

### 1，Application Pool

IIS6.0采用隔离的worker process，每一个Application Pool对应一个隔离的工作进程(即w3wp.exe)。所以当你建立了多个Application Pool时，你会在任务管理器中看现多个w3wp.exe进程，如下图：

![](http://blog.chinaunix.net/photo/11680_090609141729.jpg)

每一个Application Pool只可以装载同一个版本的.net framework，也就是说不同版本的asp.net应用，必须建立各自的Application Pool。

具体的工作过程是：当一个访问者首次访问一个asp.net页面时，相应版本的.net framework会被装载进入Application Pool。当你试图在同一个Application Pool中布署两个不同asp.net应用时，会出现两个页面均无法访问，显示错误信息为：Server Application Unavailable。

最佳实践是你可以为.net版本创建不同的Application Pool，分别用来布署不同版本的asp.net应用。
 
 
### 2,Asp.net版本的设置

在布署完asp.net应用时，你需要设置asp.net应用的版本。

具体做法是：选中待设置的asp.net应用->右击->属性->ASP.NET标签下面的asp.net version下拉框中选择对应的net framework版本。注意asp.net3.5使用2.0的版本即可。


 
