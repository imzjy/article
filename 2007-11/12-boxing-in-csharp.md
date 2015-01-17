C#中的装箱(Boxing)和拆箱(Unboxing)
========

C#中有个术语(term)：装箱(Boxing)和拆箱(Unboxing)。这两个动作也常常是低效语句的“帮兄”。在了解Boxing和Unboxing之前先来看看C#中的另一个概念：值类型(value type)，引用类型(reference type).

### 1. Reference type and value type.

在C#中定义几个变量例如：

```csharp
int age = 12;
MessageType msgType = MessageType.OK //enum型


string name = "Jerry";
object o = new OleDbConnection();
```

其中age, msgType是值类型，而name,o属于引用类型。C#中规定：

以下类型是值类型：

```text
  数值型(int,float.decimal...),
  结构体(struct),
  枚举型(enum).
```

而像：

```text
  类类型(class),
  接口(interface),
  委托(delegate),
  object,
  string.
```

则属于引用类型。

#### 1st,Difference between the reference type and the value type:

其实value type和reference type的本质差别的内存的分配方式不同。类似于上面的定义，在内存中的方式如下图：

![](http://blog.chinaunix.net/photo/11680_071114091412.gif)

在定义一个值类型时，会在线程的Stack中为该变量分配空间，并在此空间中保存该变量的值。而在定义一个引用类型时会在Managed heap(托管堆)中为该变量分配足够大的空间，并返回该空间的"引用"(即Managed heap中的地址),并保存在Stack上.任何对Managed heap上对象的访问都必须通过Stack上的"引用/指针"来进行.

例如上图,在stack中，age或MsgType中保存的是“值”,而name或o中保存的是“引用”，可以通过该引用来访问Heap上的实际值("Jerry"字串或OleDbConnection对象)。

从图中还可以看出：“引用类型多了一层间接性”.当我们访问name时，首先找到name,由于name是一个reference type所以找到的name只是一个"reference"。真正的值分配在Heap上，并通过该"reference"来访问。

注:此处"reference" 即是 托管对象(managed object)在托管堆(managed heap)中的地址.之所以使用"reference"是因为C#.Net中好像并不提倡很直白的说"地址"(address),或是"指针"(pointer)...,下同.

#### 2nd,Something you must notice.

变量(或对象)是在Statck中分配空间,还是在Managed heap中分配中空完全取决于该对象是reference type还是value type.如下面的代码:

```csharp
int iVal = new int(); //iVal保存一个int型值
string name = "jerry"; //name保存"jerry"在Managed heap上的引用
```

### 2,Boxing and Unboxing.

#### 1st, Boxing.

Boxing的动作分为两步：

1. 将Stack中的值类型Copy至Heap中；
1. 在Stack上通过一个"reference"来访问位于Heap中的Copy值;

例如：

```text
//first copy the value of age(12) to heap.then rAge refer to heap which saved the copyed value of 12.
object rAge = age;
```

在内存中的表示如下：

![](http://blog.chinaunix.net/photo/11680_071112200141.gif)

#### 2nd, Why we need boxing and when.

一些函数只接受object型的参数,其实我个人更愿意称些类函数为泛型函数.例如ArrayList.Add()函数,该函数只接爱object型参数,而当你写出如下代码时:

```csharp
int val = 100;
ArrayList al = new ArrayList();
al.Add(val);
```

此时便发生Boxing,将val的值Copy至Managed heap中,并该返回的"reference"通过al.Add(Object o)方法加入至al中.

#### 3rd, Unboxing.

Unboxing的动作也分为两步:

1. 通过"reference"引用到位于Managed heap中的值;
1. 将该值Copy至值类型的变量中保存(该变量位于Stack上);

例如下面的代码:

```csharp
int val = 12;

object o = val;
int b = (int)o;  //Unboxing
```

在内存中发生的动作如下图:

![](http://blog.chinaunix.net/photo/11680_071114103136.gif)

#### 4th, Why we need unboxing and when.

简单点讲,想让那些已装箱的数据保存在值类型的变量中时,就需要Unboxing.例如接上面的ArrayList的代码.当我需要将al中的元素保存在一个int型(本质是int型属于值类型)变量中,就需要Unboxing.

```csharp
int retVal = al[0];      //Error,不能将引用类型的object保存在值类型int中.
int iVal = (int)al[0]; //OK,通过Unboxing将元素copy至stack中的iVal中.
```

注意:此时al[0]引用的堆上的变量(对象)和位于Stack中的iVal变量是两个互不相干的变量.

#### 5th, Something you must notice.

装箱(Boxing)是会做一些类似Copy,创建托管堆上的对象(Create object in managed heap),并有可能需要做垃圾回收(Garbage Collection)等动作.所以会带来一些性能损耗(Overhead).其中创建托管堆上的对象带来的性能消耗占了很大比重.这是因为在托管堆上创建一个对象有以下几个动作来完成:

1. 在堆上分配足够大的空间;
1. 可能带来一次垃圾回收(GC)的动作;
1. 堆上对象都要附加两个成员:类型对象&同步块索引;
1. 将Stack上变量Copy至heap中;

相比之下拆箱(Unboxing)只做一次Copy的动作,而且通常value type都是一些"light variant".所以由拆箱带来的性能损耗会小的多,一般情况下可以忽略.
