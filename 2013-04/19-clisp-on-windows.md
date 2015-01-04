Windows下的Lisp(CLisp)开发环境搭建
======

虽然我也算个编程的老鸟，但是即使这样想找个可以用的Lisp环境也是特别困难，你很难在这一堆的Lisp实现中选择一个。选择就是煎熬，最后我选择了GNU CLisp(http://www.clisp.org/)。我在Windows下工作时间较多，所以选择了CLisp的Windows port。你可以从这里下载已经编译好的文件。

### 1，Lisp解释器的配置
解压下载好的Zip，然后将其放至C盘根目录下。重命名目录为clisp。在环境变量的PATH中添加：

`C:\clisp;`

![clisp](http://images.cnitblog.com/blog/72292/201304/19155632-f8848e0c0c7d49daaa3d84777f61f853.png)

### 2，配置编辑器

我使用的是Sublime Text 2，其实我们需要做的就是可以方便调用解释器来解释当前文件就可以了。我们先为clisp添加Build System。

![editor](http://images.cnitblog.com/blog/72292/201304/19155508-94eac71704d9418eae2fe174cf135fdb.png)

然后新建一个clisp的build，也就是:

```javascript
{
    "cmd": ["clisp", "$file"],
    "selector": "source.cl"
}
```

Sublime Text 2的build的参数及语法参见：Build System。

配置好了以后，我们新建一个clisp文件t.cl，在Sublime Text 2中打开该文件输入common lisp代码，然后直接Ctrl+B ,就可以看到结果啦。

![build](http://images.cnitblog.com/blog/72292/201304/19155633-dbbc2c4725b44e859e136cdb2f771bad.png)

 

### 3，其他资源

clisp解释器帮助文件：http://www.clisp.org/impnotes/clisp.html

common lisp的标准及实现：http://www.clisp.org/impnotes/
