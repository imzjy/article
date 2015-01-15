Emacs中使用Zencoding
========

上午公司停电，连不上服务器。所以正好找些时间来折腾Emacs。

周末在家看了emacs lisp introduction的第一章，无意间觉得Emacs中的”’”（apostrophe）有些像C语言的指针了。其实C语言和Lisp代表了两种风格，不是相容的风格，而是互补的的风格，一种在本源上一致的风格。

[Zen Code](http://code.google.com/p/zen-coding/)是一种书写标记语言的快捷方式，在Emacs中也有相应的实现。我们可以在Emacs安装相应的插件。

### 1，下载Zen Code的实现

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201101/201101110854006374.png)

### 2,将其拷贝到合适目录

本例是：`.emacs.d/plugins/zencoding/`

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201101/201101110854003866.png)

### 3，在.emacs中加入以下配置

```lisp
;;;Zen Coding 
;'zencoding-expand-line bound to C-Return 
(add-to-list 'load-path "~/.emacs.d/plugins/zencoding/") 
(require 'zencoding-mode) 
(add-hook 'sgml-mode-hook 'zencoding-mode) ;;Auto-start on any markup modes
```

这时你便可以使用ZenCoding了，使用`C-Ret`来绑定到`zencoding-expand-line`，借此来展开Zencoding表达式。

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201101/201101110854001881.png)

 -----
 
参考 :

http://code.google.com/p/zen-coding/ 

http://www.emacswiki.org/emacs/ZenCoding
