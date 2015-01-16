[C++]访问私有变量的怪现象
======

### 缘起：

最近在看Kent Beck的《测试驱动开发》，其中第4章有一个语言的语法问题让我很关注。这个问题说起来有些拗口：在[类的成员函数]中可以访问[同类型实例的私有变量]？

### 现象：

为了更好的说明问题，我将该问题用C++语言描述如下：

```c++
#include <iostream>
using namespace std;
class TestClass
{
public:
    TestClass(int amount)
    {
        this->_amount = amount;
    }
    void UsePrivateMember()
    {
        cout<<"amount:"<<this->_amount<<endl;
        
        /*----------------------*/
        TestClass objTc(10);
        objTc._amount = 15;   //访问同类型实例的私有变量
        cout<<objTc._amount<<endl; 
        /*----------------------*/
    }
private:
    int _amount;
};


int main()
{
    TestClass tc(5);
    tc.UsePrivateMember();
    return(0);
}
```

不知你看出问题来了没有？在类TestClass的UsePrivateMember()方法中我们创建了TestClass类型的一个实例objTc。

目前没有任何问题，问题出现在我们可以访问objTc的私有变量。在[对象]的外部可以访问该对象的私有变量，这不是破坏了面象对象的封装性吗？

确实此处破坏了对象的封装性。

### 解析：

之所以会出现这个问题是因为C++用来实现封装性的访问控制是编译器强加上的。此处问题是对`_amount`这个私有变量的名字解析出现了问题，“骗”过了编译器。

我们来看看`_amount`的名字(symbol)是怎么被解析的：

1. 决定名字查找的域；
    
    当编译器发现`_amount`变量时，它会在objTc对象的类域(class scope)中寻找该名字。

2. 决定当前域中哪些名字可以访问；

    由第1步可知，当前查找的域是类域。而`objTc`对象`TestClass`类体中，所以`TestClass`中的所有变量均可见(accessible)。也就是说无论是private,`protected`还是`public`均可可见，此时_amount被找到；

3. 名字已查找到，编译通过；

     访问`_amount`是编译器强加的，既然已通过编译，自然可以访问到`_amount`变量的值。

从直觉上讲，我们会以为objTc会在其[对象域(object scope)]（这是我自己杜撰的一个名词，与类域相对）中查找该名字。而C++编译器的实现(implement)却是在`objTc`对象的类域(class scope)中查找该名字。

----

参考：
  
1，《C++ Primer 3/e》  第13.9节 类域




