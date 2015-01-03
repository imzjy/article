协程
===

一直对协程(coroutine)的概念不很很懂，看了Wiki中关于Coroutine的条目心里有点而谱了，至少知道协程是什么了。

通常我们的子例程，比如我们编程语言中的常用的函数，只有一个入口点(Entry Point)，那就是你调用这个函数时执行第一行代码，出口点有可能有多个，比如正常执行完最后一行代码，再比如使用return语言在任意一点退出函数。而数据的交换通过参数和返回值来实现。并且这个线程的调用栈，会有Caller的Stack Frame和Callee的Stack Frame。返回的时候Callee的Stack Frame被销毁。Callee能给Caller的也就是返回值。

### 什么是协程
协程比这个复杂一点，他可以有多个入口点。另一点是多次进入这个函数的时候，可以保持这个Callee的进程Stack Frame，所以执行中的环境并不会销毁和重建，而是使用上次执行时候的Stack Frame。有点需要说明的就是我们这里只考虑单线程的情况，这就变得好玩的。在单个线程中，你可以采用协作式的调用和环境保持，而不像多线程中的抢占。Wiki中给的例子是这样的：
```python
var q := new queue

coroutine produce 
    loop 
        while q is not full 
            create some new items 
            add the items to q 
        yield to consume

coroutine consume 
    loop 
        while q is not empty 
            remove some items from q 
            use the items 
        yield to produce
```
你可以指定写作的例程，然后通过Queue来做数据的交换。当前进程让出(yield)控制权给指定例程的时候，指定例程得到执行，而且还保存着上次执行时候的环境，比如内部定义的变量。

这也是像Golang中Goroutine的做法，只不过Goroutine是可以跨多个虚拟进程的。

如果一个协程没有使用yield的让出进程，而是执行完最后一条代码退出，这就跟我们普通的例程没有区别的。换种说法例程是协程的一个“特例”。

### 生成器
Python语言中生成器(generator)，生成器也可以让出控制权，而且保持上次执行时候的环境。这也是Python中generator最常用的地方，做迭代或者计数这样的工作。

比如Python中定义和使用一个计数器。
```python
def gen():
    print "start gen execution"
    for x in xrange(1,10):
        yield x


#调用gen函数创建生成器实例,但是其中的代码并没有执行
#gnext保存了当前生成器的状态，比如还未执行
gnext = gen()

print 'generator is not executed'
#next做了两件事
#1. 如果生成器还没有执行，开始执行。如果已经执行，resume到上次执行的位置继续下次执行
#2. 将当前yield expression的值返回给caller。
print gnext.next()  
print 'first execution and returned the value'

print gnext.next()
print gnext.next()
print gnext.next()
```
生成器也可以让出控制权，但是跟协程的区别是：生成器是一个能力削弱了的协程，他只能将控制权交给Caller，而不能将控制权交给指定例程。

那如果要实现producer->comsumer这样的模式的话，需要一个控制例程也就是caller来协调producer和comsumer这两个生成器实例。

### 实现协程
协程最大的优势就是能保持当前的环境，所以在实现的时候如果语言本身不支持协程，可以使用闭包(Closure)，用Closure去保持执行的状态，然后使用flag去控制执行流程。

实现了协程的语言在实现上也有很大的不同，但是基本原则就是解决两个问题：

1，保持当前协程的Stack在推出后不被释放

2，跳到上次yield位置继续执行剩下的代码
