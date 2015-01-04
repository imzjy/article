Go语言学习
======

### 1，函数

#### 1.1 函数的定义
Go支持匿名函数和闭包，Go的函数类似Python可以返回多个值。Go也是静态编译型的语言。先来看看Go的函数定于格式：

```golang
func 函数名(参数表...) [(返回值...)] {
    //函数体
}
```

注意：

1. 返回值在参数表后定义，如果只有一个返回值，那么返回值两边的括号是不要的，如果没有返回值那么返回值这一项可以省略。
2. 函数体的开始大括号必须在行尾，这是强制的，类似的if, switch中的也是如此。
3. 如果函数名大写字母开头，那么就是对外可见的(exported, public)。如果是小写字母那么就是包内(package level)私有的。

#### 1.2 成员函数定义

```golang
func (t *type) 函数名(参数表...) [(返回值...)] {
    //函数体
}
```

这样就可以为type定义一个成员函数了。

#### 1.3 函数的嵌套

你可以在一个函数体内定义匿名函数甚至你可以定义匿名函数，然后用变量去引用这个匿名函数。但是你不可以在函数体内嵌套定义一个具名函数。

```text
func main() {
    func () {
        fmt.Println("anonymous func is ok")
    }()
 
    var foo = func () {
        fmt.Println("using a variable to refer anonymous func is ok")
    }
    foo()
 
    func notAllow() {
        fmt.Println("you can not define named func")
    }
}
```

匿名函数在这里有值(value type)的语义。你可以像对待一个值那样去对待匿名函数（当参数传递，作为函数返回值）。但是具名函数不享有这种优待。相对于JavaScript或Lisp这样的语言，他缺少了“可以在任意位置定义函数”的能力。在Go中，匿名函数有这种能力。

### 2，构建系统(build)

#### 2.1 GOPATH

当前的项目目录要添加到GOPATH中，你可以用$go env来检查你当你的环境变量，包括GOPATH。

如果，你想列出当前目录下所有的包(packages)，可以使用

$go list ./…

当你GOPATH设置过了以后，你所有以go开头的命令，都是以GOPATH指定的项目目录为起始目录的。

比如：

$go test algorithm/bubblesort   #目录为[项目ROOT]src/algorithm/bubblesort，go test是找src目录下的还有test的包

 

3，三个点(…)
对于定义不定参数数量的函数需要三个点…:

1
func(a, b int, z float64, opt ...interface{})
最后一个为任意类型的的不定参数，用…来标明。

还有个时常用到…的地方是对数组切片添加元素，当添加的元素是数组或数组切片类型的，append(arr, …T)需要将元素“打散”以当做不定参数来传递，这时也要用到…:

1
2
s2 := append(s1, 3, 5, 7)  //一个一个传递
s3 := append(s2, s0...)    //将数组“打散传递”
 

4，goroutine
goroutine是Go语言在语言级别对并发的支持。并发执行体的粒度从系统到轻量级线程分别有：进程，线程，轻量级线程。goroutine应该算是轻量级线程，在我的电脑上(Win7, Intel i7)可以在3s内创建大约300,000个goroutine。

对于并发来说最大的问题是同步和通信，在Go语言中同步和通信是通过语言内置的channel来近乎完美解决的。channel不仅仅是goroutine通信的方式，也通过自动阻塞这种方式达到了同步的目的。channel可以作为函数的参数传来传去，channel这个参数在使用上像一个引用类型。他可以跨“函数”传递消息。然而实际上他是值类型，channel是函数通信的边界，你不能通过channel来执行还有副作用的赋值操作——当然，除了你通过传递一个指针硬要这么做。

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
package main 
import "fmt"
 
func intGenerator(ch chan int) {
    for i := 0; i < 10; i++ {
        ch <- i    //pass the i to the channel
    }
    close(ch)  //close the channel
}
 
func main() {
    var ch chan int = make(chan int)
    go intGenerator(ch)
    for {
        val, ok := <-ch  //if channel closed, the ok will be false
        if ok {
            fmt.Println(val)  
        } else {
            return
        }
    }
}
