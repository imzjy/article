Oracle - 在查询中使用Decode，Case，NVL进行逻辑判断
================

Oracle提供了一些逻辑判断函数，这些函数可以在查询中使用。

### 1，针对空值进行测试-NVL函数

函数原型为：`NVL(testValue,SubstituteValue)`

常见的用法是

`Select max(score) From SC Where Name='Jerry'`

有时`max(score)`为空，也就是说`Jerry`并没有考试记录，这时我们用"No Record"标注一下：

`Select NVL(max(score),"No Record") From SC;`

还有一个NVL2函数跟其相似，函数原型为： `NVL(testValue,SubValue1，SubValue2)`

NVL2函数实现的是若testValue为NULL，返回SubValue1，否则返回SubValue2。


### 2,更广泛意义上的测试-Decode函数

Decode函数的原型为: `Decode(testValue, if1, then1, if2,then2.....else)`.

针对testValue进行测试，若testValue等于if1则返回then1,若testValue等于if2则返回then2,....若都没有返回，刚返回else.

常见用法是在Oracle中实现行转列(Convert Rows to Columns).

```text
CLASS  COURSE  STUDENT
-----  ------   ------
11  Engish   D
11  Engish   F
11  Engish   E
11  Math     F
11  Math     D
22  Engish   C
22  Engish   B
22  History  A
22  History  B
22  Math     B
22  Math     C
```

我想针对知道11和22班选修`English`, `Math`, `History`各有多少名同学:

```sql
SELECT course, SUM (DECODE (class, 11, 1, 0)) AS "Class-11",
               SUM (DECODE (class, 22, 1, 0)) AS "Class-22"
   FROM studentinfo
   GROUP BY course
```

在这里我们先对class进行测试，若为11，我们返回1，若不是11我们返回0，再对结果进行sum，即可以知道，11班有共有多少同学。再按Course分组，便可以得出：

```text
COURSE   Class-11   Class-22
-------  --------   -----
Engish   3            2
Math     2            3
History  0            2
```

这个解决方案有一个限制就是：你必须预先知道有几个`class`，但若这些`class`是不固定的，那这个解决方案就不适用了。针对此限制，SQL部分不太容易解决，可以在程序中workaround.

比如现在加了一个班级号为33的记录：

```text
33  Match  A
```

在程序中动态构建SQL时在From语言之前加入: `,SUM (DECODE (CLASS, 33, 1, 0)) AS "Class-33")`


### 3，更可读的逻辑测试-Case语句
上面的Decode函数参数数目不定，看上去容易让人迷糊，Oracle提供了另一种语句来实现类似功能，但可读性更高。

如果我们要针对上表的同学栏位进行重命名：

```text
A： Anco
B： Bily
C： Candy
D： Davi
E:  Eve
F:  Fion
```

若我们用Decode可以这样实现：

```sql
SELECT class, course,
       DECODE (student,
               'A', 'Anco',
               'B', 'Bily',
               'C', 'Candy',
               'D', 'Davi',
               'E', 'Eve',
               'F', 'Fion'
              ) AS en_name
  FROM studentinfo
```

同样的也可以用Case语句实现：

```sql
SELECT CLASS, course,
       (CASE student
           WHEN 'A' THEN 'Anco'
           WHEN 'B' THEN 'Bily'
           WHEN 'C' THEN 'Candy'
           WHEN 'D' THEN 'Davi'
           WHEN 'E' THEN 'Eve'
           WHEN 'F' THEN 'Fion'
        END) AS en_name
  FROM studentinfo
```
