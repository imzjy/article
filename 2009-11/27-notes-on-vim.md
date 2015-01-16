Notes on Vim
==========

整理了一下Vim方面的笔记，在某些方面填补了国内空白——就是有关tab和space的说明（背景音：脸皮好厚，大家扔西红柿）。

```text
1,打开水平滚动条
  a,set guioptions+=b #(bottom scrollbar)
  b,set nowrap

2,滚屏
  a,一行[向下:ctrl+e, 向上:ctrl+y(Win32+p)]
  b,半屏[向下:ctrl+d, 向上:ctrl+u]
  c,整屏[向下:ctrl+f, 向上:ctrl+b]

3,移动可视屏的行(针对自动折行时有效)
  a,下移可视屏的一行 gj
  b,上移可视屏的一行 gk

4,进入Visual(选择)模式
  a,单个字符   [v]
  b,整行       [shift+v]
  c,Block      [Win32:ctrl+q, Unix:ctrl+v]

5,折行
  a,创建折行--[zf{motion}]
  b,打开--[zo] 打开所有嵌套折行--[zO]  打开所有折行--[zR]
  c,折起--[zc] 折起所胡嵌套折行--[zC]  折起所有折行--[zM]
  d,删除--[zd] 删除所有折行(在折行的最初一行才有效)--[zD]
  e,显示左边折行标记: set foldcolumn=4

6,显示控制字符[help listchars]
  a,set listchars=tab:>-,eol:$,trail:-
  b,trick&tips:using searching hightline:
    b,1: [/\t] -- show tabs.
    b,2: [/\s\+$]  -- show trailing whitespace.
    b,3: [/ \+\ze\t]  -- show spaces before a tab.

7,显示行号
  a,set number
  b,set nonumber

8,字符宽度控制
  a,每行显示字符数量：textwidth=72
  b,缩进所占字符数量：shiftwidth=2 | 增加当前行缩进(以空格填充)：>>
  c,Tab所占字符数量 ：tabstop=4
    b.1, tabstop -- (显示的角度)一个tab所占字符长度(从底层来讲二进制编码：0x09);
    b.2, softtabstop -- vim特定的一种表示，当按下tab键时要补全(包括已前面键入的空格)的空格总数(0x20)。
      例如，softtabstop=4时，
      >>光标前有1个空格时，你按下tab会添加3个空格，以补全4个空格; 
      >>而当光标前已有2个空格时你按下tab则会添加2个空格，以补全4个空格。 
      >>光标前已有4个空格时，不用补全。继续进入一下轮，发现只有0个空格，所以一次被足4个空格。--相当于连key了4下空格键
      注意(关键点)：当按下softtabstop补全的空格数(包括已前面的已有的空格)可以产生tab时，vim自动将前面所有空格按tabstop的宽度(每tabstop宽度个0x20)转换成tab(一个0x09)字符
    b.3, expandtab --将tab转换成空格(expand the tab as blankspaces where you are typing,the amount of expanding based on settings of softtabstop/tabstop)
    b.4, retab {number} --根据number重新计算tab(tab周围的空格也被算在内),
      例如：当前tabstop=8,当你[retab 2]的时候执行两个动作：
      >>第一步，将一个tab(原本tab占8个字符)拆为4个tab(现在tab占2个字符)。
      >>第二步，将tabstop设为2。

9,以二进制方式查看文件
  a,%!xxd -- 整个文件(%)dump为二进制格式
  b,%!xxd -r -- 将文件反转为原来的格式

10,自动补全
  a,I_CTRL_P--Previous Match, I_CTRL_N--Next Match
  b,I_CTRL_X(进入补全模式) + CTRL_O

11,特殊字符
  a,I_CTRL_V + {special char} 或 I_CTRL_V + {digits} [Win32上用CTRL_Q代替CTRL_V]
  b,怪异符号(合体字,Digraphs) I_CTRL_K + {digraphs} | :digraphs -- Show all of digraphs
  c,查看当前光标下的字符编码 [ga]

12,比较缓冲区与原文件--显示已做的改动
  a,DiffOrig

13,加法，减法
  a,加法: {count}CTRL+A -- 将光标下的数字加上count.(Win32下先用unmap取消CTRL+A的“全选”功能)
  b,减法: {count}CTRL+X

14,大小写变换
  a,gue --当前字符 guw --当前word
  b,gUe --当前字符 gUw --当前word 

15,虚编辑
  a, set virtualedit=all -- 可以将光标移动到一行中的任意位置(列)。
    注意：若该不是一个空白行(blank line & empty line)，则光标会自动回到行尾。
    >>如果想避免该问题可以先用r进行替换，替换时至光标位置的所有空白将自动以空格填充。
  b, 虚替换：gr或gR(进入虚替换模式) -- 可以让被替换的字符占据应有的空间位置，这对替换tab(0x09)时特别有用。

16,快速移动
  a,f+{character} 向前查找一个字符(停在该字符上) 
  b,F+{character} 向后查找一个字符(停在该字符上)。

17,跳转光标
  a,``(两个脱字符) 回到之前的位置。注意:w,b,fx之类的命令不能算是跳转。
  b,CTRL_O 跳回(older)
  c,CTRL_I 向前跳

18,程序内的移动
  a,[+{ --该block头, [+/ --该注释头, [+m --该函数头
  b,]+{ --该block尾, ]+/ --该注释尾, ]+m --该函数尾

19,格式化程序代码
  a,== 当前行， gg=G 整个文件
  b,按文件类型自动缩进: filetype indent on

20,格式化文本
  a, set textwidth=78
  b, gggqG  --格式化整个文档

21,删除空行
  a, :g/^$/d  --删除空行
  b, :g/\s\+/d --Delete trailing whitespace.

22,Vim脚本中的变量
  a,脚本特殊变量
    $NAME  环境变量名
    &name  Vim中的选项名(例如ts,sw)
    @name  Vim中的寄存器名
  b,变量作用范围标识
    name  函数局部
    b:name  局部于一个缓冲区
    w:name  局部于一个窗口
    g:name  全局变量
    v:name  Vim预定义变量

99,Windows下对应的组合键被占用的解决方法
  a,unmap {<C-A>}  -- 取消Windows下CTRL+A(全部选择)的功能。

# vim:set shiftwidth=2 foldmethod=indent tabstop=8: #
```
