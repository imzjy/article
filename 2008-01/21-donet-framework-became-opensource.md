.Net Framework开源了
========

Microsoft .Net Framework开源了,对开发者而言,这是一个值得欢呼的事情.就我个人从学习的角度来考虑,很希望看到Microsoft的源码,很希望看到杰出程序员的Source Code.有什么能比"源码"更让人心服口服呢!这一下子把整个Framework的类库公开了,还可以任意使用F11进行step into,以后遇到一些puzzle,一不用猜疑,二可以学习.快乐呀,快乐.

Scott的Blog最先报到了这一为人振奋的时刻,现将其翻译如下:


### .Net Framework类库公开源码

去年10月份,我曾在日志里记录了我们计划发布.net Framework类库的源码,并同时在Visual Studio 2008里支持源码的调试.今天我很高兴地宣布:从现在开始每个人都可以使用.net Framework类库的源码.特别是你现在就可以调试和浏览以下类库的源码:

- .NET Base Class Libraries (including System, System.CodeDom, System.Collections, System.ComponentModel, System.Diagnostics, System.Drawing, System.Globalization, System.IO, System.Net, System.Reflection, System.Runtime, System.Security, System.Text, System.Threading, etc).
- ASP.NET (System.Web, System.Web.Extensions)
- Windows Forms (System.Windows.Forms)
- Windows Presentation Foundation (System.Windows)
- ADO.NET and XML (System.Data and System.Xml)

我们正在将另外的一些类库(包括LINQ,WCF和Workflow)添加到上面的列表中.一旦它们将要发布我会在数周前向大家详细播报.

#### 在Visual Studio 2008中使用RSA(Reference Source Access)

仅需花几分钟做相应的设置,你便可以在Visual Studio 2008中打开源代码访问功能.Shawn Burke有一篇相关blog,其中包括了每一步设置的详细说明.
如果你遇到了一些问题,或是设置中有一些疑问.请在MSDN的Reference Source Form版块中发贴以寻求帮助.

#### 走进.Net Framework类库源码

一旦你按照Shawn Burke的blog配置完成后,你就可以动态地加载.Net Framework类库debug symbols(译注:调试标志,此处应指pdb文件)和一步步地进入(step into)源码.当你在.Net Framework的源码中进行调试时,VS2008将会自动下载debug symbols和源代码文件.

![](http://blog.chinaunix.net/photo/11680_080123085449.png)

在源码中还包括了开发者的注释.从上面你可以看到Control基类的Dispose方法以及相关的注释.

有时你会看到在注释中会引用一些过去的bug/tracking编号,这些编号是保存在我们的bug/work-item追踪数据库中,该数据库包括一些特定代码决议的历史信息.举个例子,上面的注释指出了(call out)为了保持和早些时候发布的.Net Framework的兼容性,那个特定的字段不能设置为null.同时也标注了一个向后兼容性的bug(译注:编号为VSWhidbey475904)因此而被修复了.

#### 引用许可(Reference License)

.Net Framework的源码是在Read-only引用许可下被发布的.在十月份时,当我们宣布我们将发布源码时就有人担心引用许可会对他们查看这些源码带来潜在的冲击.为了澄清和消除这些担忧,我们对该份许可(License)做了小小的改动,特别地指明该份许可并不用应用到用户为非windows(non-Windows)开发软件.哪怕该平台(now-Windows平台)与.Net Framework有着相同或相似的功能或特征.如果你是在Windows平台下面开发,你可以"观看"源码,甚至让你的软件和.Net Framework有着相同或相似的功能或特征.

#### 小结

我们认为发布.Net Framework的源码和在VS中集成了源码的调试功能,对.Net的开发者而言,这将会很有用处.让.Net Framework类库的源码可以完整的访问和查看,这会让你更好的了解.Net Framework类库是怎么样实现的,接下来使你创建更好的应用,让这些源码体现出更多的价值.

希望这会给你带来帮助.

Scott

-----

总言之,Microsoft能将他的部分源码公开,对所有开发者来说,特别是.Net平台的开发者,将会从中受益良多.对应用来说,了解.Net Framework本身,让应用可以更好地被创建.对学习来说,能看见那些杰出程序员的代码,还有注释.还有比这更让人值得高兴的吗?

开发者的快乐,探索的快乐,是交流的快乐.
