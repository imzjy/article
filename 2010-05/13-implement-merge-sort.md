归并排序(Merge-Sort)的C语言实现
===========

归并排序是分治法(Divide-and-Conquer)的典型应用：

- **Divide** the problem into a number of subproblems.
- **Conquer** the subproblems by solving them recursively. if the subproblem sizes are small enough, just sovle the subproblems in a straightforward manner.
- **Combine** the solutions to the subproblems into the solution for the original problem.

对于归并排序，需要考量的是：

- **递**：将待排序数组划分为左边和右边，并对于左边和右边进行递归地排序。直到左边和右边只剩下一个元素——直接求解。
- **归**：递归合并结果得到最终解。

```c
#include "stdafx.h"
#define MAX 99999;
#define SIZE 7
 
void PrintNewLine();
void PrintArray(int arr[]);
void MergeSort(int arr[], int p, int r);
void Merge(int arr[], int p, int q, int r);
 
int _tmain(int argc, _TCHAR* argv[])
{
    int original[] = {6,4,3,1,7,5,2};
    PrintArray(original);
    PrintNewLine();
     
    MergeSort(original,0,SIZE - 1);
    PrintArray(original);
    PrintNewLine();
 
    char wait = getchar();
    return 0;
}
 
void MergeSort(int arr[], int p, int r)
{
    if( r > p )
    {
        //divide&conqurer by recursion
        int q = (p + r) / 2;
        MergeSort(arr, p, q);
        MergeSort(arr, q+1, r);
 
        //combine
        Merge(arr, p, q, r);
 
        printf("Merge(%d,%d,%d) => ",p,q,r);
        PrintArray(arr);
        PrintNewLine();
         
    }
}
void Merge(int arr[], int p, int q, int r)
{
    //calc left side and right side
    int nLeft = (q - p) + 1;
    int nRight = r - q;
 
    int* leftArr = new int[nLeft];
    int* rightArr = new int[nRight];
 
    //copy element to left&right side
    for(int i = 0; i < nLeft; i++)
    {
        leftArr[i]=arr[p+i];
    }
    for(int j=0; j<nRight; j++)
    {
        rightArr[j]=arr[(q+j) + 1];
    }
 
    //sentinel
    leftArr[nLeft] = MAX;   
    rightArr[nRight] = MAX;
 
    //pick the small card in original array
    int i = 0, j = 0;
    for(int k = p; k <= r; k++)
    {
        if(leftArr[i] < rightArr[j])     //sentinel takes effect
        {
            arr[k] = leftArr[i];
            i++;
        }
        else
        {
            arr[k] = rightArr[j];
            j++;
        }
    }
}
 
void PrintArray(int arr[])
{
    for(int i = 0; i < SIZE; i++)
        printf("%d ",arr[i]);
}
void PrintNewLine()
{
    printf("\n");
}
```

**输出**：

```text
6 4 3 1 7 5 2
Merge(0,0,1) => 4 6 3 1 7 5 2
Merge(2,2,3) => 4 6 1 3 7 5 2
Merge(0,1,3) => 1 3 4 6 7 5 2
Merge(4,4,5) => 1 3 4 6 5 7 2
Merge(4,5,6) => 1 3 4 6 2 5 7
Merge(0,3,6) => 1 2 3 4 5 6 7
1 2 3 4 5 6 7
```

递归排序的算法复杂度为：`O(nlgn)`。
