插入排序-C实现中的几点问题记录
========

昨晚看《算法导论》，其中有一个举例是插入排序。上午我用C语言实现了该算法。本来以为自己理解了昨晚所看的算法，谁知实现的时候还是出现了些问题。我们在学习时会遇到这样的现象：

`你以为自己会了，潜意识里认为只要懂了原理花些时间就可以搞定。`

所以我们看书时大多只关注原理。这样本身也没有什么不好，因为人的大脑有限，每天思考也不能过于长，否则容易分神。而记住原理忽略细节可以是大脑的一种自我保护机制。同时这也是一个陷阱，我们时常以为自己理解了却没有验证这种理解，这种理解往往在运用时会出现一些问题，显得不太可靠。

### 第一次实现

经过思考，我用C语言实现了插入排序：

```c
#include "stdafx.h"
#define SIZE 7
 
void PrintNewLine();
void PrintArray(int arr[]);
void InsertionSort(int arr[]);
 
 
int _tmain(int argc, _TCHAR* argv[])
{
    int original[] = {2,5,3,1,4,7,6};
    PrintArray(original);
    PrintNewLine();
 
    InsertionSort(original);
 
    PrintNewLine();
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
void PrintNewLine()
{
    printf("\n");
}
 
 
void InsertionSort(int arr[])
{
    for(int i=1; i < SIZE; i++)
    {
        int key = arr[i];
        while(key < arr[i-1] && i > 0)    //i>0 role as Termination
        {
            //Exchage key and element which postion at key-1
            arr[i] = arr[i-1];
            arr[i-1] = key;
 
            //Due to key advanced, so key's previous element will be compared next.
            i--;
        }
        PrintArray(arr);
    }
}
```

**输出如下**：

```text
2 5 3 1 4 7 6
 
2 5 3 1 4 7 6
2 3 5 1 4 7 6
2 3 5 1 4 7 6
1 2 3 5 4 7 6
1 2 3 5 4 7 6
1 2 3 5 4 7 6
1 2 3 5 4 7 6
1 2 3 4 5 7 6
1 2 3 4 5 7 6
1 2 3 4 5 7 6
1 2 3 4 5 6 7
1 2 3 4 5 6 7
 
1 2 3 4 5 6 7
```

**问题**

通过每次迭代的结果可知，上面的InsertionSort方法中有一个缺陷。算法的迭代次数远远超出了预计。导致这个原因的是：我们在内层while循环中对迭代子i的操作，影响到外层的for循环中的i取值。这样每次迭代外层循环都是从下标1开始。而从下标1开始会重复迭代那些已经排序好的元素。

其实简单些讲，这个是常见编程陷阱即：命名冲突(Naming Conflict)

### 第二次实现

要解决这个问题，并不是很难，我们引入一个内层while循环专用的迭代子j，代码如下：

```c
void InsertionSort(int arr[])
{
    for(int i=1; i < SIZE; i++)
    {
        int key = arr[i];
 
        int j = i;
        while(key < arr[j-1] && j > 0)    //i>0 role as Termination
        {
            //Exchage key and element which postion at key-1
            arr[j] = arr[j-1];
            arr[j-1] = key;
            //Due to key advanced, so key's previous element will be compared next.
            j--;
        }
         
        PrintArray(arr);
    }
}
```

**输出如下**：

```text
2 5 3 1 4 7 6
 
2 5 3 1 4 7 6
2 3 5 1 4 7 6
1 2 3 5 4 7 6
1 2 3 4 5 7 6
1 2 3 4 5 7 6
1 2 3 4 5 6 7
 
1 2 3 4 5 6 7
``` 

**问题**

由输出我们可以看见，命名冲突问题已经解决。我们外层循环一共执行了n-1次(n为需排序元素个数，此处为7)。但这个实现跟算法导论上的实现还是有一些不同。我的实现将每次待排序的元素Key跟Key前面的元素进行交换。而算法导论上的实现更加严谨：先移动元素，待元素移动好了，再将Key插入适当的位置。

每次都移动Key并不是必要的，必要的移动只是最后一步，即：将Key移动到适当的位置。

这个在实现上的区别就是将一条语句从内层循环移动至外层循环。

### 第三次实现

```c
void InsertionSort(int arr[])
{
    for(int i=1; i < SIZE; i++)
    {
        int key = arr[i];
 
        int j = i;
        while(key < arr[j-1] && j > 0)    //i>0 role as Termination
        {
            //move key to previous position
            arr[j] = arr[j-1];
            j--;
        }
        arr[j] = key;   /*将key的赋值从内层循环移动至外层循环*/
 
        PrintArray(arr);
    }
}
```
