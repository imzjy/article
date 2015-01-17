《Inside the C++ Object Model》E文整理之一
======

```text
1, with the exception of  除……外
Exp: With the exception of brief discussion within [ELLIS90] and [STROUP94]
C: 除了[ELLIS90] and [STROUP94] 有简单的讨论
J：除[ELLIS90] and [STROUP94]中有蛛丝马迹

2，feel very strongly that 强烈认为……
Exp: They feel very strong that rabbit can fly.
M:他们强烈认为兔子会飞.

3，sort of 有那么点儿，有几分
4，lead to 导致
5，hold by 坚持
Exp: It is this sort of “myth and legend” leads to opinions such as those held by your colleagues.
M:就是这点儿“ (C++语言的)神说传说”，导致了你同事们(坚持)的看法。

6，referred to as 被称为……
Exp: This story referred to as “myth”.
M:这个故事被称之为“神话”。

7，do away with 废除，去掉
Exp: They decided to do away with the rule.
M: 他们决定废除这条规则。

6，rather than  而不是
Exp: It is aimed at the intermediate C++ programmer rather than the novice.
M:它（Inside C++ Object Mode这本书）是针对中级C++程序员的，而不是C++的初学者。

7，field  巧妙回答
8，astounding patience 惊人的耐心
Exp: She fielded all too many questions about Standard C++ both with astounding patience and fearful insight.
M：她以惊人的耐心和独特的眼光回答了很多关于Standard C++方面问题。

9，Portion of （一）部分
Exp: portions of this text were originally published as column in the magazine while I was editor.
M：这本书的部分内容在我做编辑的时候被我作为专栏发表在杂志(C++ report)上。

10，not only……but also…….不仅…..而且
Exp: These are obviously not only very difference style of programming, but also very difference ways of thinking about our program.
M：明显，这不仅是编程风格的不同，而且也是我们对程序的思考方式的不同。

11，at the expense of  以……为代价
Exp: She completed the work at the expense of her health.
M: 她完成了工作，但损坏了健康。

12，rely on   依靠......
Exp: The SOM object model also relies on this two table model.
M:  SOM对象模型也依靠这种双表格模型。

13，make use of ......   利用…….
Exp: Its primary drawback is the need recompile unmodified code that makes use of an object of class for which there has been an addition, removal, or modification of the nonstatic class data members.
M: 它(C++对象模型)主要的缺点是需要重新编译并未改动的代码(这些代码使用了已新增，移去，更改了nonstatic data members的类)。
J:  他的主要缺点是，如果应程序代码本身未变，但所用到的class objects的nonstatic data members有所修改(可能是增加，移除，或修改)，则需要重新编译应用程序代码。

14，in the case of…… 至于……
regardless of  不顾，不管
Exp: In the case of virtual inheritance, only a single occurrence of base class is maintained (called a subobject) regardless of how many times the class is derived from within the inheritance chain.
M: 至于虚继承，只有一个基类实例生成，而不管在继承链中基类被派生了多少次。
J: 在虚拟继承情况下，不管base class在继承链中被派生(derived)了多少次，永远只会存在(maintained)一个实体。

15，either……or……不是…..就是……，要么…….要么
Exp: Alternative models have evolved that either introduce a virtual base class table or augment the existing virtual table to maintain the location of each virtual base class.
M：其它(alternative)演化出来的模型，要么是引入一个virtual base class table，要么增加已存在的virtual table，用来维护每个virtual base class的位置

16，be supposed to 可以, 应该
Exp: You’re not supposed to understand all of these transformations at this point in this book.
M：只在本书的该章节中，你不可能了解所有这些转换。

17，ever [副词] 总是，始终，永远
Exp: He is ever ready to help you.
M: 他总是乐意(ready to)帮助你。

18，in place of  代替
as well as 和，同…..一样
Exp: We can use struct in place of class, but still declare public, protected, private sections and a full public interface, as well as specify virtual functions and full range of single, multiple, and virtual inheritance.
M: 我们可以使用struct来代替class，但仍申明public, protected, private区域和full public interface ，以及指定virtual functions and full range of single, multiple, and virtual inheritance.

19，is determined by….   由…..决定， 取决于……
Exp: The conceptual meaning of the two declarations is determined by an examination only of the body of the declaration.
M：这两种声明在观念上的意义由“申明”本身的检验决定。
J： 这两种声明的观念上的意义取决于对“声明”本身的检验。

20，stumble 绊倒，绊脚
stumble across 偶然发现，偶然碰见
around 大约
Exp: I first stumble across what I call the “passion of the keyword” around 1988 when a new member of our internal testing group issued a dead-in-the-water bug report against cfont itself.
M：我第一次遇到被我叫做“keyword受难记”大约(around)是在1988年，当时我们内部测试小组的一位新成员对(against)cfont 发出了(issued)dead-in-the-water 的臭虫报告。

21, fall outside    落在……之外, 逸出
Exp: The definition and use of thing1 fall outside the OO idiom.
M：thing1的定义和使用落在OO习惯之外了。
J：thing1 的定义和使用逸出了OO习惯。

22, In terms of……   就…而论, 在…方面
Exp: In terms of memory requirements, there is generally no difference.
M：在占用(需求)的内存方面，通常没有什么不同。

23, other than… 除了…
Exp: pz cannot directly access any members other than those present within ZooAnimal subobject, except through the virtual mechanism.
M：pz(指向ZooAnimal)的指针不能直接访问出现在ZooAnimal以外的成员，除了通过虚拟机制。
J：除了 ZooAnimal subobject 中出现的成员，不能直接使用pz访问Bear的任何成员，唯一例外的是通过虚拟机制。

24， take place  发生,举行
Exp: This synthesis, however, take place only if the constructor actually needs to be invoked.
M：这种种合成只在Constructor真正需要被调用时才发生。

25，prior to… 在….之前
Exp: The compiler augments the existing constructors, inserting code that invokes the necessary default constructors prior to the execution of user code.
J：compiler扩充了存在的代码，在其中安插了一些代码，使得用户代码在被执行之前,先调用必要的default constructors.

26，in the order of…   以……顺序
Exp: The synthesized default constructor of the derived class invokes the default constructor of each of its immediate base classes in the order of their declaration.
M：派生类的default constructor 以当前基类声明的顺序调用每个(基类的)default constructor。

27, at length… 详细地[作副词用]
Exp: The problem will be discussed at length in subsequent chapters.（at length修饰discuss）
M：问题将被在随后几章里详细地讨论。


28, in the course of…   在…期间，在…过程中
Exp: If there is a program need for a default constructor, such as initializing a point to 0, it’s programmer’s responsibility to provide it in the course of class implementation.
M；如果是程序上需要default constructor，诸如初始化一个指针为0。这是程序员的责任，程序员需要在类的实现(implementation)过程中提供default constructor。

29，in effect  1,实际上，在功效方面
2,生效
Exp1: In effect, the Bear portion of yogi is sliced off when franny is initialized.
M：实际上，在franny被初始化的时候，yogi 的部分(成员)被削除。
Exp2: The old regulations will remain in effect until next June.
M：旧的税到明年6月前仍然有效.

30，side effect   副作用
Exp: At least in the case of a synthesized copy constructor, the possibility of program size effect is nil and optimization would seem to make good sense.
M：至少在合成copy constructor的情况下，产生程序副作用的可能性为零。同时优化似乎会产生很好效果。

31，rest  1,休息，
2剩余的部分，其余 [the rest of ]
Exp: The rest of subsection explains why.
M：剩余的章节说明为什么会这样。

32，substitute for 代替
Exp: Tom substituted for the injured player.
M：Tom 代替了那个受伤的运动员。

33，at fault 犯错误，出毛病
Exp: Is the compiler at fault here for suppressing the copy constructor invocation?
M：是否compiler抑制了copy constructor 的调用而在这儿出错了。

34, result in 导致，结果是
Exp1：This implementation of the Word constructor initializes _name once, then overrides the initialization with an assignment resulting in the creation and the destruction of a temporary String object.
M：Word的构造函数的实现，初始化_name一次，(但)这时(compiler)以assignment重写了该初始化(构造函数).导致了临时字串对象的构建和销毁。
Exp2：This results in a total size of 12 bytes.
M：(这样)结果是总共12个字节大小。

35，confuse…with… 将….和….相混淆
Exp：Many people new to C++ confuse syntax of the list with that of a set of function calls。
M：许多刚接触C++的人，会将list的语法和一组函数的调用相混淆.

36, the same as….跟….一样
Exp: It looks exactly the same as when _cnt is assigned within the body of the constructor.
M：他看上去跟在constructor中给_cnt赋值一样。

37，apart from 除去…不考虑…
Exp: Apart from the issue of weather the members it accesses have been initialized.
M：不考虑它访问的成员是否已被初始化的问题

38，in preparation for 作为….的准备
Exp：In preparation for his work, he coded and then printed out the result of applying the sizeof operator to the following seemingly trivial class hierarchy.
M：作为准备工作，他编写了代码，同时打印出了下面看起来无用的类层次结构的sizeof结果。

39，in turn  依次
Exp：Let’s look at each declaration in turn and see what’s going on?
M：让我们依次看看每个(类的)声明，同时看看发生了什么。

40，in part  在某种程度上，部分地
Exp：Obviously, in part that depends on the compiler being used.
M：显然，在某种程度上这依赖你使用的compiler。
```
