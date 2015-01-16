《Vim Recipes》翻译 – Basic Navigating
=================

[书接上回](http://www.cnblogs.com/Jerry-Chou/archive/2010/04/14/vim-recipes-choosing-the-right-mode.html)

### 浏览文档(Basic Navigating)
 
#### 问题

你想在一个文件中移动光标。

#### 解决方案

惯用的做法是使用方向键来上下左右地移动光标。Vim也支持这种风格地光标移动方法，但同时也提供了另外一种高效的移动方案。

```text
Key   Movement
h	    Left
l	    Right
k	    Up a line
j	    Down a line
0	    Start of line
^	    First character of line
$	    End of line
```

#### 讨论

旧习惯总是引诱我们使用惯用的移动方法。但若你使用Vim提供的方式将使你变得更加高效。其中一个原因是这些移动命令键都在主键盘部分，而不用将手移动到方向键的位置——这会降低你的速度。

另一个优点是：你可以在这些快捷键的前面加上一个数字（跟你在命令行前加的数字一样），用来指定你希望这些快捷键执行的次数。例如，用 2k 来向上移动两行

一旦你习惯了这些快捷键，翻看一下《通过移动来选择文本》中的移动和文本对象章节，你将会看到通过简单地结合h,l,k,j来使得vim命令更加强大。
