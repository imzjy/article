[转]函数调用方式的区别: thiscall, __cdecl, __stdcall
===================

前几天在CSDN看到yc_8301写的一篇介绍VC中的几种函数调用方法区别的文章，一下子释放了我的好奇心。先前也听说过诸如__cdecl和__stdcall的区别，但也只是泛泛地介绍一下前一种调用(__cdecl)由主调函数负责参数压栈，同时主调函数负责栈(Stack)的恢复。后一种调用(__stdcall)由主调函数负责参数压栈，由函数本身负责栈的恢复。但终究觉得不过隐，觉得__cdecl和__stdcall仍然有些"犹报琵琶半遮面"，经YC_8301的一提醒，顿时开朗，在此表示感谢!

本文转自: http://blog.csdn.net/yc_8301/archive/2007/10/08/1814744.aspx

预知更清楚的表述，请朋友们至原文作者Blog: http://blog.csdn.net/yc_8301/

详查。本文对于原文做了些"篡改"，请原作者多多包涵。此外本文示例所用的平台：WinXP + VC6.0

----

通常在使用VC进行函数定义时会指定该函数调用方式，诸如：

```c++
int __stdcall max(int a, int b)
{
 return a>b?a:b;
}
int __cdecl min(int a, int b)
{
  return a<b?a:b;
}
bool __fastcall equal(int a, int b)
{
  return a=b?true:false;
}
```

首先，让我们来分个类，调用方法分为两大类另加一个较特殊的`__thiscall`.

1. `__stdcall`，别名：WINAPI,CALLBACK,PASCAL。该类特点是:主调函数负责参数入栈，由函数本身负责栈的恢复.
2. `__cdecl`，别名：C/C++中默认调用方式，若你定义函数未指定函数调用约定(Calling Conventions),例如在VC6中下面两个函数的调用约定是等价的：

```c++
int max(int a, int b)
{
  return a>b?a:b;
}
int __cdecl min(int a, int b)
{
  return a<b?a:b;
}
```

该类调用约定的特点是：**由主调函数负责参数入栈，并由主调函数负责线的恢复**.

``__thiscall``比较特殊，只用于类成员函数调用，你甚至不能强制指定这个函数调用约定。它是由C/C++编译器自动添加的。在C/C++中类成员函数会默认传入一个this指针，对于此，在默入情况下，C/C++中类成员函数通过此类调用约定来指定this指针.

接着介绍一下`__thiscall`，`__thiscall`是关于类的一种调用方式.它与其他调用方式的最大区别是：

> `__thiscall`对每个函数都增加了一个类指针参数

```text
class   aa
{
  void   bb(int   cc);
};
```

实际上`bb`的函数原形是`void bb(aa &this, int cc)`;

`__cdecl`的调用方式介绍, 即C和C++缺省调用方式

例子：

```c++
void   Input(   int   &m,int   &n);
/*相当于void   __cdecl   Input(int   &m,int   &n);*/
```

以下是相应的汇编代码:

```text
00401068 lea eax,[ebp-8]    ;取[ebp-8]地址(ebp-8),存到eax
0040106B push eax           ;然后压栈
0040106C lea ecx,[ebp-4]    ;取[ebp-4]地址(ebp-4),存到ecx
0040106F push ecx           ;然后压栈
00401070 call @ILT+5(Input) (0040100a)    ;然后调用Input函数
00401075 add esp,8          ;恢复栈
```

从以上调用`Input`函数的过程可以看出：在调用此函数之前，首先压栈`ebp-8`,然后压栈`ebp-4`,然后调用函数`Input`,最后`Input`函数调用结束后，利用`esp+8`恢复栈。由此可见，在C语言调用中默认的函数修饰`_cdecl`，由主调用函数进行参数压栈并且恢复堆栈。

下面看一下：地址`ebp-8`和`ebp-4`是什么？ 在VC中点击`VIEW->debug  windows->Registers`, 显示寄存器变量值，然后选`debug  windows->Memory`,输入`ebp-8`的值和`ebp-4`的值(或直接输入`ebp-8`和`-4`)，看一下这两个地址实际存储的是什么值，实际上是变量`n`的地址(ebp-8),`m`的地址(ebp-4).

由此可以看出：在主调用函数中进行实参的压栈并且顺序是从右到左。另外，由于实参是相应的变量的引用，也证明实际上引用传递的是变量的地址(类似指针)。

**总结**：在C或C++语言调用中默认的函数修饰`_cdecl`，由主调用函数进行参数压栈并且恢复堆栈，实参的压栈顺序是从右到左，最后由主调函数进行堆栈恢复。由于主调用函数管理堆栈，所以可以实现变参函数。另外，命名修饰方法是在函数前加一个下划线`_`.

`_stdcall` 调用约定介绍, 实际上就是PASCAL，CALLBACK,WINAPI

例子：

```c++
void WINAPI Input( int &m,int &n);
```

看一下相应调用的汇编代码：

```text
00401068 lea eax,[ebp-8]
0040106B push eax
0040106C lea ecx,[ebp-4]
0040106F push ecx
00401070 call @ILT+5(Input) (0040100a)
```

从以上调用`Input`函数的过程可以看出：在调用此函数之前，首先压栈`ebp-8`,然后压栈`ebp-4`,然后调用函数`Input`,在调用函数`Input`之后，没有相应的堆栈恢复工作(为其它的函数调用，所以我没有列出)下面再列出`Input`函数本身的汇编代码：(实际此函数不大，但做汇编例子还是大了些，大家可以只看前和后，中间代码与此例子无关)

```text
39:   void   WINAPI   Input(   int   &m,int   &n)
40:   {
00401110   push   ebp
00401111   mov   ebp,esp
00401113   sub   esp,48h
00401116   push   ebx
00401117   push   esi
00401118   push   edi
00401119   lea   edi,[ebp-48h]
0040111C   mov   ecx,12h
00401121   mov   eax,0CCCCCCCCh
00401126   rep   stos   dword   ptr   [edi]
41:   int   s,i;
42:
43:   while(1)
00401128   mov   eax,1
0040112D   test   eax,eax
0040112F   je   Input+0C1h   (004011d1)
44:   {
45:   printf("\nPlease   input   the   first   number   m:");
00401135   push   offset   string   "\nPlease   input   the   first   number   m"...   (004260b8)
0040113A   call   printf   (00401530)
0040113F   add   esp,4
46:   scanf("%d",&m);
00401142   mov   ecx,dword   ptr   [ebp+8]
00401145   push   ecx
00401146   push   offset   string   "%d"   (004260b4)
0040114B   call   scanf   (004015f0)
00401150   add   esp,8
47:
48:   if   (   m=   s   )
004011B3   mov   eax,dword   ptr   [ebp+8]
004011B6   mov   ecx,dword   ptr   [eax]
004011B8   cmp   ecx,dword   ptr   [ebp-4]
004011BB   jl   Input+0AFh   (004011bf)
57:   break;
004011BD   jmp   Input+0C1h   (004011d1)
58:   else
59:   printf("   m   <   n*(n+1)/2,Please   input   again!\n");
004011BF   push   offset   string   "   m   <   n*(n+1)/2,Please   input   agai"...   (00426060)
004011C4   call   printf   (00401530)
004011C9   add   esp,4
60:   }
004011CC   jmp   Input+18h   (00401128)
61:
62:   }
004011D1   pop   edi
004011D2   pop   esi
004011D3   pop   ebx
004011D4   add   esp,48h
004011D7   cmp   ebp,esp
004011D9   call   __chkesp   (004015b0)
004011DE   mov   esp,ebp
004011E0   pop   ebp
004011E1   ret   8
```

之后，我们看到在函数末尾部分，有`ret   8`，明显是恢复堆栈，由于在32位C++中，变量地址为4个字节(`int`也为4个字节)，所以弹栈两个地址即8个字节。由此可以看出：在主调用函数中负责压栈，在被调用函数中负责恢复堆栈。因此不能实现变参函数，因为被调函数不能事先知道弹栈数量，但在主调函数中是可以做到的，因为参数数量由主调函数确定。

下面再看一下，`ebp-8`和`ebp-4`这两个地址实际存储的是什么值，`ebp-8`地址存储的是`n`的值，`ebp-4`存储的是`m`的值。说明也是从右到左压栈,进行参数传递。

总结：`_stdcall`在主调用函数中负责压栈，在被调用函数中负责弹出堆栈中的参数，并且负责恢复堆栈。因此不能实现变参函数，参数传递是从右到左。另外，命名修饰方法是在函数前加一个下划线`_`，在函数名后有符号`@`，在`@`后面紧跟参数列表中的参数所占字节数(10进制)，如：`void Input(int &m,int &n)`,被修饰成：`_Input@8` 对于大多数api函数以及窗口消息处理函数皆用CALLBACK,所以调用前，主调函数会先压栈，然后api函数自己恢复堆栈。

如：

```text
push   edx
push   edi
push   eax
push   ebx
call   getdlgitemtexta
```

最后，在SDK中输出API函数的时候，经常会利用WINAPI对函数进行约定，WINAPI在WIN32中，它被定义为`__stdcall`函数调用约定有多种，这里简单说一下：

1. `__stdcall`调用约定相当于16位动态库中经常使用的PASCAL调用约定。在32位的VC++5.0中PASCAL调用约定不再被支持（实际上它已被定义为`__stdcall`。除了`__pascal` 外，`__fortran`和`__syscall`也不被支持），取而代之的是`__stdcall`调用约定。两者实质上是一致的，即函数的参数自右向左通过栈传递，被调用的函数在返回前清理传送参数的内存栈，但不同的是函数名的修饰部分（关于函数名的修饰部分在后面将详细说明）。`__stdcall`是Pascal程序的缺省调用方式，通常用于Win32 Api中，函数采用从右到左的 压栈方式，自己在退出时清空堆栈。VC将函数编译后会在函数名前面加上下划线前缀，在函数名后加上`@`和参数的字节数。
2. C调用约定（即用`__cdecl`关键字说明）按从右至左的顺序压参数入栈，由调用者把参数弹出栈。对于传送参数的内存栈是由调用者来维护的（正因为如此，实现可变参数的函数只能使用该调用约定）。另外，在函数名修饰约定方面也有所不同。`__cdecl`是C和C＋＋程序的缺省调用方式。每一个调用它的函数都包含清空堆栈的代码，所以产生的可执行文件大小会比调用`_stdcall`函数的大。函数采用从右到左的压栈方式。VC将函数编译后会在函数名前面加上下划线前缀。是MFC缺省调用约定。
3. `__fastcall`调用约定是“人”如其名，它的主要特点就是快，因为它是通过寄存器来传送参数的（实际上，它用`ECX`和`EDX`传送前两个双字（DWORD）或更小的参数，剩下的参数仍旧自右向左压栈传送，被调用的函数在返回前清理传送参数的内存栈），在函数名修饰约定方面，它和前两者均不同。`__fastcall`方式的函数采用寄存器传递参数，VC将函数编译后会在函数名前面加上`@`前缀，在函数名后加上`@`和参数的字节数。
4. `thiscall`仅仅应用于“C++”成员函数。`this`指针存放于`CX`寄存器，参数从右到左压。`thiscall`不是关键词，因此不能被程序员指定。
5. `naked call`采用1-4的调用约定时，如果必要的话，进入函数时编译器会产生代码来保存`ESI`，`EDI`，`EBX`，`EBP`寄存器，退出函数时则产生代码恢复这些寄存器的内容。`naked call`不产生这样的代码。`naked call`不是类型修饰符，故必须和`_declspec`共同使用。
