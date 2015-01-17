设计模式之观察者模式
======


设计模式中的观察者(Observer)模式我个人觉得是蛮好玩的。原因是原本这个模式并不难，道理也较容易懂，但就是这样我也是看了好几次才明白这个模式的用意是什么。其实模式本质真的是可以跨语言，很多时候模式是种思想:"**重用，解耦合**"。这种思想在GOF提出的23种模式中无处不在。

Observer，观察者模式。它还有个别名叫：发布--订阅.这个别名比较形象。时常上网的朋友都会在网上订一些网络杂志/消费记录通知等等。比如我就订了移动公司的每月话费清单，还订了天极网的每周杂志。正是这种服务商提供订阅，而消费者订阅相应的服务构成了观察者的雏形。

作为构建软件的你，或许更关心这些发布--订阅是怎么实现的。发布--订阅的真正好处是：可重用，松耦合。我们先来看看可重用。

可重用，无论对发布者(移动公司)或是消费者(订阅话费清单的人)来说。从软件角度来说他们都是可重用的，这体现在。发布者可以稍稍改动一下把话费清单改为积分通知，重用了原来的话费清单模块。订阅者也稍稍改动一下订阅联通公司的话费清单。这样在软件中，你重用发布部分也好，重用订阅人也好，随你.

松散耦合，移动公司新增了积分通知——你并不知道，也不需要知道。你订阅了联通公司的话费清单——移动公司并不知道，也不需要知道。

现在可以对号入座了，我们消费者就是观察者(Observer).我们观察我们每个月的消费记录。移动公司提供订阅的主题(Subject).我们先来看看Observer以及Subject都能做哪些事情。

Observer只需(被通知)话费清单已到.

```c++
class Observer
{
public:
    virtual void Received()=0; //收到通知后动作,阅读话费清单
};
```

Subject(移动公司),需提供

1. 一个接口让用户订阅话费清单(添加已订阅用户列表);
2. 一个接口让用户取消订阅话费清单(更新已订阅用户列表);
3. 发出通知告诉订阅用户话费清单已到.

```c++
class Subject
{
public:
    //Support Subscribe/Unsubscrible
    virtual void Attach(Observer* o);
    virtual void Detach(Observer* o);
    virtual void Notify();   //发送通知
private:
    list<Observer*> observers;  //已订阅用户列表
};
```

函数部分实现部分也很简单，提供上面所说的三种功能。

```c++
void Subject::Attach(Observer* o)
{
    observers.push_back(o);   //加至订阅用户列表
}
void Subject::Detach(Observer* o)
{
    observers.remove(o);     //从订阅用户列表中移除
}
void Subject::Notify()
{
     //通知所有订阅者
    list<Observer*>::iterator i;
    for(i=observers.begin(); i!=observers.end(); i++)      {
        static_cast<Observer*>(*i)->Received(this);
    }
}
```

现在我们定义出具体的一个Subject和具体的订阅人：

```c++
//定义一个具体Subject类(移动公司)
class Mobile:public Subject
{
public:
    Mobile(){ _checklist = "";};
    string GetChecklist();
    void SimulateChklst();
private:
    string _checklist;
};
void Mobile::SimulateChklst()
{
    cout<<"---------话费清单(Mobile.Suzhou)---------"<<endl;
    _checklist = "市话话费:17.52\t\t长途话费:57.00\n短信:5.00(包月)\t\t彩铃:2.00(包月)\n";
    Notify();
}
string Mobile::GetChecklist()
{
    return _checklist;
}
//定义一个具体观察者:Jerry --找移动公司订阅(到移动大厅让移动服务人员订阅)
class Jerry:public Observer
{
public:
    void Received(Subject* sender);
};
void Jerry::Received(Subject* sender)
{
    cout<<"Jerry收到话费通知:"<<endl
        <<static_cast<Mobile*>(sender)->GetChecklist()
        <<endl;
}
//定义另一个具体观察者:Anco --由观察者自已订阅(上网自助订阅)
class Anco:public Observer
{
public:
    void Subscribe(Subject *subject);
    void Unsubscrible(Subject *subject);
    void Received(Subject* sender);
private:
    Subject _subject;
};
void Anco::Received(Subject* sender)
{
    cout<<"Anco收到话费通知:"<<endl
        <<static_cast<Mobile*>(sender)->GetChecklist()
        <<endl;
}
void Anco::Subscribe(Subject *subject)    //自助订阅
{
    subject->Attach(this);
}
void Anco::Unsubscrible(Subject *subject)  //自助取消订阅
{
    subject->Detach(this);
}
```

我们的类，看起来是下面这个样子的：

![](http://blog.chinaunix.net/photo/11680_071205120949.gif)

其中需要注意那一段注释：

```c++
for(all o in observers){
   o->Received();
}
```

这段注释道出了Observer的另一个重点：由基类Notify统一维护各观察者的状态，这样可以确保观察者都可以得到通知。这给解耦合带来了绝佳的效果。
我们再也不用担心，谁去维护这个状态，状态怎么样保持一致。

现在我给出完整的代码：

```c++
//Platform: WinXP + VC6.0
#include <iostream>
#include <string>
#include <list>
using namespace std;
//--------------------------------------------------
//An abstract class define the Observer's interface
class Subject;
class Observer
{
public:
    virtual ~Observer(){};
    virtual void Received(Subject* sender)=0; //传入sender，支持多主题Subscribe
protected:
    Observer(){};
};
//An abstract class define the Subject's interface
class Subject
{
public:
    virtual ~Subject(){};

    //Support subcribe
    virtual void Attach(Observer* o);
    virtual void Detach(Observer* o);
    virtual void Notify();
public:
    Subject(){};
private:
    list<Observer*> observers;
};

void Subject::Attach(Observer* o)
{
    observers.push_back(o);
}
void Subject::Detach(Observer* o)
{
    observers.remove(o);
}
void Subject::Notify()
{
    list<Observer*>::iterator i;
    for(i=observers.begin(); i!=observers.end(); i++)
    {
        static_cast<Observer*>(*i)->Received(this);
    }
}
//--------------------------------------
//定义一个具体Subject类
class Mobile:public Subject
{
public:
    Mobile(){ _checklist = "";};
    string GetChecklist();
    void SimulateChklst();
private:
    string _checklist;
};
void Mobile::SimulateChklst()
{
    cout<<"---------话费清单(Mobile.Suzhou)---------"<<endl;
    _checklist = "市话话费:17.52\t\t长途话费:57.00\n短信:5.00(包月)\t\t彩铃:2.00(包月)\n";
    Notify();
}
string Mobile::GetChecklist()
{
    return _checklist;
}
//定义一个具体观察者:Jerry --找移动公司订阅(到移动大厅让移动服务人员订阅)
class Jerry:public Observer
{
public:
    void Received(Subject* sender);
};
void Jerry::Received(Subject* sender)
{
    cout<<"Jerry收到话费通知:"<<endl
        <<static_cast<Mobile*>(sender)->GetChecklist()
        <<endl;
}
//定义另一个具体观察者:Anco --由观察者自已订阅(上网自助订阅)
class Anco:public Observer
{
public:
    void Subscribe(Subject *subject);
    void Unsubscrible(Subject *subject);
    void Received(Subject* sender);
private:
    Subject _subject;
};
void Anco::Received(Subject* sender)
{
    cout<<"Anco收到话费通知:"<<endl
        <<static_cast<Mobile*>(sender)->GetChecklist()
        <<endl;
}
void Anco::Subscribe(Subject *subject)
{
    subject->Attach(this);
}
void Anco::Unsubscrible(Subject *subject)
{
    subject->Detach(this);
}
//------------Main函数------------------
int main()
{
    Mobile mobile;
    Jerry jerry;
    Anco anco;
    //订阅
    mobile.Attach(&jerry); //Subject添加Observer
    anco.Subscribe(&mobile); //Observer subscrible Subject;
     //本质就是向Subject维护的observers链表中加一条记录

    mobile.SimulateChklst();
    cout<<"\t[月底了...移动又该送话费清单啦:-)大家赶快看啊!]"<<endl;
    mobile.SimulateChklst();

    cout<<endl<<"\t[喏,Anco，取消订阅了...]"<<endl;
    anco.Unsubscrible(&mobile);
    mobile.SimulateChklst ();

    system("PAUSE");
    return 0;
}
```

C#为观察者模式提供的便利:

C#中的事件机制为实现观察者(Observer)提供了很好的支持，在C#中若一类提供了事件，则这个类就相当于发布了一个主题。

在C#中若在一个类中定义了一个事件，则等于定义了一个委托+两个方法，对应于上面的Subject类就是定义了ObserverList成员用来存用户列表，两个方法分别对应Attach()和Detach().

在C#中实现以上的观察者模式就要简单的多了，现给出代码：

```csharp
//Platform: WinXP + C# in vs2003
using System;
namespace Class1
{
    //-------------定义委托及事件传送的数据-------------
    internal class ChkLstEventArgs:EventArgs
    {
        private readonly string _checklist;
        public ChkLstEventArgs(string checklist)
        {
            _checklist = checklist;
        }
        public string Checklist
        {
            get{return _checklist;}
        }
    }
    internal delegate void PublishEventHandler(object sender, ChkLstEventArgs args);
   //--------------------定义抽象类---------------------
    internal class Subject
    {
        public event PublishEventHandler PublishChkLst;
        public void Notify(ChkLstEventArgs args)
        {
            if(PublishChkLst != null)
                PublishChkLst(this,args);
        }
    }
    internal abstract class Observer
    {
        public abstract void Received(object sender, ChkLstEventArgs args);
    }
    //------------------定义实体类----------------------
    class Mobile:Subject
    {
        public void SimulateChklst()
        {
            Console.WriteLine("---------话费清单(Mobile.Suzhou)---------");
            ChkLstEventArgs args = new ChkLstEventArgs("市话话费:17.52\t\t长途话费:57.00\n短信:5.00(包月)\t\t彩铃:2.00(包月)\n");
            base.Notify(args);
        }
    }
    class Jerry:Observer
    {
        public override void Received(object sender, ChkLstEventArgs args)
        {
            Console.WriteLine("Jerry收到话费通知:\n{0}",args.Checklist);
        }
    }
    class Anco:Observer
    {
        public void Subscribe(Subject sub)
        {
            sub.PublishChkLst += new PublishEventHandler(Received);
        }
        public void Unsubscrible(Subject sub)
        {
            sub.PublishChkLst -= new PublishEventHandler(Received);
        }
        public override void Received(object sender, ChkLstEventArgs args)
        {
            Console.WriteLine("Anco收到话费通知:\n{0}",args.Checklist);
        }
    }
    class ExcelProgram
    {
        [STAThread]
        static void Main(string[] args)
        {
            Mobile mobile = new Mobile();
            Jerry jerry = new Jerry();
            Anco anco = new Anco();

            //订阅
            mobile.PublishChkLst += new PublishEventHandler(jerry.Received); //Subject添加Observer
            anco.Subscribe(mobile); //Observer subscrible Subject;
                     //本质就是向Subject维护的observers链表中加一条记录

            mobile.SimulateChklst();
            Console.WriteLine("\t[月底了...移动又该送话费清单啦:-)大家赶快看啊]");
            mobile.SimulateChklst();
            Console.WriteLine("\t[喏,Anco，取消订阅了...]");
            anco.Unsubscrible(mobile);
            mobile.SimulateChklst ();

            Console.ReadLine();
        }
    }
}
```

观察者模式应用相当广泛，因为他非常好用。当你看MVC模式时，你可以看到观察者模式。当你用VB，DELPHI编程时，对类似按钮的事件的处理也可以看到观察者的影子。

引用GOF设计模式中的两段话作为总结：

> 定义对象间的一种一对多的依赖关系,当一个对象的状态发生改变时, 所有依赖于它的对象都得到通知并被自动更新。

> Observer模式描述了如何建立这种关系。这一模式中的关键对象是目标(Subject)和观察者(Observer)。一个目标可以有任意数目的依赖它的观察者。一旦目标的状态发生改变, 所有的观察者都得到通知。作为对这个通知的响应，每个观察者都将查询目标以使其状态与目标的状态同步。
