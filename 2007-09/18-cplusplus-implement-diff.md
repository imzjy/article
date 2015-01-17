set_unexpected函数-看VC6.0对Standard C++的支持
======

异常规范(Exception Specification)，是通过异常列表(throw list)来规定一个函数只能抛出哪些异常。例如：

```c++
#include <iostream>
#include <string>
using namespace std;
void Fun()throw(string)   //Exception specification,即Throw list确保只抛出string型异常
{
 cout<<"Fun is called!"<<endl;
 throw string("Exception occurred!");   //Ok,会抛出string型异常
 //throw int(123);   //若throw出了int型异常,这会调用set_unexpected注册的函数，默认为terminate
}
```

上面的函数的异常规范指定了只用抛出string型异常，Standard C++会保证该函数只能抛出string型异常。若抛出其它异常都是不期望的(Unexpected)。

但这对Microsoft VC++6.0却不成立。试写以下代码:

```c++
// Platform: WinXp + VC6.0
#include <stdlib.h>
#include <iostream>
#include <string>
using namespace std;
void Fun()throw()   //Exception specification,即Throw list确保不发生任何异常
{
  cout<<"Fun is called!"<<endl;
  throw string("Excepton is thrown in Fun()");   //但是throw出了异常,这会调用set_unexpected注册的函数，默认为terminate
}
void Show()
{
  cout<<"unexpected excepton occurred in Fun()"<<endl;
  system("PAUSE");
}
int main()
{
  set_unexpected(Show);   //VC6并不支持，对Standard C++的支持并不好
  try
  {
    Fun();   //出现异常，虽有Throw list但仍被throw
  }
  catch(string str)
  {
    cout<<"Exception catched!"<<endl<<"description:"<<str<<endl;
  }

  system("PAUSE");
  return 0;
}
```

VC6好像并不理会Standard C++的规定。这在Microsoft的网页上得到了见证:

> In the current Microsoft implementation of C++ exception handling, unexpected calls terminate by default and is never called by the exception-handling run-time library. There is no particular advantage to calling unexpected rather than terminate.

Microsoft并不觉得unepxpected的处理会比terminate的调用更有优势.

但标准就是标准，不能因为Microsoft不支持标准而标准就会改变。还是有很多Compiler的厂商实现标准。例如我手上的Dev-C++5.0 beta版。(华军软件园上有下载)就对标准支持较好。

```c++
//Platform: WinXp + Dev-C++5.0 beta
#include <stdlib.h>
#include <iostream>
#include <string>
using namespace std;
void Fun()throw()   //Exception specification,即Throw list确保不发生任何异常
{
 cout<<"Fun is called!"<<endl;
 throw string("Excepton is thrown in Fun()!");   //但是throw出了异常,这会调用set_unexpected注册的函数，默认为terminate
}
void Show()
{
    cout<<"unexpected excepton occurred!"<<endl;
    system("PAUSE");
}
int main()
{
 set_unexpected(Show);   //Dec-C++支持，对Standard C++的支持较好
 try
 {
  Fun();     //Show() is invoked when Fun() throw the exception
             //此时，代码跳至Show中处理
 }
 catch(...)
 {
  cout<<"Catch exception!"<<endl;
 }

 system("PAUSE");
 return 0;

}
```

其实上面也只是说明VC6对标准C++支持并不是十分完全，但这并不是什么坏事。相反VC6还是很好用的。不过对Standard C++的有些特性不支持，学习C++语言时可就要留个心眼了。当你看《C++ Primer》等标准C++的教材时，如果书有些例子拿到VC6中并不能编译通过，再怀疑代码敲错或书上代码印错的同时还得想想是不是VC6不够Standard.(不过还好的是VC6.0基本上90%以上还是挺标准的)。
