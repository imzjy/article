Oracle - Table Joining Query Explanation
==================

表的连接查询在做报表分析的时候时常会用到，而且本身连接查询要实现的【现实抽象】也很明了，在两个(或多个)表中相互参考（Reference），找出对自己有用的信息。

因为SQL语言是DSL(Domain-Specific Language)所以，要实现这个功能也很直观，本文试图用极其简单的方式向你描述表的连接查询，及其连接查询想要实现的【现实抽象】。

可以将`ID`看作员工的工号，`a`表看作个人信息表，`b`表是工作分配表。

```text
select * from a;
ID         NAME
---------- ----------
2006  Anco
2007  Jerry
2008  Zero

select * from b;
ID         DEPT
---------- ----------
2006  MIS
2007  MES
2009  DEV


select * from a [inner Join] b                [(内)连接,笛卡尔积]
select * from a [inner join] b on a.name =‘Anco’ [等值连接，笛卡尔积后选取满足特定条件的列]


select * from a,b where a.id=b.id;            [自然连接,公共属性相等,公共属性只取一份（特殊等值连接）]
ID         NAME       ID_1       DEPT
---------- ---------- ---------- ----------
2006  Anco   2006  MIS
2007  Jerry  2007  MES


select * from a left join b on a.id=b.id;     [左外连接,左表为基表]
ID     NAME     ID_1    DEPT
----   -----    -----   ----------
2006   Anco     2006  MIS
2007   Jerry  2007  MES
2008   Zero   [NULL]  [NULL]


select * from a right join b on a.id=b.id;    [右外连接,右表为基表]
ID         NAME       ID_1       DEPT
---------- ---------- ---------- ----------
2006  Anco   2006  MIS
2007  Jerry  2007  MES
[NULL]  [NULL]  2009  DEV


select * from a full join b on a.id=b.id;     [保留左,右表的异同部分]
ID         NAME       ID_1       DEPT
---------- ---------- ---------- ----------
2006  Anco   2006  MIS
2007  Jerry  2007  MES
2008  Zero   [NULL]  [NULL]
[NULL]  [NULL]  2009  DEV
```
