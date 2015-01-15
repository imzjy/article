列举整数的各位数值
========

记得上次面试，有道题目：给出一个整数，请打印出该整数的各位数值是多少。比如输入为：274396。输出：

```text
第1位为 6； 
第2位为 9； 
第3位为 3； 
第4位为 4； 
第5位为 7； 
第6位为 2；
```

面试的时候，我不太能做算法相关的题，因为很难让自己保持平静，让自己的脑子空下来。而算法的东东，想的彻底的一会儿就可以搞定，而糊涂起来半天也没有个结果。今天正好有同事问起类似的问题，我突然回忆起的当时面试时的题目，当时做的也不太好，虽然实现了功能，但不漂亮。凭直觉我知道有更优雅的代码/思路可以完成这个任务。

见代码：

```csharp
static void Main(string[] args)
{
    Console.WriteLine("Type the nubmer:");
    int number = int.Parse(Console.ReadLine());
 
    List<int> list = new List<int>();
    for (int i = number; i > 0; i = i / 10)
    {
        list.Add(i % 10);
    }
 
    Console.WriteLine("原数字: {0}", number);
    for (int i = 0; i < list.Count; i++)
    {
        Console.WriteLine("第{0}位的数字为: {1}", i+1, list[i]);
    }
 
 
    Console.ReadKey();
}
```

