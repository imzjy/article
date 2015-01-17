Oracle - The Usage of Rank and Dense_Rank
=====

`Rank`，Oracle提供的一个用来分组排序的函数。

考虑以下基表，该表格是考试成绩表(SC)：

![](http://blog.chinaunix.net/photo/11680_081018135624.gif)

我想知道每个同学的特长科目是什么，即每个同学在所选科目中哪一个科目排第一(成绩最好)。

经分析我们知道这个SQL查询其实是需要实现以下语义：

1. 按学生姓名来分组；
1. 对于每个学生的所有科目成绩进行排序；
1. 取出排序后的最大值所在的记录；

这正好符合`Rank`函数所能完成的功能，我们写出以下SQL：

```sql
SELECT RANK () OVER (PARTITION BY Name ORDER BY Score DESC) AS "rank",
       Name, Course,Score
  FROM sc
```

该SQL查询出的结果为：

![](http://blog.chinaunix.net/photo/11680_081018140055.gif)

可以看到Rank函数按姓名分组(Partition by Name)，然后再按成绩进行排序(Order by Score)。

得到这个结果后，我们可以再对这个结果进行筛选，即可得到我们想要的结果。

```sql
SELECT *
  FROM (SELECT RANK () OVER (PARTITION BY Name ORDER BY Score DESC) AS rk,
    Name, Course, Score
          FROM sc)
 WHERE rk = 1
```

**Dense_Rank**:

我们留意的下SC表，Bily的English成绩和Match的成绩相等。也就是说在对Bily的成绩进行排序时，Bily的Rank为2的数据有两笔，那Bily剩下的一门History的排名应是第三呢，还是第四呢。这个问可以抽象为：

> Bily的成绩排名结果是[1, 2, 2, 4]呢？ 还是[1, 2, 2, 3]呢？

答案是：

如果你用`Rank`,则是[1, 2, 2, 4]，这你从上面的查询结果中可以看出来。

若你用的是`Dense_Rank`则排名结果为[1, 2, 2, 3]。
