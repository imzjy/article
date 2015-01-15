C#函数式编程风格-范型Filter,Map,Reduct函数的实现
========

早上看园友的一篇文章《[lambda与闭包](http://www.cnblogs.com/perhaps/archive/2010/05/03/1726442.html)》，忽然间想起了以前刚学Python，刚接触FP时的高兴劲。对FP的no-side-effect的向往，对Declaration式编程的喜爱，让我对于编程，对于另一种程序设计的思想有了种转变。

还记得那时，看到Python中的built-in函数Filter,Map,Reduce，心想为什么.NET的BCL中怎么就没有呢。C#3.0出来以后，基本上已经可以DIY一个山寨版的Filter,Map,Reduce了，看代码：

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
 
namespace FuncPro
{
    class Program
    {
        static T[] Filter<T>(Func<T, bool> func, IEnumerable<T> iSource)
        {
            List<T> iResult = new List<T>();
            foreach (var item in iSource)
            {
                if (func(item))
                    iResult.Add(item);
            }
            return iResult.ToArray();
        }
        static T[] Map<T>(Func<T, T> func, IEnumerable<T> iSource)
        {
            List<T> iResult = new List<T>();
            foreach (var item in iSource)
            {
                iResult.Add(func(item));
            }
 
            return iResult.ToArray();
        }
        static T Reduce<T>(Func<T, T, T> func, IEnumerable<T> iSource)
        {
            T sum = default(T);
            foreach (var item in iSource)
            {
                sum = func(sum, item);
            }
            return sum;
        }
 
        static void PrintArray(int[] iSource)
        {
            Console.Write("\t");
            iSource.ToList().ForEach(x => Console.Write("{0} ", x));
            Console.WriteLine();
        }
        static void Indent(string msg)
        {
            Console.WriteLine("{0}:", msg);
        }
 
 
        static void Main(string[] args)
        {
            int[] iSource = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
            Indent("Source");
            PrintArray(iSource);
 
             
            int[] iFilterResult = Filter(x => x > 5, iSource);
            Indent("Filter, item more than 5");
            PrintArray(iFilterResult);
 
 
            int[] iMapResult = Map(x => x * 2, iSource);
            Indent("Map, multiple with 2");
            PrintArray(iMapResult);
 
 
            int iReduceResult = Reduce((x, y) => x + y, iSource);
            Indent("Reduce");
            Console.Write("\t{0}\n ", iReduceResult);
 
            Console.ReadKey();
        }
    }
}
```

前些日子和一个朋友闲聊到.NET加入了很多函数式编程的元素，应该可以写出函数式编程风格的代码来，也应该算是支持函数式编程的语言了，今天随手写了代码感觉确实是这样了。

PS.

今天看《CLR via C# 3e》时看到Jefferey利用扩展方法(Extension Method)来提高代码可读性的例子，我将上面的代码重构了一下，以提高可读性：

```csharp
static class ExtendMethod
{
    public static void ShowItems<T>(this IEnumerable<T> collection)
    {
        Console.Write("\t");
        collection.ToList().ForEach((x) => Console.Write("{0} ", x));
        Console.WriteLine();
    }
}
class Program
{
    static T[] Filter<T>(Func<T, bool> func, IEnumerable<T> iSource)
    {
        List<T> iResult = new List<T>();
        foreach (var item in iSource)
        {
            if (func(item))
                iResult.Add(item);
        }
        return iResult.ToArray();
    }
    static T[] Map<T>(Func<T, T> func, IEnumerable<T> iSource)
    {
        List<T> iResult = new List<T>();
        foreach (var item in iSource)
        {
            iResult.Add(func(item));
        }
 
        return iResult.ToArray();
    }
    static T Reduce<T>(Func<T, T, T> func, IEnumerable<T> iSource)
    {
        T sum = default(T);
        foreach (var item in iSource)
        {
            sum = func(sum, item);
        }
        return sum;
    }
 
    static void PrintArray(int[] iSource)
    {
        Console.Write("\t");
        iSource.ToList().ForEach(x => Console.Write("{0} ", x));
        Console.WriteLine();
    }
    static void Indent(string msg)
    {
        Console.WriteLine("{0}:", msg);
    }
 
    static void Main(string[] args)
    {
        int[] source = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        Indent("Source");
        source.ShowItems();
 
         
        int[] filterResult = Filter(x => x > 5, source);
        Indent("Filter, item more than 5");
        filterResult.ShowItems();
 
 
        int[] mapResult = Map(x => x * 2, source);
        Indent("Map, multiple with 2");
        mapResult.ShowItems();
 
 
        int reduceResult = Reduce((x, y) => x + y, source);
        Indent("Reduce");
        new[] { reduceResult }.ShowItems();
 
        Console.ReadKey();
    }
}
```
