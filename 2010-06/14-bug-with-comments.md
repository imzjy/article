由注释引起的问题
========

前些日子泰国的同事将更新的网页发给我们，让我们更新我们的网页。但网页一更新到我们的服务器上就要会现以下报错。

```text
Microsoft VBScript compilation error '800a03f6'
Expected 'End'
xxx.asp, line 52
```

咋一看，以为是语法错误，少了一个End，根据提示找到相应文件的52行。

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/WindowsLiveWriter/d67277e7b2de_9492/expect_end_thumb_1.png)

即上图中的 `vValid_hour=48`。我们仔细检查的`If…End`的配对，并没有发现问题。最终一个同事无意地将那段泰文（乱码）的注释删除，一切就OK了。

知道问题出现在哪里，找根源就容易多了。用Notepad++显示不可见字符——一切尽收眼底：

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/WindowsLiveWriter/d67277e7b2de_9492/expect_end_comment_thumb.png)

原来乱码将一个`<CR>`吃掉了。结果`End if`被作为注释而注释掉了。

Windows下`<LF>`只做特殊字符来处理，并不作为换行来处理。对于编译器来讲上面的代码如下：

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/WindowsLiveWriter/d67277e7b2de_9492/expect_end_compiler_view_thumb.png)

知道的原因，我们再回头看看最初的报错信息感觉也就不那么突兀和茫然了。由此我们也可以积累一条经验：对于注释（特别是乱码的注释）我们在调试的时候可以先将其删除。不过要记住使用源代码管理工具，需要时保证原文件可以还原。

