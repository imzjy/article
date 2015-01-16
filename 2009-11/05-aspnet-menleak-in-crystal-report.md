Asp.net中水晶报表无法释放问题
======

### 现象： 

近来在程序中使用了水晶报表(Crystal Report)——在一个页面中用水晶报表生成PDF文档。程序运行良好，但有一个很奇怪的问题：程序运行一段时间后就必须重起一下IIS。

### 分析过程：

我用Process Explorer对IIS进程检查发现进程里有很多文件没有释放。如下图：

![](http://images.cnblogs.com/cnblogs_com/jerry-chou/CrystalRport_Unrelease.PNG)

IIS进程中充斥了很多临时文件没有释放。

### 解决方法：

在用到水晶报表的页面事件Page_Unload中，将水晶报表相关对象释放。

```vb
Imports DataBean
Imports DataSet1
Imports System.Data
Imports CrystalDecisions.CrystalReports.Engine
Imports CrystalDecisions.Shared

Partial Class _CrystallReportTesting
    Inherits System.Web.UI.Page

    Dim oRpt As New ReportDocument
    Protected Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load
        '' 水晶报表绑定
        oRpt.Load(Server.MapPath("CrystalReport4.rpt"))
        oRpt.SetDataSource(GetDataSourceFromOracle())
        '' 设定水晶报表的ReportSource
        CrystalReportViewer1.ReportSource = oRpt
    End Sub
    
    Protected Sub Page_Unload(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Unload
        oRpt.Close()    ''释放水晶报表对象
        oRpt.Dispose()
        System.GC.Collect(0)
    End Sub
End Class
```

**小插曲**：

在调式过程中，我发现每当页面加载时执行`Page_Load`事件之后（如果没有其它代码），将会紧接着执行`Page_Unload`事件。这怎么回事？我直觉地以为`Page_Unload`会在客户端将网页关闭时触发。  

这也是我记录这个事件的主要原因：我总是不自然地将Web的编程模式理解为Windows编程模式。将http无状态性本质遗忘。主观臆断，不经思考地认为`Page_Unload`会在客户端将网页关闭时触发——这怎么可能呢？对于ASP.NET执行模型来说，在IIS接到一个Get/Post请求时初始化一个与访问相关的页面类来处理该请求。并在处理完成后生成的HTML发送回客户端，之后该页面类等待被垃圾回收。

转一段网上的回帖，很好的回答了该问题：

> It's confusing for windows developer. Remember about Unload event defenition. "Occurs when the server control is unloaded from memory" after each load or post back in server side all controls Unloaded from memory. Remember we talking about web application all controls get alived by request and died when response create and send to client.So thats why after load event Unload event called. 

