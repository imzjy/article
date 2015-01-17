设计模式之原型模式(Prototype)
======

原本在《设计模式--可复用面向对象团软件基础》(简称《设计模式》)书中介绍这个模式的时候选的例子太过复杂.倒不是因为GOF选材不好.而是本来这个模式就复杂,想要将该模式很好的应用的话,需要考虑的也较多.但这对模式的初学者并不好,往往是看着看着就迷茫了.而忘记的该模式本身想表达的意思.

我倒想以个简单的方式来说明这个模式,分享一下经验.希望可以抛砖引玉,让更多的朋友可以亲近,或是不再害怕模式.

### 1,概述.

在《设计模式》中有几个原则:

- 尽量采用组合,而不是继承.这是为什么?
  解耦合(Decoupling).
- 那又为什么要解耦合呢?
  方便复用(Reusable).

这便符合《设计模式》本书想带给大家的收获--创建可复用的软件. 原型(Prototype)这个模式给我们带来两个优势:

1. 是尽量采用组合;
1. 可以尽可能减少定义类的数量(注:多做多错,杨老师的口头禅,呵呵.)

如果一个类`A`仅依赖另一个类`B`,那么可以考虑使用原型(Prototype)模式.是不是说的有些迷糊,我们看一看实例.

### 2,举例说明.

我们拿做汉堡(Hamburger,也就是类似KFC的那种)为例.要做汉堡我们需要配料(Material)再加上两片面包.根据配料不同我们可以做出不同的汉堡,比如牛肉汉堡,蔬菜汉堡等等.

经过一段时间的思考,我们可能这样定义出表示配料(Material)的类,以及表示汉堡的类(Hamburger).类图如下:

![](http://blog.chinaunix.net/photo/11680_080128152638.gif)

从上图可以看出,当前我们定义了四个具体类(Concrete class).他们分别表示两个配料的类,和两种汉堡的类. 也许看看代码,更容易理解一些.现给出第一次设计的完整代码.

```c++
//Platform: WinXp + VC6.0
#include <iostream.h>
#include <stdio.h>
/*-----------------表示配料的类-----------------------*/
class Material
{
protected:
    char *materialName;
public:
    virtual void Feed() = 0;
    char *MaterialName()
    {
        return materialName;
    }
};
class Vegetable:public Material
{
public:
    virtual void Feed()
    {
        Clean();
        cout<<"Added the vegetable..."<<endl;
        materialName = "Vegetable";
    }
    void Clean() //清洗蔬菜
    {
        cout<<"Cleaning the vegetable. "<<endl;
    }

};
class Beef:public Material
{
public:
    virtual void Feed()
    {
        Roast();
        cout<<"Added the beef..."<<endl;
        materialName = "Beef";
    }
    void Roast() //牛肉是需要烤一下

    {
        cout<<"Roasting the beef."<<endl;
    }
};
/*-----------------表示汉堡的类-----------------------*/
class Hamburger
{
public:
    virtual void MakeHamburger() = 0;
};

class BeefHam:public Hamburger
{
private:
    Beef _beef;
public:
    virtual void MakeHamburger()
    {
        _beef.Feed(); //添加配料

        cout<<_beef.MaterialName()<<"汉堡已经做好，请慢用."<<endl;
    }
};
class VegeHam:public Hamburger
{
private:
    Vegetable _vegetable;
public:
    virtual void MakeHamburger()
    {
        _vegetable.Feed(); //添加配料

        cout<<_vegetable.MaterialName()<<"汉堡已经做好，请慢用."<<endl;
    }
};


void main()
{
    cout<<"开始制作牛肉汉堡."<<endl;
    BeefHam beefHam;
    beefHam.MakeHamburger();

    cout<<endl;
    cout<<"开始制作蔬菜汉堡."<<endl;
    VegeHam vegeHam;
    vegeHam.MakeHamburger();
}
```

输出结果如下:

```text
开始制作牛肉汉堡.
Roasting the beef.
Added the beef...
Beef汉堡已经做好，请慢用.

开始制作蔬菜汉堡.
Cleaning the vegetable.
Added the vegetable...
Vegetable汉堡已经做好，请慢用.
```

这样设计的话,我们的复用性并不好.从UML图中我们可以看出.我们从`Hamburger`派生出的类依赖于`Material`的派生类即:`Vegetable`和`Beef`类.

如果这时我们需要再做另外一种鸡肉汉堡的话,我们必须添加两个类,其中一个类继承于`Material`,再一个继承于`Hamburger`.即添加以下代码:

```c++
//派生自Material
class Chicken:public Material
{
public:
    virtual void Feed()
    {
        HandleChicken();
        cout<<"Added the beef..."<<endl;
        materialName = "Chicken";
    }
    void HandleChicken() //处理鸡肉
    {
        cout<<"Roasting the beef."<<endl;
    }
};
//派生自Hamburger
class ChickenHam:public Hamburger
{
private:
    Chicken _chicken;
public:
    virtual void MakeHamburger()
    {
        _chicken.Feed(); //添加配料
        cout<<_chicken.MaterialName()<<"汉堡已经做好，请慢用."<<endl;
    }
};
```

之所以需要如此,是因为`ChickenHam`这个类,紧紧依赖于`Material`的派生类`Chicken`.这反映在类图上就是被标为黄色的两个派生类:

![](http://blog.chinaunix.net/photo/11680_080128155855.gif)

也许这时大家发现了些端倪,类乎派生自Hamburger的类,除了各自拥有的配料(beef,chicken,vegetable)不一样以外,其它的并没有什么不同.冒似可以自动化生成`Hamburger`的派生类.

如果你已想到这一步了,那离原型模式也就不远了.我们先给出原型模式的UML图示,让朋友们自己对号入座.并看看这带来优势--类似于自动生成一个具体(Concrete)的`Hamburger`类.这是一件美妙的事.

![](http://blog.chinaunix.net/photo/11680_080128161448.gif)

看一看,这个Prototype的图示.我们可以将配料类看做一个原型(Prototype),我们也为该原型定义一个virtual方法.让其可以Clone出一个具体的配料类.

这会带来一个好处:我们在Client位置,即Hamburger类,只需参数化传递需要Clone的配料类即可,而不必我们每次都派生出一个具体化(Concrete)的`Hamburger`类.看起来类图是这样(注意,我将`Material`和`Hamburger`类位置左右调换了一下)

![](http://blog.chinaunix.net/photo/11680_080128163124.gif)

从图上可以看出,我们新增的Chicken类并没有新增一个相应的Hamburger类,而是定义了一个纯虚函数Clone,让其返回原型类(些处指Vegetable,Chicken或Beef)的引用.通过这些引用,我们可以不用派生Hamburger而直接是在Hamburger的方法中引用(或者说是参考)原型对象(Prototype Object).

现在给出经过重新设计后,采用Prototype模式的完整Source.

```c++
//Platform: WinXp + VC6.0
#include <iostream.h>
class Material
{
protected:
    char *materialName;
public:
    virtual Material* Clone() = 0;
    virtual void Feed() = 0;
    char *MaterialName()
    {
        return materialName;
    }
};
class Vegetable:public Material
{
public:
    virtual Material* Clone()
    {
        return this;
    }
    virtual void Feed()
    {
        cout<<"Added the vegetable..."<<endl;
        materialName = "Vegetable";
    }
};
class Beef:public Material
{
public:
    virtual Material* Clone()
    {
        return this;
    }
    virtual void Feed()
    {
        cout<<"Added the beef..."<<endl;
        materialName = "Beef";
    }
};

/*--------此处新增一个Material派生类即可----------*/
class Chicken:public Material
{
public:
    virtual Material* Clone()
    {
        return this;
    }
    virtual void Feed()
    {
        HandleChicken();
        cout<<"Added the beef..."<<endl;
        materialName = "Chicken";
    }
    void HandleChicken() //处理鸡肉

    {
        cout<<"Roasting the beef."<<endl;
    }
};

class Hamburger
{
private:
    Material *_pMaterial;   //优先采用组合,而不是继承
public:
    Hamburger(Material *pMaterial):_pMaterial(pMaterial)
    {}
    void MakeHamburger();
};
void Hamburger::MakeHamburger()
{
    //注意此处clone可以是深拷贝(deep copy)
    Material *pPrototype = _pMaterial->Clone();
    pPrototype->Feed();
    cout<<pPrototype->MaterialName()<<"汉堡已经做好，请慢用."<<endl;
}

void main()
{
    //创建汉堡配料
    Beef beef;
    Vegetable vegetable;


    cout<<"开始制作牛肉汉堡."<<endl;
    Hamburger beefHam(&beef);
    beefHam.MakeHamburger();

    cout<<endl;
    cout<<"开始制作蔬菜汉堡."<<endl;
    Hamburger vegeHam(&vegetable);
    vegeHam.MakeHamburger();

    cout<<endl;
    cout<<"开始制作鸡肉汉堡."<<endl;
    /*新增一个配料，然后当做参数传递即可*/
    Chicken chicken;
    Hamburger chickenHam(&chicken);
    chickenHam.MakeHamburger();

}
```

### 3,总结.

Protetype模式,本身似乎可以看做一个类型生成器(Class Generator).但又跟工厂方法(Factory Method)有些区别,工厂方法所产生的类,是我们已经在代码里显示定义过了的.而Prototype模式模似了(Simulate)了一组相关的派生类.

原理简单但要是实施起来还是有很多地方需要细细考虑,单从原型类(Prototype class)的派生类(即,Concrete Prototype class)怎么样实现Clone这个方法来讲就非常的复杂.因为你不得不考虑"深拷贝"和"浅拷贝"(Shallow copy and deep copy)的情况.

模式本身并不难,想要实现的目的也很明显.但在实际的项目中应用模式,用好模式.那还是相当有难度的.当你有一堆较烂的设计,你可以尝试通过重构(Refactoring),真至找到很好的解决方案.这些解决方案中,肯定会有模式的身影,不信你试试...

