TO_DATE使用详解
=======

时常使用`to_date`函数来查询特定时间内的资料。

但每次都是用别人写好的语句再改一下日期，一直对`to_date`函数的格式不太了解。今看了oracle的书上面`to_date`函数讲的比较好。

**语法**：

`to_data(date&time,format)`

其中第一个参数date&time是我们要查询的具体日期和时间，比如：2006年5月21日。但是这个时间也分为很多种精度的，比如：

```text
2006年5月21日
2006年5月21日17：24
2006年5月21日17：34分55秒
```

这个精度要根据实际情况来定。

另外一个参数format决定的日期的表示方法，比如：

`2006年5月21日`可以表示为：060521、20060521、2006FEB21等等

而他们对应的format为:

```text
060521        YYMMDD
20060521      YYYYMMDD
2006FEB21     YYYYMONDD
```

示例：

`select * from book where intime=to_date('2003/02/17/17/53/55','YYYY/MM/DD/HH24/MI/SS')`

上面的语句是查询：2003年8月17日下午5点53分55秒，入库的书本。

其实用下面的写法也是可以的

```sql
select * from book where intime=to_date('20030217175355','YYYYMMDDHH24MISS')
select * from book where intime=to_date('2003-02-17-17-53-55','YYYY-MM-DD-HH24/-I-SS')
```

中间的连字符`/`、`:`或`-`，并不影响表达，只是为了更加容易看清楚。

表示年份有以下几种格式，及这种格式对应的表达方法：

```text
2003年为例
YYYY        2003
YYY          003
YY            03
```

月份表示格式及表达方法：

```text
二月分为例
MM          08
RM          IIX(罗马数字)
MONTH       february
MON         feb
```

日期的格式及表达方法：

```text
17号为例
DDD         76          2月的17日在本年度(不是闰年的情况)是多少天
DD          17          在本月中是号(17号)
D           在这一个星期是哪天
```

星期的格式和表示方法：

```text
星期一为例
DAY         monday     全名显示
DY          mon        缩写
```

小时的格式和表示方法：

```text
HH24      18    二十四小时制
```

分钟的格式和表示方法：

```text
MI        32    该小时32分钟
```

秒的表示方法:

```text
SS        28    该分钟28秒
```


既然知道格式和表示方法就简单了，比如我想知道在:

`2005年12月15日18时21分08秒` 至 `2006年 2月23日19时00分00秒`

共入库多少书本我们就可以用以下语句

```sql
SELECT SUM(QTY)
FROM BOOK
WHERE INTIME BETWEEN TO_DATE('2005/12/15-18:21:08','YYYY/MM/DD-HH24:MI:SS')
  AND TO_DATE('2006/02/23-19:00:00','YYYY/MM/DD-HH24:MI:SS')
```

具体使用什麽样的格式就要看我们的需要和使用习惯了，但这并不影响结果