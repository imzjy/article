Fisher–Yates shuffle 洗牌算法
======

### 1，缘起

最近工作上遇到一个问题，即将一组数据，比如[A,B,C,D,E]其中的两个B,E按随机排列，其他的仍在原来的位置：

```text
原始数组：[A,B,C,D,E]
随机字母：[B,D]
可能结果：[A,B,C,D,E],[A,D,C,B,E]
```

在解决这个问题的过程中，需要解决的一个问题是，怎么样让一个数组随机排序？上网一查，这也是计算机科学基础问题，也称之为洗牌算法(Shuffle Algorithm)。

### 2，问题及解决

#### 2.1，问题

很简单：给定一个数组，将其中的元素随机排列。比如给定数组arry=>[1,2,3,4,5]。有A5-5种结果即5!=120种结果

#### 2.2，解决

也很简单，如果用白话来说就是：

1. 选中第1个元素，将其与n个元素中的任意一个交换(包括第1个元素自己)。这时排序后的第1个元素已经确定。
2. 选中第2个元素，将其与n-1个元素中作任意一个交换(包括第2个元素自己)。
3. 重复上面步骤，直到剩1个元素为止。

#### 3.3，代码

知道其算法了，实现就简单了：

```text
/// <summary>
/// Randomize the list elements using Fisher–Yates shuffle algorithm http://en.wikipedia.org/wiki/Fisher-Yates_shuffle
/// </summary>
/// <typeparam name="T">elements type</typeparam>
/// <param name="list"></param>
public static void Shuffle<T>(this IList<T> list)
{
    Random rng = new Random();
    int n = list.Count;
    while (n > 1)
    {
        n--;
        int k = rng.Next(n + 1);
        T value = list[k];
        list[k] = list[n];
        list[n] = value;
    }
}
```

#### 3.4，其它

该算法复杂度为O(n)，且无偏差，各个元素随机概率相等。确实是一个好算法:)。

在Wiki上，还有一些该算法的变种，但还是上面讲的那种比较好用，最初的Fisher–Yates算法并不好用，复杂度为O(n^2)。

----

参考

http://blog.codingnow.com/2007/09/shuffle.html

http://en.wikipedia.org/wiki/Fisher-Yates_shuffle
