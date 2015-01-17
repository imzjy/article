设计模式之抽象工厂
=======

《设计模式》的书已买过有段时间了，看来看去像是看经书:都是实话，但似乎都是些没有用了。佛家讲这叫悟性不够。周五晚上看《Effictive C++》时突然来了些灵感，是顿悟嘛，我想不是。而是渐悟后的觉悟罢了。即然是好东西，分享当然是最快乐的事情了，那我现在就开始我的快乐之旅。

Abstract Factory(抽象工厂)，让我们先抛开程序设计的观感(虽然话是如此，我想这对像我一样的程序员来说很难，毕竟程序员都很执着)，来看看抽象工厂是什么意思。工厂：用来生产东西的。抽象的工厂，哟哟哟...看来该工厂还是个假的并不实际存在。

或许我们可以把抽象工厂当做呼唤“阿拉丁”神灯的那个怪物的咒语。你在念完咒语之后大叫：“我要个锤子。”没有多久一个锤子就会出现在你面前。你还可以在念完咒语之后大喊：“我要一台电脑。”那么没有多久一台崭新的电脑也会出现在你的面前。如果我要是掌握了这个咒语我会做什么呢？嗯，想到了。我会对着天空大叫三声：“给我一个女朋友吧!”。西西...

书回原位，其实我们谁都都要这样一个工厂。毕竟想要什么都可以让工厂给我生产。在程序设计中出现这种情况会更多。让我们从一个实例开始吧(摘自《设计模式精解》):

现在我们需要做一个系统软件需要支持不同的显示及打印分辨率。我们可能先会想以这个实现：

```text
if 当前显示率为800*600 then
   new 打印驱动对象
打印驱动对象.打印

if 当前显示率为400*300 then
   new 显示驱动对象
显示驱动对象.显示
```

如果我们需要new十个相应的驱动对象，红色部分是不是太麻烦(需要重复十次)，万一你哪次写错了怎么办!你每次new对象时必须记住当前的分辨率，这是多么复杂和无聊的事情啊。

> Software's primary technical imperative: managing complexity(软件首要技术使命：管理复杂度)

> -- McConnel(The author of code complete2)

既然这么复杂，那么我们该去管管它了。我们建立一个类来管管他。嗯...走到这步我们离Abstract Factory就不远啦.

我们试想的方式是如下的:

```text
给我一个打印驱动对象吧,这时一个打印驱动对象出现在你的面前
   打印驱动对象.打印
给我一个显示驱动对象吧,这时一个显示驱动对象出在在你的面前
   显示驱动对象.显示
```

Oh.so nice...想要时就大呼一声,这是件多么令人向往的事啊."我要一个女朋友啊...小崔..这段掐了别播".

再看看具体是怎么实现的,现给出完整代码(源码之前,了无秘密).在给出源码之前给出类图,以帮助理解.从下面这张图中可以看出[主程序]只和DrvFactory,Display,PrintDriver进行交互.再者这三个类(黄色)也都只是个接口(C++没有接口的概念，用Abstract class来实现).只和接口交互，隐藏了细节。这才是Abstract Factory本身想表达的意义。

![](http://blog.chinaunix.net/photo/11680_070918102737.jpg)

```c++
Platform: WinXp+VC++6.0
/*----------------
No.: one
Filename: AbstractFactory.cpp
Desc: 主程序
----------------*/
#include <iostream>
#include <string>
#include "Factory.h"
using namespace Factory;

void main()
{
 DrvFactory *pResFactory;

 cout<<"Please input resolution,format likes \"800*600\" or \"1024*768\""<<endl;
 string strConfig("800*600");
 cin>>strConfig;

 if(strConfig == "800*600")
  pResFactory = new LowResolutionFactory();
 else if(strConfig == "1024*768")
  pResFactory = new HighResolutionFactory();
 else
 {
  cout<<"The format of resolution is error!"<<endl;
  return;
 }

 //使用相应分辨率的驱动
 //这时你可以忘记具体的分辨率了(被封装起来了),需要用到Driver时至pResFactory"拿来"即可(拿来主义)
 DisplayDriver *pDisplayDriver = pResFactory->GetDispDrv();
 pDisplayDriver->Display();
 delete pDisplayDriver;  //用完将其删除，防止memory leak

 PrintDriver *pPrintDriver = pResFactory->GetPrintDrv();
 pPrintDriver->Print();
 delete pPrintDriver;
}
/*------------------------------------------------------
No.: two
Filename: DvrFactory.h
Desc: DrvFactory,LowResolutionFactory,HighResolutionFactory三个类的头文件
-------------------------------------------------------*/
#include "Headers.h"
using namespace Driver;
namespace Factory
{
 class DrvFactory
 {
 public:
  virtual ~DrvFactory(){};
  virtual DisplayDriver *GetDispDrv()=0;
  virtual PrintDriver *GetPrintDrv()=0;
 };

 class LowResolutionFactory:public DrvFactory
 {
 public:
  DisplayDriver *GetDispDrv();
  PrintDriver *GetPrintDrv();
 };
 class HighResolutionFactory:public DrvFactory
 {
 public:
  DisplayDriver *GetDispDrv();
  PrintDriver *GetPrintDrv();
 };
}
/*--------------------------
No.: three
Filename: DrvFactory.cpp
Desc: DrvFactory(抽象类，无实现文件),
      LowResolutionFactory,HighResolutionFactory二个类的实现文件
---------------------------*/
#include "Factory.h"
#include "headers.h"
using namespace Factory;
using namespace Driver;
//生成低分辨率Driver对象
DisplayDriver* LowResolutionFactory::GetDispDrv()
{
 return new LowResolutionDisplayDriver();
}
PrintDriver* LowResolutionFactory::GetPrintDrv()
{
 return new LowResolutionPrintDriver();
}
//生成高分辨率Driver对象
DisplayDriver* HighResolutionFactory::GetDispDrv()
{
 return new HighResolutionDisplayDriver();
}
PrintDriver* HighResolutionFactory::GetPrintDrv()
{
 return new HighResolutionPrintDriver();
}
/*--------------------------------------
No.: four
Filename: DisplayDriver.h
Desc: DisplayDriver,
      LowResolutionDisplayDriver,HighResolutionDisplayDriver三个(显示)类头文件
----------------------------------------*/
#include <iostream>
using namespace std;
namespace Driver
{
 class DisplayDriver
 {
 public:
  virtual ~DisplayDriver(){};
  virtual void Display()=0;
 };
 class LowResolutionDisplayDriver:public DisplayDriver
 {
 public:
  void Display();
 };
 class HighResolutionDisplayDriver:public DisplayDriver
 {
 public:
  void Display();
 };
}
/*--------------------
No.: five
Filename: DisplayDriver.cpp
Desc: DisplayDriver(抽象类)
      LowResolutionDisplayDriver,HighResolutionDisplayDriver二个(显示)类的实现文件
---------------------*/
#include "DisplayDriver.h"
using namespace Driver;
void LowResolutionDisplayDriver::Display()
{
 cout<<"Display picture in Low Resolution(800*600)"<<endl;
}
void HighResolutionDisplayDriver::Display()
{
 cout<<"Display picture in High Resolution(1024*768)"<<endl;
}
/*------------
No.: six
Filename: PrintDriver.h
Desc: PrintDriver,
      LowResolutionPrintDriver,HighResolutionPrintDriver三个(打印)类的头文件
------------*/
#include <iostream>
using namespace std;
namespace Driver
{
 class PrintDriver
 {
 public:
  virtual ~PrintDriver(){};
  virtual void Print()=0;
 };
 class LowResolutionPrintDriver: public PrintDriver
 {
 public:
  void Print();
 };
 class HighResolutionPrintDriver: public PrintDriver
 {
 public:
  void Print();
 };
}
/*-------------------------------
No.: seven
Filename: PrintDriver.cpp
Desc: PrintDriver(抽象类)
      LowResolutionPrintDriver,HighResolutionPrintDriver二个(打印)类实现文件
--------------------------------*/
#include "PrintDriver.h"
using namespace Driver;
void LowResolutionPrintDriver::Print()
{
 cout<<"Print the Photo in Low Resolution Printer..."<<endl;
}
void HighResolutionPrintDriver::Print()
{
 cout<<"Print the Photo in High Resolution Printer..."<<endl;
}
/*-----------------------------------
No.: eight
Filename:headers.h
Desc: 为了防止重复包含而定义的头文件
------------------------------------*/
#ifndef PRINTDRIVER_H
#define PRINTDRIVER_H
#include "PrintDriver.h"
#endif
#ifndef DISPLAYDRIVER_H
#define DISPLAYDRIVER_H
#include "DisplayDriver.h"
#endif
```

其实从最初的那张图来看,DrvFactory就是我们的呼唤"阿拉丁"神灯的咒语.我们管需要什么样的类,向其大喊一声即可.这最终还是一种封装的思想.Abstract Factory封装了一个创建具体对象的过程,这给我们程序设计带来的更大的灵活性和弹性.

试想如果我们现在又增加了一个分析率1600*1200,那么我们要做哪些工作呢?

新增一个1600*1200的显示类(Derived from DisplayDriver)及打印类(Derived from PrintDriver)即可(这一步是必不可少的,所以我们只有乖乖地做好他)

试想如果我们现在加了一个扫描仪那么我们又需做哪些工作呢? 我们只需新增一个扫描仪驱动类(ScannerDriver)即可.

看起来应该是下面这样(为了看起来清爽,我省略了部分虚线):

!{}(http://blog.chinaunix.net/photo/11680_070918103139.jpg)

根本问题是这些更改并不会影响现存的代码,这是多么奇妙的事啊.

附记：昨天晚上写完之后，回去想了一下，觉得并没有表达清楚。自己想着都模糊怎么能让别人看的懂呢。既然语言表达不清楚，就用图吧。所以今天特地将两幅图更新了一下。希望可以见图知意。
