从JQuery中的Deferred对象谈谈异步编程
======

JQuery中的[Deferred Object](http://api.jquery.com/category/deferred-object/)其实就是实现了一种异步编程模式，这个模式在[CommonJS](http://wiki.commonjs.org/wiki/Promises)中有介绍。这种模式改变的代码的书写方式，他采用的异步模式还是回调式异步(async callback)。通常我们的异步代码都是non-blocking的，我们开一个异步操作，我们不知道什么时候完成，我们需要知道的就是这个异步操作在完成的时候通过我们传入的callback来通知我们。

具体Deferred Object怎么用，可以参考阮一峰的《[jQuery的deferred对象详解](http://www.ruanyifeng.com/blog/2011/08/a_detailed_explanation_of_jquery_deferred_object.html)》。我这里想谈的是异步编程模式。现在我们的整个internet就是异步的，你获取一个页面这个页面的处理，返回都是以一种异步的方式在工作，所以现在编程很难绕开异步。而基本上目前所有的异步，都是观察者模式的变种，即subscribe,publish式的。而区别就在于subscrible的时间和约定或者说是语法。常见的异步编程模式有：

### 1，notification, message, intent

这种模式在iOS和Android都有用到。这种异步的决定权在接受者，对于发送者而言，只要发一个notification, message, intent说我想做什么，具体的工作由接受者来完成，并且返回结果或者对其他可用的对象的引用。notification, message, intent中还可以包含了当任务完成后的执行代码，当任务被接受和完成后调用相应的代码。

### 2，event based

事件式异步也差不多，在一个object上attach一个event，当这个object的状态发生改变的时候调用这个注册的函数。C#中WinForm的编程就是这种模式。他的代码也体现了这种编程模式：

`btnDone.OnClick += new ClickCallback(btnDone_click);`

事件式编程与上面的notification式的区别就是，事件是预先attach在object上的。这里的关注点在object，以object为中心。object不存在了，那么事件就无从谈起了。而notification式的异步关注点在事件本身，也就是以事件为中心。发送者和接受者唯一关联的就是这个事件，事件发生执行完了，发送者和接受者就没有关系了，直到下次事件发生。

### 3，others

其他的变种还有很多例如.net中的[Task-based async(TAP)](http://msdn.microsoft.com/en-us/library/hh873175.aspx)和[APM](http://msdn.microsoft.com/en-us/library/ms228963.aspx)，最大的区别就在于管理异步的注册的方式不同。TAP把这些都抽象在Task这个对象中，C# 5.0中新加的await, async把这种注册方式集成在语言中。
