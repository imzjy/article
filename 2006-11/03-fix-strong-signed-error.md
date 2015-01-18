"引用的程序集没有强名称"解决方法
========

这几天在写C#，当引用到装配件`Shape.dll`，生成一个`ShapeUesr`的程序时，报错如下：

`程序集生成失败   --   引用的程序集“shape”没有强名称.`

针对此报错，先分析引用的`Shape`装配件，没有强名（程序＋公共＋版本）。

回到`Shape`程序，使用`sn -k shape.snk`，将`shape.snk`添加至以下一段：

`[assembly: AssemblyKeyFile("shape.snk")]`

然后再重新buiding成Shape.dll，此时Shape.dll已被强名。再使用ShapeUser引用该装配件时，便不会出现上面的问题了。

PS：

其实无论我们遇到什么事，乍一看是无头绪的。

但是静下心来，仔细观察出现的现象，给你的提示。

分析一下，找到问题根源所在。

问题也就迎刃而解了。
