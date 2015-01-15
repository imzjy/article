反转数组
=======

昨天老赵给了篇文章《[为什么我要反对北大青鸟](http://blog.zhaojie.me/2010/04/why-i-say-no-to-aptech.html)》，回想起刚毕业那会儿为了生计差点儿进北大青鸟做讲师，差点儿害人害已。细想来我还是幸运的。老赵在文章中提到：如果不能将一个数组反转，还能叫程序员吗？

我细细想来，我从写程序到现在还真没有做过这样的事。我进入程序员行业中学习的是C++语言，但除了写些东西玩玩外，平时已经不用了，更确切地说：不太会用了。有些语法已经需要翻《C++ Primer》，这也使我诚惶诚恐，每次面试前我都需要将这个大部头再翻一下回忆回忆，省得到时面试官让我写个代码我一行写不出，但简历或许是精通或熟悉C++。

前两天听[Anders的讲座](http://channel9.msdn.com/posts/adebruyn/TechDays-2010-Developer-Keynote-by-Anders-Hejlsberg/)，讲座中提到当前语言发展的三大块：Language, Library, Tools。其中Language进步很小，而Library和Tools进步神速。我当时也在Twitter发了tweet支持这个观点。但后来我又仔细想了一下，虽然当前语言大都还是由if...else...组成，但由于库的增强使得需要写if..else的时间越来越少。

为验证一下自己是不是程序员，我也来写一个反转数组的程序。先来个简单地C#版：

```csharp
class Program
{
    static void Main(string[] args)
    {
        List<int> arr = new List<int> { 2, 5, 3, 1, 4, 7, 6 };
 
        PrintArray(arr);
        arr.Reverse();
        PrintArray(arr);
 
        Console.ReadKey();
    }
 
    static void PrintArray(List<int> arr)
    {
        arr.ForEach(i => Console.Write("{0} ", i));
        Console.WriteLine();
    }
}
```

就真实应用来说上面的数组反转更可能出现在生产代码中，有多少程序员在生产环境中写过反转数组的代码？

面试数组反转主要考的是思维基础。我又用C写了一个数组反转的程序：

```c
#include "stdafx.h"
#define SIZE 7
 
void PrintArray(int arr[]);
void ReverseArray(int arr[]);
 
 
int _tmain(int argc, _TCHAR* argv[])
{
    int original[] = {2,5,3,1,4,7,6};
    PrintArray(original);
     
    ReverseArray(original);
    PrintArray(original);
 
    char wait = getchar();
    return 0;
}
 
void PrintArray(int arr[])
{
    for(int i = 0; i < SIZE; i++)
        printf("%d ",arr[i]);
    printf("\n");
}
 
void ReverseArray(int arr[])
{
    int temp = 9999;
    for(int i=0; i < SIZE/2; i++)
    {
        temp = arr[i];  //Step One
 
        int lastIndex = (SIZE - 1) - i;
        arr[i] = arr[lastIndex];  //Step Two
 
        arr[lastIndex] = temp;    //Step Three
    }
}
```

但就是这个数组反转代码段，我在面试的时候也没有写出来。即使今天我写这个程序也用了半个小时，但真正思考的时间却不多。漫长地半个小时是这样过来的：

1. 想一下问题，选一组测试数据。2分钟。
2. 空想不行，画个图，思考一下，比如元素个数为奇数和元素个数为偶数处理上有没有什么不同。2 分钟。
3. 想一下语言特性：地板除7/2结果是3，验证一下。(中间上网下了本ebook，乱想了一会儿)。 20分钟以上。
4. 验证。 1分钟。

即使写好了，我仍然诚惶诚恐。因为我不能保证我写的程序没有bug。我想很多朋友随便看上两眼bug或许就出来了。做个程序员或许不难，[找份职位是程序员或软件工程师](http://www.cnblogs.com/diggingdeeply/archive/2010/04/22/The_one_who_can_program_is_unlikely_a_programmer_it_possibly_is_a_software_engineer.html)的工作就成，但[编程好难](http://coolshell.cn/?p=1391)啊 :D
