协变和逆变-Covariance and Contravariance
========

在C#4.0新特性介绍中，总是免不了对协变和逆变的介绍。但似乎协变逆变又很鸡肋。我试图简单地讲下协变（Covariance）和逆变(Contravariance)。

1. Co&Contravariance并非C#4.0引入的，早在C#1.0中就有了。只是C#4.0加入了对Generic Type的Co&Contravariance的支持。
2. Co&Contravariance是`静态语言`用来支持(安全的隐式)`类型转换`的技术。
3. Co&Contravariance都满足Liskov原则：子类可以替换基类(在需要较少信息的基类时候，可以提供较多信息的子类来替代)。
4. 只支持引用类型，值类型则不支持。

### Covariance

对Caller来说，需要返回一个基类。对Callee来说，实际返回了一个子类。看如下代码片段：

```csharp
class Base{}
class Sub:Base{};
static Base SomeMethod()
{
    return new Sub();    //Sub casting up to Base.
}
```

Caller: Access Sub via Base

Callee: Return Sub for Base

从Callee的视角来看：子类安全地向上Casting——提供了更多信息.

### Contravariance

对Callee来说，需要传入一个基类。对Caller来说实际传入一个子类。代码如下：

```csharp
class Base{}
class Sub:Base{};
static void SomeMethod(Base b)
{
    Sub sb = (Sub)b;   //Base casting down to Sub
}
static void Main(string[] args)
{
    SomeMethod(new Sub());
}
```

Callee:Access Sub via Base

Caller:Pass Sub for Base

从Callee的角度来看：基类向下Casting——可以提供更多信息.

 
----

参考：

http://en.wikipedia.org/wiki/Covariance_and_contravariance_(computer_science)

http://www.cnblogs.com/fox23/archive/2009/12/03/covariance-contravariance-in-csharp-4.html

http://www.cnblogs.com/Ninputer/archive/2008/11/22/generic_covariant.html
