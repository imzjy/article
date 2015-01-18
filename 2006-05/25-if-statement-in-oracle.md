PL/SQL_选择结构
=====

控制语句几乎是所有面向过程语言的核心，PL/SQL也是一程过程化语言，学好PL/SQL，掌握PL/SQL中几种控制语句的语法是必不可好的。

PL/SQL和其它过程化语言一样，主要有三种结构控制语句，他们分别为：

1. 顺序结构；
2. 选择结构；
3. 循环结构；

顺序结构比较简单了，我们在写PL/SQL时多注意一下实际需要就行了。我们先来看看选择结构。

选择结构语法：

主要有`IF判断`和`CASE判断`;

### 1,IF判断

**第一种**

```sql
if conditional then        --条件为真执行statment
  statement                --条件为NULL或否时执行 end if 以后的语句
end if;
```

**第二种**

```sql
if conditional then    --条件为真执行statement1
  statement1           --条件为NULL或否时执行statement2
else
  statement2
end if;
```

**第三种**

```sql
if conditional1 then    --先判断条件1
  statement1            --若为真执行statement1
elsif conditional2 then --再判断条件2
  statement2            --若为真执行statement2
  ......
  ......
else                    --若以上条件都为NULL或否
  statementn            --执行statementn
end if;
```

### 2,CASE判断

```sql
case conditonal                --需要检测的表达式
  when decision1 then statement1   /*若上面的表达式值等于decision1执行statement1*/
  when decision2 then statement2   /*若上面的表达式值等于decision2执行statement2*/
  ......
  ......
  when decisionN then statementN   /*若上面的表达式值等于decisionN执行statementN*/
  else  statementN+1               --若没有匹配的decision执行statementN+1
end;
```

注意：CASE语句中conditional和decision的数据类型必须一致，或相互兼容。

**选择结构中NULL值的判断**：

在选择结构中需要注要一点的就是NULL值的判断，因为有时我们没有注意NULL值的判断会导致出现相反的结果。我们看以下两个procedure,他们都可以判断`v_num1`是否大于`v_num2`。

```sql
PROCEDURE CHK_NUM_1 (
              p_num1 in number,
              p_num2 in number,
              p_result  out varchar2
)
IS
     v_num1   number(2);
     v_num2   number(2);
     v_result varchar2(10);
BEGIN
  v_num1:=p_num1;
  v_num2:=p_num2;

  if v_num1>v_num2 then
    v_result:='YES';
  else
    v_result:='NO';
  end if;
p_result:=v_result;
dbms_output.put_line('the result is'||p_result );
END;

/* --splitter-- */

PROCEDURE CHK_NUM_2 (
              p_num1 in number,
              p_num2 in number,
              p_result  out varchar2
)
IS
     v_num1   number(2);
     v_num2   number(2);
     v_result varchar2(10);
BEGIN
  v_num1:=p_num1;
  v_num2:=p_num2;

  if v_num1<v_num2 then
    v_result:='NO';
  else
    v_result:='YES';
  end if;
p_result:=v_result;
dbms_output.put_line('the result is'||p_result );
END;
```

在逻辑上，chk_num_1和chk_num2一样，只不过是换个表示方法。

例如：现在我们令

```text
p_num1 = 5;
p_num2 = 3;
```

无论你用`chk_num_1`，还是`chk_num_2`得出的结果都是"YES".

但如果令：

```text
p_num1 为空;(即为null)
P_num2 = 5;
```

则会出现两种不同的结果,`chk_num_1`为"NO",而`chk_num_2`为"YES".

导致这种情况出现的原因是无论NULL和一个数的比较结果仍为NULL(`NULL>5 = NULL`)

因些会执行else以后的语句，而上面两个procedure判断顺序又不一样，所以出现了以上的两种结果。

**解决方法**：

在判断之前先判断一下是否有NULL值，将上面判断部分加上一段：

```sql
if p_num1=null or p_num2 null then
  v_result:="parameter is NULL!";
if v_num1>num2 then
    v_result:='YES';
  else
    v_result:='NO';
```

加上上面的判断无论是`chk_num_1`或是`chk_num_2`都可以正确判断`p_num1`和`p_num2`的大小。
