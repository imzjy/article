转型(Cast)可能破坏封装
=====

转型(Cast)可能破坏C++面向对象最根本的特征之一：封装(Encapsulation).特别是当我们使用了一个“蛮力”的转型时更是如此。下面我们通过一小段代码看看转型对封装的破坏。考虑以下面的这个类：

```c++
class hide
{
public:
    hide(int _n, string _msg):errNo(_n),msg(_msg)
    {}
private:
    int errNo;
    string msg;
};
```

类作者本意是想封装`errNo`和`msg`，这符合面向对象的思想，是个较好的主意。但若是通过一些"蛮力"的转型仍可以将`errNo`,`msg`水落石出。

为了让`errNO`,`msg`显形，我们定义以下类：

```c++
class visual
{
public:
    visual(int _n, string _msg):errNo(_n),msg(_msg)
    {}
public: //Only change access level

    int errNo;
    string msg;
};
```

在这个类中我们只做了小小的变动将`errNo`及`msg`的访问权限更改为`public`.破坏工具制做完成了，下面开始我们的破坏之旅，看以下代码：

```c++
//Platform: WinXP + VC6.0
#include <iostream>
#include <string>
using namespace std;

int main()
{
    hide h(100,string("hello Jerry"));

    visual *v1 = (visual*)&h;                    //C-style,蛮力转型
    visual *v2 = reinterpret_cast<visual*>(&h); //C++-style,蛮力转型
    //visual *v3 = static_cast<visual*>(&h); //C++-style,理性转型

    cout<<v1->errNo<<endl;
    cout<<v1->msg<<endl;
    v1->errNo = 222;
    cout<<v2->errNo<<endl;
    cout<<v2->msg<<endl;

    return 0;
}
```

运行结果让我们大吃一惊，精心封装的`errNo`及`msg`就这样被显示于众了。`hide`这个类名不符实呀!

上面的代码采用了三种转型(Cast)，分别是：C风格的转型，C++风格的`reinterpret_cast`和`static_cast`。前两种转型即是我所说的“蛮力”转型。他们可以成功将h对象所封装的部分显示于众。`static_cast`转型是一类较为理性的C++风格的转型，它拒绝没有继承关系的类之间的"蛮力"转型，如果我们将第三种转型的注释去掉，Compiling时将会出现以下错误信息：

`error C2440: 'static_cast' : cannot convert from 'class hide *' to 'class visual *'`

在这里我也再次推荐static_cast这种C++-style的转型，这种转型可以给你减少你在无意间使用了“蛮力”转型而带来的问题。
有没有方法可以防止这类转型呢？之所以"蛮力"转型会成功，主要是因为在C++中访问等级(Access Level)并不影响类对象在内存中的布局。我们可以采取一些小手来改变hide在内存上的布局来防止这种“蛮力”转型，例如我们可以在hide中加入一个无意义的virtual函数，这样使hide对象的内存布局和visual类对象的内存布局不一致，这样在做转型时就会出现系统错误。
不过上面的只是理论而已并不实用，最简单的方式还是程序员在写C++程序时尽量减少转型动作，在必须做转型时优先考虑那个"理性"的转型，而避免"蛮力"的转型。
