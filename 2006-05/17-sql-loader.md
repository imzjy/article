oracle学习_Sql loader使用
=====

昨天看了一下oracle中数据的导入方法，在oracle中数据导入方法主要有以下几种：

### 1，直接用insert ......values()语句；**

example:

`insert into book(no,name,type) values('2006001','basketball park','magazine')`

### 2，use select query sentence;

example:

`insert into book_1 select * from book2 where book1='condition'`

### 3,use PL/SQL procedure;

example:

```text
SQL>edit input_example.sql
-----------input prompt
accept p_no prompt 'please input book no'
accept p_name prompt 'please input book name'
accept p_type prompt 'please input the type of book'
------------evaluation
declare
v_no book.no%type:=&p_no;
v_name book.name%type:=&p_name;
v_type book.type%type:=&P_type;
-------------insert
begin
insert book(no,name,type)
values(v_no,v_name,v_type);
commit work;
end;
```

### 4,使用 Oracle Loader插入记录

这裡重点讲一下Oracle Loader的使用，很多时候我们会使用Oracle Loader进入资料的导入工作。像在工厂裡我们要把别的机器或是人为的资料档导入Oracle通常我们会使用Oracle Loader.

再一说来，oracle loader其实也是一个较为自动的导入工具。

比如现在别人给我们图书馆1000本书，并用e-mail给了我们一个清单。清单是用一个*.txt，内容如下：

```text
#bookname,bookno,bookqty,booktype,intime,price
#书名,书号,书的数量,书的类型,加入时间,价格
C语言程序设计,001,13,课本,20060521,20.45
oracle学习与提高,002,15,课外书,20060522,45
...........
...........
...........
```

如果这个清单有十几条，我们完全可以用手工insert但是如果是一千条那我们用手工就太慢了，而且容易出错，这时我们就可以使用oracle Loader.

**sql loader 的例子**

```text
c:\sqlldr userid=bookadm1/sysadm control=input.ctl log=input.log bad=input.bad errors=30 skip=1 direct=true

sqlldr是 oracle loader的命令，后面跟的是参数，参数控制著具体的导入方法，参数解释如下：
userid=bookadm1/sysadm  --username='bookadm',password='sysadm'
control=input.ctl       --control file name input.ctl
log=input.log           --log file name input.log
bad=input.bad           --when input error to take down error record 
errors=30               --permit error rows
skip=1                  --skip rows
direct=true             --use direct directory
```

其中`input.ctl`是控制著输入数据文件的格式。

control file

```text
load data                              --关键字，指出这是一个控制文件。
infile 'd:\book\200605.txt'            --要导入的文件的位置及文件名
append(insert,replace) into table book --向BOOK的表中追加(append)（插入一个空表(insert),替换一个表(replace原表内容将被删除)）
fields terminated by ','               --两个字段间的分隔符
（bookname char,
bookno   number,
bookqty  number,
booktype char,
intime date 'yyyymmdd'
price  number(6,2)
）                                     --定义列对应的顺序
```