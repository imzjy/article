Find closest number in a list
========

### 1，Problem

There are two ordered list, the list a and the list b, such as:

```text
a=>[1,14,20,36]
b=>[2,7,11,25,32,39]
```

the result that I want to get is:

```text
result=>[(2,1),(7,null),(11,14),(25,null),(32,null),(39,36)]
```

Put it into word: find the closest number(which delta between counterpart  is less than 5) in list a for each item in list b.

First of all, I decide to divide the problem to:

1. find closest number for each item in a, since a is less elements than b.
2. compose a result into a list. if no proper value be found, put it to null.

Because a&b are ordered list, so binary search is fast way to find out corresponding closest value. The complexity of binary search for a ordered list is O(log(N)).Each of item in list a have O(N), so the total complexity is O(N*log(N))。

 
### 2，Code

How to use the code:

```csharp
static void Main(string[] args)
{
    int[] arrTime = { 1, 3, 5, 7, 8, 9, 10, 12, 15, 18, 25 };
    int[] arrAlign = { 3, 6, 11, 15, 22 };
 
    FindClosestNumber finder = new FindClosestNumber(3);
 
    var lst = finder.FindClosestAlignment(arrTime, arrAlign);
 
    foreach (var item in lst)
    {
        Console.WriteLine("{0}\t\t{1}", item.Time, item.Alignment);
    }
 
    Console.ReadKey();
 
}
```

There is the code:

```csharp
public class Pair
{
    public Pair(int? time, int? alignment)
    {
        Time = time;
        Alignment = alignment;
    }
    public int? Time { set; get; }
    public int? Alignment { set; get; }
}
 
public class FindClosestNumber
{

    public int Threshold { get; set; }

    public FindClosestNumber()
    {
        this.Threshold = 50;

    }
    public FindClosestNumber(int threshold)
    {
        this.Threshold = threshold;
    }


    public  List<Pair> FindClosestAlignment(int[] arrTime, int[] arrAlignment)
    {
        List<Pair> list = FindClosestTime(arrTime, arrAlignment);

        List<Pair> reslut = new List<Pair>();
        for (int i = 0; i < arrTime.Length; i++)
        {
            Pair pair = new Pair(arrTime[i], null);
            foreach (var p in list)
            {
                if (pair.Time == p.Time)
                    pair.Alignment = p.Alignment;
            }
            reslut.Add(pair);
        }

        return reslut;
    }

    private  List<Pair> FindClosestTime(int[] arrTime, int[] arrAlignment)
    {
        List<Pair> list = new List<Pair>();

        for (int i = 0; i < arrAlignment.Length; i++)
        {
            int el = arrAlignment[i];
            int index = FindClosestIndexInOrderList(el, arrTime, this.Threshold);
            if (index == -1)
            {
                list.Add(new Pair(null, el));
            }
            else
            {
                list.Add(new Pair(arrTime[index], el));
            }
        }

        return list;

    }

    private  int FindClosestIndexInOrderList(int val, int[] arr, int threshold)
    {
        int index = Array.BinarySearch(arr, val);
        if (index >= 0)
        {//found
            return index;
        }
        else
        {
            //bitwise complement for index
            int compl = (~index);
            if (compl == arr.Length)
            {//val is biggest value in the arr

                if (Math.Abs(arr[arr.Length - 1] - val) > threshold)
                    return -1;
                else
                    return (arr.Length - 1);
            }
            else if (compl == 0)
            {//val is smallest value in the arr
                if (Math.Abs(arr[0] - val) > threshold)
                    return -1;
                else
                    return 0;
            }
            else
            {
                int preIndex = compl - 1;

                int deltaToPrevious = Math.Abs(arr[preIndex] - val);
                int deltaToCurrent = Math.Abs(arr[compl] - val);

                if (deltaToPrevious > threshold)
                    return -1;
                if (deltaToCurrent > threshold)
                    return -1;

                return deltaToPrevious <= deltaToCurrent ? preIndex : compl;
            }
        }
    }
}
```
