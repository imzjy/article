C++中对象对内存的使用
=======

今天早上打开Blog奇怪了，六一写的blog怎么不见了，一开始我还以为是忘记保存了，后来去CU上一看知道知道原来是CU的Blog所在服务器出现了故障.好在的是非常负责的CU的管理员们及时恢复了大部分文章，随便key几个关键字，就找到了六一写的那篇blog，并将其导入至我的Blog.再一次感谢CU的管理员，千言万语，抵不上一次行动，你们的表现让CUer们很是放心。

最近看了一本IBM中国研究院的《C++性能优化》，感觉里的内容很是通俗，里面有掺杂很多实例，通过实例可以很好的了解作者想要说明的内容。什么叫好书？个人觉得能看的懂的书便是好书。至少是适合你的书。里面有对C++对象对内存的使用进行了详尽的说明，现在我将其整整好，给还不知道的朋友分享一下，让自己温故而知新。

我们知道，`程序=代码+数据`。若按照这个等式，一个C++程序在内存的中分配方式如下：

1. 全局/静态变量存储区；[数据]
2. 常存储区；[数据]
3. 代码区；[代码]
4. 栈；[数据]
5. 堆；[数据]

我们写一小段代码测试一下；

```c++
Platform:winXp + vc6.0
----------------------------------------------------------
#include <stdio.h>
#include <malloc.h>
int iGlobal;
void main()
{
 	static int iStatic;

	char cChar = 'A';
	int b = 6;
	int iLocal;
	int *p = new int[5];
	char *c = (char*)malloc(1);

	printf("iGloba  address: 0x%x\n",&iGlobal);
	printf("iStatic address: 0x%x\n",&iStatic);
	printf("\n");
	printf("a       address: 0x%x\n",&cChar);
	printf("cChar   address: 0x%x\n",&b);
	printf("iLocal  address: 0x%x\n",&iLocal);
	printf("p self  address: 0x%x\n",&p);
	printf("\n");
	printf("p point address: 0x%x\n",p);
	printf("c       address: 0x%x\n",&(*c));
}
```

output:

```text
iGloba  address: 0x42359c
iStatic address: 0x4235a0

a       address: 0x12ff7c
cChar   address: 0x12ff78
iLocal  address: 0x12ff74
p self  address: 0x12ff70

p point address: 0x431ed0
c       address: 0x431ea0
```

从上面的输出可以看出：

- 全局/静态变量,存储在一个区域0x42659c地址；
- 局部变量及局部常量,存储在一个区域0x12ff70，该区域属于线程栈；（以4字节对齐）.
- 动态创建的空间,p数组,c字符都在一个区域0x431ea0,该区域属于进程堆;(以16字节对齐).

从上面可以大体得到这样一个结论:

- 全局/静态变量----->全局/静态存储区;
- 局部变量及局部常量------>栈;
- 动态创建的内存空间------>堆;

有了这个基础，我们来看看C++中定义的对象的内存使用情况。我们首先定义个类：

```c++
#include <stdio.h>
class CTemp
{
public:
 static int iStatic;
 int a;
 int b;
public:
 int GetA(){return a;};
 void SetA(int A){a = A;};
public:
 virtual ~CTemp(){};
};
void main()
{
 CTemp tm;
 printf("Sizeof tm :%d\n",sizeof(tm));
 CTemp tn;
 printf("Sizeof tn :%d\n",sizeof(tn));
 printf("tm GetA Function adress:   0x%x\n",tm.GetA);
 printf("tn GetA Function adress:   0x%x\n",tn.GetA);
}
```

Output:

```text
Sizeof tm :12
Sizeof tn :12
tm GetA Function adress:   0x40101e
tn GetA Function adress:   0x40101e
```

通过输出可以看出，`tm`和`tn`对象的大小都是12字节；还可以看出，两个对象使用的`SetA`函数地址都是一样的，我们先估且认为:

1. 函数不占对象的内存空间。
2. 每个int 型成员占4个字节，共计12字节。

为了验证我们的假设，我们将代码更改如下：

```c++
#include <stdio.h>
class CTemp
{
public:
 static int iStatic;
 int a;
 int b;
public:
 int GetA(){return a;};
 int GetB(){return b;};
 void SetA(int A){a = A;};
 void SetB(int B){b = B;};
public:
 virtual ~CTemp(){};
};
void main()
{
 CTemp tm;
 printf("Sizeof tm :%d\n",sizeof(tm));
 CTemp tn;
 printf("Sizeof tn :%d\n",sizeof(tn));
}
```

Output:

```text
Sizeof tm :12
Sizeof tn :12
```

通过输出可以看出，虽然增加了两个成员函数，但对象的大小并未增加。这也验证了我们的第一个假设：**成员函数并不会占用对象的内存**。

再次修改我们的代码，将CTemp类的static成员变量注释掉;

`//static int iStatic;`

Output:

```text
Sizeof tm :12
Sizeof tn :12
```

我们通过可以看出，对象大小并没有变化，这说明了，我们第二个假设：每个成员变量都占用了4个字节，是错误的。

修改代码验证，将`int a`成员注释掉;

`//int a;`

Output:

```text
Sizeof tm :8
Sizeof tn :8
```

通过输出，发现对象减少了4个字节。哦......，静态成员变量不占用对象内存。

占用内存的是`a`和`b`两个变量?不过也不对啊，两个`int`型变量应该占用8字节的空间，为何在每一类的输出中，一个对象占用了12字节。那么多余的4个字节是谁占用了呢？

分析下面的类:

```c++
class CTemp
{
public:
 static int iStatic;       [不占内存空间]
 int a;                    [4字节]
 int b;                    [4字节]
public:
 int GetA(){return a;};    [不占内存空间]
 int GetB(){return b;};    [不占内存空间]
 void SetA(int A){a = A;}; [不占内存空间]
 void SetB(int B){b = B;}; [不占内存空间]
public:
 virtual ~CTemp(){};       [虚函数占内存空间?]
};
```

虚函数占内存空间? 那我们把虚函数注释掉，再次运行我们的程序，输出如下：

```text
Sizeof tm :8
Sizeof tn :8
```

果然是虚函数占用了内存空间，那么是一个虚函数占4字节么？

再修改代码以验证，添加一个虚函数。

```c++
virtual ~CTemp(){};
virtual void GetCount(){};
```

输出如下：

```text
Sizeof tm :12
Sizeof tn :12
```

通过输出可以看出，无论多少个虚函数，只是增加了4个字节；

通过以上的验证，我们可以得知，一个对象所占有的空间，主要是非静态成员数据。

为什么增加了一个虚函数就是增加4个字节的空间，这是因为在每个拥有虚函数的对象，都会增加一个指向virtual table的指针，该指针本身占了4个字节且指向Virtual table。

一个类的静态数据成员，为所有该类生成的对象共享。增加新的对象，该静态成员数据所占用空间并不会随之增加。

函数的实现虽然需要占用了空间，但也不会随着对象的增加，而增加该部分占用的空间，总结以上可以得出下面一幅关系图。

![](http://blog.chinaunix.net/photo/11680_070605142408.gif)

从上图中可以很清楚的看出，每创建一个对象，只会增加CTemp对象部分占用的空间。而这部分反映到类中至等于:非静态数据成员+虚函数指针(4字节)。