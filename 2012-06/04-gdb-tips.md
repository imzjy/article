gdb调试
====

### 1，gdb的一般调试过程

- 你先用gcc –g 参数生成带调试符号的二进制文件
- gdb prog_name加载待调试的文件
- l(list) [func_name | line_num]查看源文件
- b(break) [func_name | line_num] 在函数或具体的行上加上断点
- info breakpoints 查看当前所有断点
- r(run)运行程序，程序会在断点的位置停下来
- bt(backtrace) 查看程序的调用路径，也就是call stack。
- 可以用up和down在调用栈中移动，借此可以使用p命令打印当前call stack上的临时变量。
- p(print) var_name 查看一个变量的值
- display var_name 自动打印变量的值
- s(step into)，以step info的方式执行代码
- n(next statement)，以next statement的方式执行代码。
- c(continue)，你想让程序继续执行，直到下次击中断点。
- q(quit)退出gdb

### 2，常用命令的说明

To be continue….

### 3，小技巧

- *执行上次命令* 直接回车 ，比如你上次s(step)，你还想继续s(step)，直接回车即可。


----
update-2015-01-05:

更多gdb的技巧参见:

https://github.com/hellogcc/100-gdb-tips/blob/master/src/index.md
