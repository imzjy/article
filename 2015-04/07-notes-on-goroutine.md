goroutine笔记
============

### goroutine没有得到运行？

看下面一段Go的代码，我们起了一个goroutine，以我们的直觉(比如在C#中的ThreadPool)这个goroutine是可以得到执行的，我们可以看到打印出的结果。

```go
package main

import (
	"fmt"
)

func main() {

	go func () {
		fmt.Println("in go routine.")
	}()

	fmt.Println("in main execution.")

	for{
		
	}
}
```

然后goroutine中的代码却没有得到运行，只打印出了"in main execution."字符。

### 聊聊goroutine

goroutine是轻量级线程，他们同属于同一个进程中。我们使用goroutine来利用多核提高单机的并行能力，利用channel进行`进程内通信`。这是一个大前提，如果我们想跨进，跨机器通信我们还是使用Socket。

在这个大前提下，我们看看上面的例子，上面的例子中goroutine并没有得到机会运行。这样说隐含了两层意思：

1. goroutine没有得到时间片
2. 上面的例子没有利用到多核

### 让goroutine得到时间片

怎么样让goroutine得到时间片呢？一种方式是当前的执行体被IO阻塞，比如等待输入。其次是当前执行线体主动让出时间片。

#### 阻塞

1，等待IO输入
```go
func main() {

	go func () {
		fmt.Println("in go routine.")
	}()

	fmt.Println("in main execution.")


	//waiting io operation
	reader := bufio.NewReader(os.Stdin)
	reader.ReadString('\n')
}
```

2, channel阻塞

channel在等待队列空以输入，或者等待队列有元素读的时候会自动block当前的execution。这也是go中进程内通信的推荐方式。

```go
func main() {
	ch := make(chan int)

	go func () {
		val := <-ch
		fmt.Println("in go routine.")
		fmt.Printf("value from main execution: %d\n", val);
	}()

	fmt.Println("in main execution.")


	//channel block
	//waiting the comsumer to read
	ch <- 2
}
```

3, time.Sleep

我们还可以使用`time.Sleep`来让当前的执行体暂停固定时间，这样当前的执行体也会让出时间片。

```go
func main() {

	go func () {
		fmt.Println("in go routine.")
	}()

	fmt.Println("in main execution.")


	//sleep for current execution
	time.Sleep(100)
}
```

#### 让出时间片

go的runtime提供的一个函数`runtime.Gosched`可以让当前的执行体主动让出时间片。

```go
func main() {

	go func () {
		fmt.Println("in go routine.")
	}()

	fmt.Println("in main execution.")

	for {
		runtime.Gosched()
		os.Exit(0)
	}
}
```

### 使用多个CPU核心

如果go只是使用单个核心，那么所谓的并发就利用不到当前CPU多核化的优势，即现在的CPU有多个核心，可以同时运行几个执行体。golang的任务调度器当前没有自动化这一步，是一个不大不小的遗憾，过我们可以通过设置让golang的运行时使用CPU多个核心。

`runtime.NumCPU`方法可以让我们得到当前机器的CPU核心数。而`runtime.GOMAXPROCS`方法可以让我们设置当前golang的runtime使用的CPU核心数，也就是使用多个CPU核心，让任务同时执行。

```go
func main() {

	go func () {
		fmt.Println("in go routine.")
	}()

	fmt.Println("in main execution.")

	//increase the cpu number
	fmt.Printf("Numof CPU:%d\n", runtime.NumCPU())
	runtime.GOMAXPROCS(runtime.NumCPU())

	for{
		
	}
}
```

通过上面的示例我们可以看到，当前的CPU执行体虽然被阻塞，但是仍然不影响goroutine的执行。
