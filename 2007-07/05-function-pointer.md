C/C++中指向函数的指针
======

近来有些事老是扰着我，总觉得有些不舒服，书也少看了许多。Why？谁知道呢。昨晚和朋友去喝酒聊天，今天精神倍好。坐在厂车上忽然想起：在C++中怎么定义使用指向函数的指针？正好刚才学了一下，做个整理。纵然有很多事，但不能忘记该做的事，将学习进行到底。

“在C语言中，函数本身不是变量，但可以定义指向函数的指针，这种指针可以被赋值、存放于数组之中，传递给函数及作为函数的返回值等”　－－《The C Programming Language Second Edition》

我们写一个函数测试一下：

```c++
//Platform:VC6+winXP

#include <stdio.h>
int (*myFun)(int a, int b);          //定义一个函数指针
int addi(int a,int b)
{
 return a+b;
}
int main()
{
 printf("myFun = 0x%X\n",myFun);
 printf("addi  = 0x%X\n\n",addi);
 myFun = addi;                      //函数指针指向addi的入口地址
 printf("&myFun = 0x%X\n",&myFun);
 printf("myFun  = 0x%X\n\n",myFun);
 printf("*myFun = 0x%X\n",*myFun);

 printf("myFun(20,30) = %d\n",myFun(20,30));
}
```

```text
Output:
myFun = 0x0
addi  = 0x401005

&myFun = 0x42D3F0
myFun  = 0x401005

*myFun = 0x401005
myFun(20,30) = 50
```

在定义一个指向函数的指针后，可以给该函数指针赋值：`myFun = addi`;

使myFun指针的内容（即指向）`addi`的入口地址。但这种赋值有一点注意，下面有段话来处C++之父：

> Pointers to functions have argument types declared just like the functions themselves. In pointer assignments, the complete function type must match exactly.
  --《The C++ Programming Language Third Edition》

即这种已定义好的函数指针只能指向一个与其申明(返回类型，参数类型及数目)严格一致的函数。在本例中，`myFun`只能指向一个返回值为`int`型，有两个`int`型参数的函数，而并不在意函数的实现部分如何。`myFun`与`addi`的申明部分必须严格匹配。

```c++
//Platform:VC6+winXP

#include <stdio.h>
int  (*myFun)(int a, int b);          //定义一个函数指针
void (*myFun2)(int a,int b);
int  (*myFun3)(double a,int b)

int addi(int a,int b)
{
  return a+b;
}
int subi(int m,int n)
{
  return m-n;
}

int main()
{
  myFun = addi;   //OK
  myFun = subi;   //OK

  myFun1 = addi;  //Error,return type doesn't match
  myFun2 = addi;  //Error,argument type doesn't match
}
```

Error Message:

```text
error C2440: '=' : cannot convert from 'int (__cdecl *)(double,int)' to 'int (__cdecl *)(int,int)'
```

经过思考画出了函数指针在内存中的表示，借一幅图来表达：

![](http://blog.chinaunix.net/photo/11680_070705100602.gif)

从图中可以看出，myFun指针指向的是addi的入口地址。这样不难得出以下结论：

```text
(*myFun) == 0x401005    //取myFun的值
myFun  == 0x401005    //取其值（右值）
&myFun  == 0x42D3F0    //取myFun的地址。
```

所以在用函数指针调用函数时

```text
(*myFun)(20,30);
myFun(20,30);
```

实际上都是通过addi入口点地址调用addi函数；
