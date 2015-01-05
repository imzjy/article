Python的一些惯用法
=======

### 1，目录处理

```text
>>> os.getcwd()    #current working directory
'/home/jerry'
>>> os.path.realpath("/home/jerry/GitHub")      #如果是symbolic link就找到真实文件
'/home/jerry/GitHub'
>>> os.path.relpath("/home/jerry/GitHub")       #相对路径
'GitHub'
>>> os.path.split("/home/jerry/GitHub")         #路径拆分
('/home/jerry', 'GitHub')
>>> os.path.join("~","repo","snippets")         #目录连接
'~/repo/snippets'
>>> os.path.splitext("/home/jerry/GitHub.txt")  #windows上常用，返回扩展名
('/home/jerry/GitHub', '.txt')
```

在Python的对象中有些特殊的内置属性，比如我们Callable类型有下面的属性：

```text
>>> os.path.split.__doc__
'Split a pathname.  Returns tuple "(head, tail)" where "tail" is\n    everything after the final slash.  Either part may be empty.'
>>> os.path.split.__name__
'split'
>>> os.path.split.__module__
'posixpath'
```

对于模块，我们有`__file__`内置属性，通过这个属性我们可以得到模块所在文件

```text
>>> os.path.__file__    #当前模块所在的文件
'/usr/lib/python2.7/posixpath.pyc'
>>> os.path.__doc__     #模块doc string
```

剩下每种类型的内置属性可以参考：http://docs.python.org/reference/datamodel.html

### 2，模块的查找

有时候你运行单元测试python a-unit-test-run.py会发现单元测试的中import our-module会报错：`ImportError: no module named our-module`。这是应为Python搜索不到这个Module/Package

Python会在下面的目录查找Module/Package

1. 内置模块
2. 当前目录: `unit-test-script.py`所在目录
3. PYTHONPATH环境变量指定目录: `export PYTHONPATH=’/usr/jerry/python-modules`
4. 标准库: `system installation default`
5. sys.path: 可以通过`sys.path.appen('/usr/jerry/python-modules')`来添加

http://docs.python.org/tutorial/modules.html#the-module-search-path

如果你觉得这样运行单元测试比较繁琐，你可以[使用nose](http://schettino72.wordpress.com/tag/nose/)。

### 3，源代码的编码

如果你在python的源代码中加了中文的注释，在执行时会产生这样的报错：

```shell
$ python deoc.py
  File "deoc.py", line 39
SyntaxError: Non-ASCII character '\xe4' in file deoc.py on line 39, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
```

怎么办？出错的链接中给出了答案，你在文件的开头加上源文件编码说明：

```python
# -*- coding: utf-8 -*-
 
def foo():
    pass
```
