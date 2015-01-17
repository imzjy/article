C++中成员初始化列表的使用
=====

C++在类的构造函数中，可以两种方式初始化成员数据(data member)。

**1,在构造函数的实现中，初始类的成员数据。诸如：**

```c++
class point
{
private:
 int x,y;
public:
 point(int m=0,int n=0)
 {
  x=m;
  y=n;
 }
 int GetX()
 {
  return x;
 }
 int GetY()
 {
  return y;
 }
};
```

**2,还可以定义初始化成员列表（Initializer list）来初始化成员数据(data member)。**

改写构造函数如下：

```c++
point(int m=0,int n=0):x(m),y(n)
{
}
```
这样咋一看没有什么不同，确实，对于上面的这种简单列子来说，也真的没有太大不同。

那我们为什么要用初始化成员列表，什么时候用初始化成员列表来初始化成员数据呢？Lippman的《C++ Primer》中提到在以下三种情况下需要使用初始化成员列表：

1. 需要初始化的数据成员是对象的情况；
1. 需要初始化const修饰的类成员；
1. 需要初始化引用成员数据；

现在分别举例说明：

### 一，需要初始化的数据成员是对象。

```c++
#include <stdio.h>
class point
{
protected:
 int m_x,m_y;
public:
 point(int m=0,int n=0)
 {
  m_x = m;
  m_y = n;
  printf("constructor called!\n");
 }
 point(point& p)
 {
  m_x = p.GetX();
  m_y = p.GetY();
  printf("copy constructor called!\n");
 }
 int GetX()
 {
  return m_x;
 }
 int GetY()
 {
  return m_y;
 }
};

class point3d
{
private:
 point m_p;
 int m_z;
public:
 point3d(point p, int k)
 {
  m_p = p;                              //这里是对m_p的赋值
  m_z=k;
 }
 point3d(int i,int j, int k):m_p(i,j)   // 相当于 point m_p(i,j)这样对m_p初始化
 {
  m_z=k;
 }
 void Print()
 {
  printf("%d,%d,%d \n",m_p.GetX(),m_p.GetY(),m_z);
 }
};
```

上述代码中Point3d是一个3D坐标，他有一个point的2D坐标和一个成员组成。

我们现在想定义一个3D坐标p3d，可以这样实现：

```c++
void main()
{
 point p(1,2);    //先定义一个2D坐标
 point3d p3d(p,3);
 p3d.Print();
}
```

从point3d实现体可以看出，我们是通过对m_p进行赋值，这样不仅调用copy constructor产生临时对象而且是对m_p的一个赋值操作。

而如果使用成员初始化列表，我们则可以这样：

```c++
void main()
{
 point p(1,2);
 point3d p3d(1,2,3);
 p3d.Print();
}
```

`p3d`中的`point`型成员是通过调用初始化的方式构建的。由于对象赋值比初始化要麻烦的多，因此也带来的性能上的消耗。（可以参见Scott Meyers著《effective C++》条款12）。
这也是我们在对成员数据是对象成员的采用初始化列表进行初始始化的主要原因。

### 二，需要初始化const修饰的类成员；

### 三，需要初始化引用成员数据；

对于类成员是`const`修饰，或是引用类型的情况，是不允许赋值操作的，(显然嘛，`const`就是防止被错误赋值的，引用类型必须定义赋值在一起)因此只能用初始化列表对齐进行初始化。

上面两点比较好明白，可以用一个例子加以说明：

```c++
#include <stdio.h>
class base
{
private:
 const int a;
 int& b;
public:
// base(int m, int n)
// {
//  a = m;
//  b = n;
// }
 base(int m, int n):a(m),b(n)
 {}
};

void main()
{
 base ba(1,2);
}
```

上面红色的部分初始化的方式是不允许的通不过编译,通过初始化列表则可以很好的定义。
