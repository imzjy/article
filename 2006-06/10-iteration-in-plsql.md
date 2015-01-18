PL/SQL_循环结构
=======

PL/SQL的循环结构和别的语言也是大同小异。

在循环结构中可以分为四小类：

1. 先循环，再判断；
2. 先判断，再循环；
3. 已知循环次数的循环；
4. 无条件转向；

### 第一类：先循环，再判断；

**说明**：该类循环特点是，先执行一次循环，再去判断是否继续循环下去。无论后面的判断是否为true，循环体总要执行一次。

**语法**：

```sql
loop
  circulation statements;    ----循环体；
  if conditional then
  exit;                      ----退出循环体标志
end loop;
```

或

```sql
loop
  circulation statements;    ----循环体；
  exit when conditional;     ----当when后的判断为真时退出循环体
end loop;
```

**示例**：

```sql
LOOP  ---start loop
  dbms_output.put_line(varient); ------circulation structure

  if varient=num then ---------if conditional is true
  exit;               ---------it will execute exit the loop
  end if;

  varient:=varient+1;  ----此点注意，要是不加会形成死循环，造成buffer overflow

end loop;  ---end loop
```

或

```sql
LOOP       ---start loop
  dbms_output.put_line(varient); ------circulation structure

  exit when varient=num;
  varient:=varient+1;
end loop;  ---end loop
```

### 第二类：先判断，再循环；

**说明**：这类循环特点是，先判断条件，若为真才执行循环，若为假则跳出循环。

**语法**：

```sql
when conditional loop   -----为真时，再执行循环体
circulation statements; ----循环体；
end loop;
```

**示例**：

```sql
while varient<num LOOP
  dbms_output.put_line(varient);
  varient:=varient+1;
end loop;  ---end loop
```

### 第三类：已知次数的循环；

**说明**：该类循环最好用在已知次数的循环中，但也不尽然。比如下面语法中的start和end既可以是固定的数字，也可以是变量。比如 `for var in 1..5`,执行5次，还可以是`for var in 1..v_booknum`

**语法**：

```sql
for var in start..end loop  ----var表示已定义过的变量，从start开始循环至end
  circulation statements;  ----循环体；
end loop;
```

**示例**：

```sql
for varient in 0..num loop
  dbms_output.put_line(varient); ------circulation structure
end loop;  ---end loop
```

### 第四类：无条件转向；

**说明**：该类循环并不常用，也不推荐使用，这种循环很难控制。通常我们都用以上的循环来代替。

**语法**：

```text
<<mark>>                  ---设置跳转的标记
circulation statements;   ---循环体
goto mark;                ---跳转到上面的mark处
```

**示例**：

```text
<<circuit>>
  dbms_output.put_line(varient); ------circulation structure
  varient:=varient+1;
  if varient<num then ---------if conditional is true
goto circuit;
  end if;
```

PL/SQL循环语句的注意点：

1. 根据实现需要来选择，是先要判断，还是先要循环。
2. 应注意变量的自增或自增，以防造成死循环。
3. 有用到GOTO语句的尽量用其它语句来实现。
