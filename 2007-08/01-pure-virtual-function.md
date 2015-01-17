C++中的纯虚函数
========

在C++中的一种函数申明被称之为：纯虚函数(pure virtual function).它的申明格式如下：

```c++
class CShape
{
public:
    virtual void Show()=0;
};
```

注意Show函数后面，在普通的虚函数后面加上"=0"这样就声明了一个pure virtual function.

在什么情况下使用纯虚函数(pure vitrual function)?

1. 当想在基类中抽象出一个方法，且该基类只做能被继承，而不能被实例化；
1. 这个方法必须在派生类(derived class)中被实现；

如果满足以上两点，可以考虑将该方法申明为pure virtual function.

我们来举个例子，我们先定义一个形状的类(Cshape)，但凡是形状我们都要求其能显示自己。所以我们定义了一个类如下：

```c++
class CShape
{
    virtual void Show(){};
};
```

但没有CShape这种形状，因此我们不想让CShape这个类被实例化，我们首先想到的是将Show函数的定义（实现）部分删除如下：

```c++
class CShape
{
    virtual void Show();
};
```

当我们使用下面的语句实例化一个CShape时：

```c++
CShape cs;  //这是我们不允许的，但仅用上面的代码是可以通过编译（但link时失败）。
```

怎么样避免一个CShape被实例化，且在编译时就被发现？答案是：使用pure virtual funcion.

我们再次修改CShape类如下：

```c++
class CShape
{
public:
    virtual void Show()=0;
};
```

这时在实例化CShape时就会有以下报错信息：

```text
error C2259: 'CShape' : cannot instantiate abstract class due to following members:
warning C4259: 'void __thiscall CShape::Show(void)' : pure virtual function was not defined
```

我们再来看看被继承的情况,我们需要一个CPoint2D的类，它继承自CShape.他必须实现基类(CShape)中的Show()方法。

其实使用最初的本意是让每一个派生自CShape的类，都要实现Show()方法，但时常我们可能在一个派生类中忘记了实现Show(),为了避免这种情况，pure virtual funcion发挥作用了。

我们看以下代码：

```c++
class CPoint2D:public CShape
{
public:
 CPoint2D()
 {
  printf("CPoint2D ctor is invoked\n");
 };
 void Msg()
 {
  printf("CPoint2D.Msg() is invoked\n");
 };
 /*---I'm sorry to forget implement the Show()---
 void Show()
 {
  printf("Show() from CPoint2D\n");
 };
------------------------------------------------*/
};
```

当我们实例化CPoint2D时，在编译时(at the compiling)也会出现如下的报错:

```text
error C2259: 'CShape' : cannot instantiate abstract class due to following members:
warning C4259: 'void __thiscall CShape::Show(void)' : pure virtual function was not defined
```
如上，我们预防了在派生类中忘记实现基类方法。也许compiler会说：

> 哼！如果不在派生类的中实现在Show方法，我编译都不会让你通过。

```c++
//--------------------------------------------------------
//now,show the completed code,
//Platform:Winxp+VC6.0
//--------------
#include <iostream>
#include <stdio.h>
using namespace std;
class CShape
{
public:
 virtual void Show()=0;
};
class CPoint2D:public CShape
{
public:
 void Msg()
 {
  printf("CPoint2D.Msg() is invoked\n");
 };
/*---I'm sorry to forget implementation of the Show()--- */
 void Show()
 {
  printf("Show() from CPoint2D\n");
 };
/*------------------------------------------------------*/
};
void main()
{
 CPoint2D p2d;   //如果派生类(CPoint2D)没有实现Show()，则编译不通过
 p2d.Msg();
 //
 CShape *pShape = &p2d;
 pShape->Show();
 //不能实例化基类
 //CShape cs;
}
```
