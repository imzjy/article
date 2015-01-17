C#中的委托(Delegate)和事件(Event)
======

把C#中的委托(Delegate)和事件(Event)放到现在讲是有目的的：给下次写的设计模式——观察者(Observer)有一个参考。

委托和事件应该是C#相较于C++等之前的非托管的语言提出的一个新的术语(term)。“旧瓶装新酒”这样的描述似乎有些“贬义”，但确实是这样。委托也好，事件也好最初的起源是C/C++中的函数指针，关于函数指针的简单介绍可以参见我以前的一篇《C/C++中指向函数的指针》。不过旧瓶装新酒没有什么不好，反而给人添加了许多新滋味。

### 1. Function pointer--the origin of delegates and events .

书回正传，既然函数指针是它们(委托和事件)的起源。那我们先看看什么情况下我们需要函数指针。函数指针最常用的方式就是回调(callback)——在函数休内回调主函数里的函数。有些绕口，看代码：

```c++
//Platform: WinXP + VC6.0
#include <iostream.h>
#include <list>
using namespace std;

void max(int a, int b)
{
    cout<<"now call max("<<a<<","<<b<<")..."<<endl;
    int t = a>b?a:b;
    cout<<t<<endl;
}
void min(int a, int b)
{
    cout<<"now call min("<<a<<","<<b<<")..."<<endl;
    int t = a<b?a:b;
    cout<<t<<endl;
}
typedef void (*myFun)(int a, int b); //定义一个函数指针用来引用max,min

//回调函数
void callback(myFun fun, int a, int b)
{
    fun(a,b);
}
void main()
{
    int i = 10;
    int j = 55;
    callback(max,i,j);

    callback(min,i,j);
}
```

Output:

```text
now call max(10,55)...
55
now call min(10,55)...
10
Press any key to continue
```

输出的结果有可能另一些对函数指针不熟悉的朋友我些意外，我们并没在`main()`中显式调用`max()`, `min()`呀，怎么会调用到它们呢。再仔细检查一下：你可能发现了：

`callback(max,i,j)`

这个函数调用了`max()`，这下好了。你便可以回答类似于这样的问题：我怎么在一个函数(callback)体内调用**主调用函数**中的函数`max`或`min`，最好能通过参数指入具体需要指定哪一个函数?

这便是函数指针的作用了，通过转入函数指针，可以很方便的回调(callback)另外一些函数，而且可以实现参观化具体需要回调用的函数。

### 2,Introduce delegate in c#;

.net里一向是"忌讳"提及"指针"的，"指针"很多程度上意味着不安全。C#.net里便提出了一个新的术语:委托(delegate)来实现类似函数指针的功能。我们来看看在C#中怎么样实现上面的例子。

```csharp
//Platform: WinXP + C# in vs2003
using System;
namespace Class1
{
    class ExcelProgram
    {
        static void max(int a, int b)
        {
            Console.WriteLine("now call max({0},{1})",a,b);
            int t = a>b?a:b;
            Console.WriteLine(t);
        }
        static void min(int a, int b)
        {
            Console.WriteLine("now call min({0},{1})",a,b);
            int t = a<b?a:b;
            Console.WriteLine(t);
        }
        delegate void myFun(int a, int b); //定义一个委托用来引用max,min

        //回调函数
        static void callback(myFun fun, int a, int b)
        {
            fun(a,b);
        }
        [STAThread]
        static void Main(string[] args)
        {
            int i = 10;
            int j = 55;
            callback(new myFun(max),i,j);
            callback(new myFun(min),i,j);
            Console.ReadLine();
        }
    }
}
```

其实代码上大同小异，除了几个`static`申明以外(C#除静态成员外必须要求对象引用),最大的变化要算定义"函数指指"，哦...不..不..不..应该是定义"委托"(小样穿上马甲了..). 定义委托的语法如下：

`delegate void  myFun(int a, int b);`     //定义一个委托用来引用max,min

其中`delegate`是关键字，`myFun`是委托名，剩下的是函数签名(signature).我们可以申明一个委托：

`myFun Max = new myFun(max);`

那么上面的回调函数的代码便可以写成：`callback(Max,i,j);`

### 3, Difference between function pointer and delegate;

委托除了可以引用一个函数外，能力上还有了一些加强，其中有一点不得不提的是:多点委托(Multicast delegate).简单地讲就是可以通过一个申明一个委托，来调用多个函数，不信？我们只要稍微更改一下上面的C#代码中的Main函数就可以了，类似：

```csharp
static void Main(string[] args)
{
  int i = 10;
  int j = 55;

  myFun mulCast = new myFun(max);
  mulCast += new myFun(min);      //(1)

  callback(mulCast,i,j);
  //callback(new myFun(min),i,j);
  Console.ReadLine();
}
```

输出如下：

```text
now call max(10,55)...
55
now call min(10,55)...
10
Press any key to continue
```

没骗你吧，我们只用了一个委托`mulCast`便同时调用了`max`和`min`。不知你注意到没有，上面代码的(1)处用"+="给已经存在的委托(mulCast)又加了一个函数(min)。这样看来C#中的委托更像一个函数指针链表。实质是在C#中，delegate关键字指定的委托自动从System.MulticastDelegate派生.而System.MulticastDelegate是一个带有链接的委托列表，在callback中只需调用mulCast的引用便可以以同样的参数调用该链表中的所有函数。

如果还是觉得不过隐，那我们就继续，下图展示了刚才那段C#代码的IL（用ILDasm反汇编即可）:

![](http://blog.chinaunix.net/photo/11680_071130131317.gif)

在C#中委托是作为一个特殊的类型(Type,Object)来对待的，委托对象也有自己的成员：BeginInvoke, EndInvoke, Invoke。这几个成员是你定义一个委托时编译器帮你自动自成的，而且他们都是virtual函数，具体函数体由runtime来实现。我们双击一个callback，可以看见以下IL：

```text
{
  // 代码大小       9 (0x9)
  .maxstack  8
  IL_0000:  ldarg.0
  IL_0001:  ldarg.1
  IL_0002:  ldarg.2
  IL_0003:  callvirt   instance void Class1.ExcelProgram/myFun::Invoke(int32,
                                                                       int32)
  IL_0008:  ret
} // end of method ExcelProgram::callback
```

从这段IL我们可以看出，当我们使用语句：`fun(a,b)`时，调用的却是委托对象(即然委托是类型，那么他自也就会有对象)的`myFun::Invoke()`.该委托对象(即上面的mulCast)通过调用Invoke来调用对象本身所关系的函数引用。

那我们再看看，一个委托对象是怎么样关联到函数的呢，我们双击Main函数，可以看到以下IL，虽然IL语法复杂但仍不影响我们了解它是怎么样将一个委托关联到一个(或多个)函数的引用的。

```text
.method private hidebysig static void  Main(string[] args) cil managed
{
  .entrypoint
  .custom instance void [mscorlib]System.STAThreadAttribute::.ctor() = ( 01 00 00 00 )
  // 代码大小       58 (0x3a)
  .maxstack  4
  .locals ([0] int32 i,
           [1] int32 j,
           [2] class Class1.ExcelProgram/myFun mulCast)
  IL_0000:  ldc.i4.s   10
  IL_0002:  stloc.0
  IL_0003:  ldc.i4.s   55
  IL_0005:  stloc.1
  IL_0006:  ldnull
  IL_0007:  ldftn      void Class1.ExcelProgram::max(int32,
                                                     int32)
  IL_000d:  newobj     instance void Class1.ExcelProgram/myFun::.ctor(object,
                                                                      native int)
  IL_0012:  stloc.2
  IL_0013:  ldloc.2
  IL_0014:  ldnull
  IL_0015:  ldftn      void Class1.ExcelProgram::min(int32,
                                                     int32)
  IL_001b:  newobj     instance void Class1.ExcelProgram/myFun::.ctor(object,
                                                                      native int)
  IL_0020:  call       class [mscorlib]System.Delegate [mscorlib]System.Delegate::Combine(class [mscorlib]System.Delegate,
                                                                                          class [mscorlib]System.Delegate)
  IL_0025:  castclass  Class1.ExcelProgram/myFun
  IL_002a:  stloc.2
  IL_002b:  ldloc.2
  IL_002c:  ldloc.0
  IL_002d:  ldloc.1
  IL_002e:  call       void Class1.ExcelProgram::callback(class Class1.ExcelProgram/myFun,
                                                          int32,
                                                          int32)
  IL_0033:  call       string [mscorlib]System.Console::ReadLine()
  IL_0038:  pop
  IL_0039:  ret
} // end of method ExcelProgram::Main
```

从上面的IL可以看出对于语句：

`myFun mulCast = new myFun(max);`

是通过以max作为参数构建一个委托对象mulCast。但对于语句：

`mulCast += new myFun(min);`

等价于：

`mulCast = (myFun) Delegate.Combine(mulCast, new myFun(min));`

哦,原来是通过调用`Delegate.Combine`的静态方法将`mulCast`和`min`函数进行关联，`Delegate.Combine`方法只是简单地将`min`函数的引用加至委托对象`mulCast`的函数引用列表中。

### 4,Introduce event;

事件/消息机制是Windows的核心，其实提供事件功能的却是函数指针，你信么？接下来我们再看看C#事件(Event).在C#中事件是一类特殊的委托.

一个类提供了"事件"，那么他至少提供了以下字段/方法：

1. 一个委托类型的字段(field)，用来保存一旦事件时通知哪些对象。即通知所有订阅该事件的对象.别忘记C#中委托是支持多播的。
1. 两个方法，以委托类型为参数。作用是将订阅该事件的对象方法加至上面的委托类型字段中，以便事件发生后可以通过调用该方法来通知对象事件已发生。

我们简单地定义一个类Test，该类支持事件：

```csharp
class Test
{
  public event EventHandler OnClick;

  public void GenEvent(EventArgs e)  //引发事件方法
  {
    EventHandler temp = OnClick;
    //通知所有已订阅事件的对象
    if(temp != null)
     temp(this,e);
  }

}
```

我们反汇编这段代码，如下图：

![](http://blog.chinaunix.net/photo/11680_071130153630.gif)

简单地定义一个字段哪来的那么多方法？其实这都是编译器帮你加上去的。当你定义一个事件时，编译器为了实现事件的功能会自动加上两个方法来提供“订阅”和“取消订阅”的功能。

通过下面的语法，你便可以订阅事件：

`test.OnClick +=new EventHandler(test_OnClick);`

也就是说，一旦`test`事件发生时(通过调用`test.GenEvent()`方法)。`test`便会调用注册到`OnClick`上的方法。来通知所有订阅该事件的对象。

**订阅是什么？** “订阅就是调用定义事件时自动生成的`add_OnClick`”。“那取消订阅就是调用定义事件时自动生成的`remove_OnClick`”，恭喜你！都学会抢答了.对于上面的订阅事件语句，逻辑意义上等同于：

`test.add_OnClick(new EventHandler(test_OnClick));`

但C#并不能直接调用该方法，只能通过 `+=` 来实现。来看IL：


```text
  IL_003b:  ldftn      void Class1.ExcelProgram::test_OnClick(object, class [mscorlib]System.EventArgs)           //先将test_OnClick压栈
  IL_0041:  newobj     instance void [mscorlib]System.EventHandler::.ctor(object, native int)                     //new一个委托对对象
  IL_0046:  callvirt   instance void Class1.ExcelProgram/Test::add_OnClick(class [mscorlib]System.EventHandler)   //通过调用add_OnClick方法将上面生委托加至test的事件(委托列表)中.
```

### 5,summarize.

如果对设计模式中的观察者模式较为熟悉的话。其实支持事件的类也就是观察者模式中的Subject(主题，我个人比较喜欢这么译).而所有订阅事件的对象构成了Observers.

最后来句总结吧，总结也许不严谨，但提供理解那还是绝佳滴..我骗你..(鼻子又变长了).....

- "委托"是"函数指针"链表，当然该链表也可以只有一个元素，如果这样的话:"委托" 约等于 "函数指针";
- "事件"是一类特特殊的"委托"，你定义一个"事件",表示你同时定义了:一个委托+两个方法。

后记：如果还不理解事件，先不要急，说不定你先把它忘记不想，等会一闪光，你就会理解了。或者你等着我下一篇《设计模式----观察者(Observer)》，我想等你看完设计模式中的观察者之后再回来看"事件"，看"多播委托(MulticastDelegate)"应该可以:忽然开朗。

如果还觉得不过隐。下面给出一个很好的帮助理解的例子，来自Jeffrey Richter.希望我的注解能帮上些忙：

```csharp
using System;
using System.Text;
using System.Data;

namespace Class1
{
    //定义事件引发时，需要传的参数
    class NewMailEventArgs:EventArgs
    {
        private readonly string m_from;
        private readonly string m_to;
        private readonly string m_subject;
        public NewMailEventArgs(string from, string to, string subject)
        {
            m_from = from;
            m_to = to;
            m_subject = subject;
        }
        public string From
        {
            get{return m_from;}
        }
        public string To
        {
            get{return m_to;}
        }
        public string Subject
        {
            get{return m_subject;}
        }

    }

    //事件所用的委托(链表)
    delegate void NewMailEventHandler(object sender, NewMailEventArgs e);

    //提供事件的类
    class MailManager
    {
        public event NewMailEventHandler NewMail;
        //通知已订阅事件的对象
        protected virtual void OnNewMail(NewMailEventArgs e)
        {
            NewMailEventHandler temp = NewMail; //MulticastDelegate一个委托链表
            //通知所有已订阅事件的对象
            if(temp != null)
                temp(this,e); //通过事件NewMail(一种特殊的委托)逐一回调客户端的方法

        }
        //提供一个方法，引发事件
        public void SimulateNewMail(string from, string to, string subject)
        {
            NewMailEventArgs e = new NewMailEventArgs(from,to,subject);
            OnNewMail(e);
        }
    }


    //使用事件
    class Fax
    {
        public Fax(MailManager mm)
        {
            //Subscribe
            mm.NewMail += new NewMailEventHandler(Fax_NewMail);
        }
        private void Fax_NewMail(object sender, NewMailEventArgs e)
        {
            Console.WriteLine("Message arrived at Fax...");
            Console.WriteLine("From={0}, To={1}, Subject='{2}'",e.From,e.To,e.Subject);
        }
        public void Unregister(MailManager mm)
        {
            mm.NewMail -= new NewMailEventHandler(Fax_NewMail);
        }
    }
    class Print
    {
        public Print(MailManager mm)
        {
            //Subscribe ,在mm.NewMail的委托链表中加入Print_NewMail方法
            mm.NewMail += new NewMailEventHandler(Print_NewMail);
        }
        private void Print_NewMail(object sender, NewMailEventArgs e)
        {
            Console.WriteLine("Message arrived at Print...");
            Console.WriteLine("From={0}, To={1}, Subject='{2}'",e.From,e.To,e.Subject);
        }
        public void Unregister(MailManager mm)
        {
            mm.NewMail -= new NewMailEventHandler(Print_NewMail);
        }
    }

    class ExcelProgram
    {
        [STAThread]
        static void Main(string[] args)
        {
            MailManager mm = new MailManager();
            if(true)
            {
                Fax fax = new Fax(mm);
                Print prt = new Print(mm);
            }

            mm.SimulateNewMail("Anco","Jerry","Event test");
            Console.ReadLine();
        }
    }
}
```
