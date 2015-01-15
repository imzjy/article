Emacs中的Color Theme以及字体设置
==========

先上一张效果图：

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201102/201102211813354705.png)

Color Theme用的是gnome2, 字体用的是Visual Studio自带的Consolas。我使用的环境是Windows+Cygwin+Emacs23.2。

### 1,安装Color Theme插件

首先，从http://download.savannah.gnu.org/releases/color-theme/下载color theme 6.6.0版本。

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201102/201102211813367703.png)

接着将color-theme-6.6.0.tar.gz解压到~/.emacs.d/plugins/文件夹

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201102/201102211813363559.png)

将下面的代码贴到.emacs文件中：

```lisp
;;;Color Theme 
(add-to-list 'load-path "~/.emacs.d/plugins/color-theme-6.6.0") 
(require 'color-theme) 
(color-theme-initialize) 
(color-theme-gnome2)
```

重新启动Emacs, 你会发现Color Theme 起作用了，界面的颜色发生的变化。你可以使用如下命令来查看当前可用的Themes：

`color-theme-select`

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201102/201102220851268643.png)

将光标移动到相应的ColorTheme上，回车就可以预览该Theme。如果选中哪个Theme，将其写入.emacs文件，以便下次Emacs在启动时便应用该Theme。

所有的ColorTheme的定义存储在`~/.emacs.d/plugins/color-theme-6.6.0/themes/color-theme-library.el`文件中，你可以在此处添加自定义Theme(即一个Lisp函数)。

### 2,更改Emacs使用的字体

将下面的两行加到.emacs配置文件中。

```lisp
;;set font family 
(set-default-font "-outline-consolas-normal-r-normal-normal-14-97-96-96-c-*-iso8859-1")
```

整个配置部分如下所示：

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201102/201102211813363002.png) 

至此，所有工作都做完了。运行emacs，这时你就会看到你的Emacs变得帅帅的了。

----

参考:

http://www.emacswiki.org/emacs/ColorTheme
