Debug/Release版运行结果异同--GC的引子
==========

有时我们在运行程序时，会出现Debug版本和Release版本运行结果不一致的情况。现给出C#中的一个例子，这个例子是Jeffrey在他的《CLR via C#》中"垃圾回收"这一章给出的，很有意思。

其实大家也会猜测，Debug版和Release版编译后的代码肯定会有不一样的地方，是的!是会这样的。要不然也不会出现运行结果不一致，呵呵!闲话不说我们来看看代码，代码很简单。(调试环境WinXP + VS2003 + C#)

```csharp
class Program
{
    [STAThread]
    static void Main(string[] args)
    {
        TimerCallback tm = new TimerCallback(ShowTime);
        Timer t = new Timer(tm,null,0,2000);

        Console.ReadLine();
        //t.Dispose(); (1)
    }
    private static void ShowTime(Object o)
    {
        Console.WriteLine(DateTime.Now.ToString());
        GC.Collect();  //强制GC (2)
    }
}
```

你可以在Debug版本中运行一下，会发现该报时程序工作正常(一直会报时)。而在Release版本中时间报只显示一下。

为什么呢？这是因为我们在(2)处强制了一次GC(Garbage Collect)即垃圾回收。在Release版中当我们程序运行到GC.Collect()时，Timer类型对象t是可以被GC的。但Debug版本中t是作为一个本地参数而不能被GC的。

我们再分解一下整个过程(仅列出关键过程)：

1. 创建Timer类型对象t;
2. t定时调用委托tm;
3. tm方法执行;
4. tm方法进行Garbage Collect;
5. 待读取一行字符;(其间t定时器重复执行步骤2)
6. 退出;

可以看出第4,5步是个关键，如果我们一直等待输入就能不停打印。但问题是：在Debug版中确实是这样的，在Release版中却只打印了一次....How mysterious!

```text
TOM:    这时t是不是不工作了？
JERRY:  对的，如果是Release版本中，至第5步时t确实不工作了，因为:它已经不存在了，被GC了.
TOM:    不....不....不,你慢一点，别忽悠我^_^!!!，那Debug版为什么它就不被GC呢？
JERRY:  这是因它，它在Debug版中不符合GC的条件.
TOM:    你鼻子变长了....
JERRY:  不信? 你看...这,这,这,诺..还有这.
```

为了让TOM相信这是真的，JERRY用ILDasm分别打开了Debug版本和Release版本的程序并双击打开Main方法.

**Debug版**:

```text
.........省略了一些行........
// 代码大小       32 (0x20)
.maxstack  5
.locals ([0] class [mscorlib]System.Threading.Timer t)
IL_0000:  ldnull
IL_0001:  ldftn      void Class1.Program::ShowTime(object)
IL_0007:  newobj     instance void [mscorlib]
                   System.Threading.TimerCallback::.ctor(object,native int)
IL_000c:  ldnull
IL_000d:  ldc.i4.0
IL_000e:  ldc.i4     0x7d0
IL_0013:  newobj     instance void [mscorlib]System.Threading.Timer::.ctor
                   (class[mscorlibSystem.Threading.TimerCallback,
                   object,int32,int32)
IL_0018:  stloc.0
IL_0019:  call       string [mscorlib]System.Console::ReadLine()
IL_001e:  pop
IL_001f:  ret   //仍可使用t对象
} // end of method Program::Main
```

在Debug版中我们定义的t是作为一个本地参数(locals[0])，在`IL_0018`位置,它参考到新new的`Timer`对象.这时需要注意一点是的，即使在`IL_001f`处，仍通过`locals[0]`引用到`t`对象.

所以在托管堆(Managed Heap)中，该对象仍象是可达对象(Reachable object).也就不符合被回收的条件。所以只要`Main`函数不结束，`t`就不能被回收。

**Release版**:

```text
.........省略了一些行........
// 代码大小       32 (0x20)
.maxstack  5
IL_0000:  ldnull
IL_0001:  ldftn      void Class1.Program::ShowTime(object)
IL_0007:  newobj     instance void [mscorlib]
                   System.Threading.TimerCallback::.ctor(object,native int)
IL_000c:  ldnull
IL_000d:  ldc.i4.0
IL_000e:  ldc.i4     0x7d0
IL_0013:  newobj     instance void [mscorlib]System.Threading.Timer::.ctor
                   (class[mscorlibSystem.Threading.TimerCallback,
                   object,int32,int32)
IL_0018:  pop
IL_0019:  call       string [mscorlib]System.Console::ReadLine()
IL_001e:  pop
IL_001f:  ret    //至此，也没有办法可以refer to至t对象,t可以被Garbage Collect
} // end of method Program::Main
```

而在Rlease版中位置:`IL_0018`只用了`pop`方法弹出该对象(也就是`t`对象).这相当于丢弃了`t`对象，这时`t`被标记为可回收。

但有一点需要了解的是：`t`虽被丢弃，还仍存活在托管堆(Managed Heap)中，直到`t`调用`ShowTime`，而在`ShowTime`函数中调用GC为止。当`ShowTime`中调用GC时，由于t被标记为可回收，所以`t`对象被回收。整个过程看起来是这个样子的：

![](http://blog.chinaunix.net/photo/11680_071207114901.gif)

正是由于在Release版本中t是作为临时变量，用完后被GC强制回收，所以`t`只能工作一次，便通过调用GC结束了自己的生命，可怜的娃!

为了使Debug版和Release运行结果保持一致，你可以有两个选择：

1. 在Console.ReadLine只后调用t.Dispose(),即取消我最先给出的代码的(1)处的注释。因为t对象在创建之后还要被引用，所以创建的t对象也被作为一个本地参数来保存，生成的IL如下：
  
  `.locals init (class [mscorlib]System.Threading.Timer V_0)`

2. 注释掉我最先给出的代码的(2)处的GC.Collect函数的调用.这样虽然在Release版中t对象已被标识为可回收，但些时没有内存需求(这只是一个假设)，CLR并不会回收t对象.
  
  显然方法2是不可取的，我们只把希望寄托在CLR不进行Garbage Collect，但在现实编程中这是不现实的。在t被触发的间隔间谁也不能保证CLR不进行Garbage Collect.若使用方法2我稍改了一下代码，Release版本的程序又不能工作了。

```csharp
class Program
{
    [STAThread]
    static void Main(string[] args)
    {
       Timer t = new Timer(new TimerCallback(ShowTime),null,0,500);
       System.Threading.Thread.Sleep(1000);  //新增
       Thread gc = new Thread(new ThreadStart(GcCollect));//新增
       gc.Start();  //新增
       Console.ReadLine();
    }
    private static void ShowTime(Object o)
    {
        Console.WriteLine(DateTime.Now.ToString());
    }
    private static void GcCollect()  //新增
    {
        GC.Collect();
    }
}
```

这段代码中，我虽没有在`ShowTime`中进行GC，但另一个线程的`CoCollect`函数却调用了`GC.Collect`，这会迫使CLR进行Garbage Collect。`t`只是存活了一小会儿，仍旧被回收了。

但若使用方法1，上面这段代码在Release版本中仍能正常工作。

后记，Garbage Colletion是一个似乎很神秘的东西。因为时常我们并不知道什么时候CLR进行Carbage Collect.以前常常将.net程序性能不好的原因都"嫁祸"在GC的头上，其实这是片面的。真正的原因是我们不了解GC，不了解GC的工作原理。
