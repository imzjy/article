异步与非阻塞的区别(Difference between asynchronous and non-blocking)
==========================

在看一些框架的时候，比如Tornado，在实现层面有的时候会提到non-blocking。有的框架会说使用async的技术。那么究竟non-blocking与async有没有什么区别呢？

下面是我的理解：

1. 很多时候没有区别。当我们再谈论异步和非阻塞的时候，我们通常是指一个API调用需要多久，会不会因此而影响性能，让调用方等待。比如，我们在Window编程的时候，如果我们的UI线程做一些费时的工作，那么我们的应用就会卡顿，造成不好的用户体验。这时无论是我们采用异步，还是非阻塞都可以解决这个问题——即都可以让调用快速返回。当我们谈论API调用返回速度的时候，async和non-blocking没有区别。
1. 当我们讨论两个线程调用时的控制权，async和non-blocking就有区别了。当线程A，调用API函数B。如果线程A一调用，结果是现成的就返回结果，结果需要计算就返回不可用的状态。这就是non-blocking，也就是说这时控制权还是在主调线程中(没有block主调线程)。如果是async的调用，那么当线程A去调用函数B，这时控制权已经由A传给B了。B有权决定什么时候返回结果(即调用回调函数)，甚至可以不返回结果。

所以Tornado声称自己是non-blocking的主要原因是Tornado设计时决定的，Browser访问Tornado Server，随即返回结果。使得别的Browser可以继续请求Tornado的资源。

既然这是设计决定，那就不是技术实现。也就是说你在实现的时候，比如你让Tornado的调用花很长时间才返回，那么所有调用者都会卡在那边(Tornado是单线程Server)。作为实现者，你不可以让调用者花费太多时间，如果实在需要，那还是要使用async调用。

这跟我们用IIS可不一样，IIS中，你一个Web访问耗时太久不会影响另一个客户端，IIS会用不同的线程来处理。而Tornado中如果你如果阻塞了一个线程，那么整个Server都是不可用的。那么问题就来了，如果一个Web访问可能耗时太久怎么办？

Tornado的官方Wiki是这样说的：

1. 让访问不耗时(这基本是废话)。
1. 使用异步的库，比如AsyncHttpClient。
1. 创建Message Queue，让一个进程单独处理。
1. 交由另一个线程处理。

---
Reference：

https://github.com/facebook/tornado/wiki/Threading-and-concurrency

http://stackoverflow.com/questions/2625493/asynchronous-vs-non-blocking

http://my.oschina.net/digerl/blog/30456
