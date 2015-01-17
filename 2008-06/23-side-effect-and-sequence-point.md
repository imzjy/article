C/C++中的时序点和副作用
========

C++中的时序点(Seqence Point)和副作用(Side-effect)是两个相关的概念，了解了副作用以后能更好的理解C++上的另一个概念－－时序点。而这两点的理解对于debug和消除代码的歧义(ambiguity)帮助还是比较大的。

## 引子

上周在完成一个类时，对这个类进行了运算符的重载。为了让运算符的重载更加的Intuitive，我在测试代码中写出了这样的语句：

`i = i++;`

就是这条语句引出了本文，Horrible Code!不知你看出这小段代码隐藏了一个错误，简言之，这段代码以对于C以及C++来将产生未定义的结果。

我们可以写代码测试一下，如下

```c++
//Platform: WinXp + VC60
#include <iostream>
using namespace std;
void main()
{
    int i=1;
    int s=0;
    s = i++;
    cout<<s<<endl; //此处s=1

    int j=1;
    j = j++;
    cout<<j<<endl; //此处j=2，what happens?
}
/*
Output:
1
2
*/
```

对于第一个`s`的输出，应该不会有什么让人感到惊奇的。后置(postfix)++操作符在将i的值增1之前，将其右值(right-value)赋给了`s`,故输出1。

但若我们以同样的方式去思考第二个`j`的输出，结果也应该是1才对(`j`在递增之后，又被先前所right-value赋值，最终它的值又成了1)。但实际的输出结果却为2.

其实对于`j`此时是1还是2，对于compiler来说都是对的。此处产生的一个未定义的结果。对于C++中某些操作，C++标准并没有强行定义，而是留给各个compiler自自行决定，比如函数参数的求值顺序。一般情况下这不会有什么问题，但也有时会产生歧义。如`fun(i++,i)`，此时是先执行`i++`还是先执行`i`，各个compiler有其自己的实现。而不同的实现可以产生截然不同的结果。

### Side-effect:

一般的操作符不会令参与计算的变量本身的值发生改变，任何改变操作数(operand)的操作符都会产生副作用。；如：

`s = x + y;`

其中的`+`操作符并不会改变`x`或`y`的值。而C/C++语言的表达式中由于`++`, `--`等运算符的介入，表达式求值(evaluation)可能导致参与计算的变量本身的值发生改变。这便产生了副作用。

并不是所有的副作用都会对程序结果产生影响，(注，`=`就是故意利用副作用来改变操作数`s`的值。我们将`=`产生副作用忽略)：

`s = (i++) + (j++);`

这段代码产生了两个副作用，分别是`i++`和`j++`。但无论是先执行`i++`，或是先执行`j++`对程序结果并不产生影响。结果都是和`s = i+j`相等。但若我们的运算结果受副作用的执行顺序影响的话，问题就来了。比如：

`s = i + (i++);`

先执行`i`，还是先执行`i++`，(也就是先执行副作用，还是后执行副作用)，运算结果将截然不同。

C++为了确定一段语句的执行顺序，引入了时序点(Sequence Point)。

### Sequence Point:

**时序点的定义**:

> At certain specified points in the execution sequence called 'sequence points', all side effects of previous evaluations shall be complete and no side effects of subsequent evaluations shall have take place.

一个时序点，被定义为程序执行过程中的这样一个点：该点前的表达式的所有副作用，在程序执行到达该点之前发生完毕；该点后的表达式的所有副作用，在程序执行到该点时尚未发生。

对于一段C++代码，C++编译器在编译时将其划分为一个个的box，然后将顺序执行，也就是说对于如下语句块：

```c++
{
  ++x;
  ++y;
}
```

将产生一个这样的执行序列：

![](http://blog.chinaunix.net/photo/11680_080623170317.gif)

其中红色的圆点标出了三个时序点，分别为A，B和C。我们拿时序点B来讲解，其它的也是一样的。在运行到B点时，A-B所产生的副作用(++x产生的副作用)发生完毕。B-C产生的副作用还未发生。而在**两个时序点之间的副作用的执行顺序是未定义的**。

也就是说如果在两个时序点之间有两个或者多个副作用，那么这些副作用的时序是不定的。如果表达式的值依赖于这些副作用间的顺序，那么表达式的值也就是不定的。

那C++的编译器怎么决定是否产生一个时序点呢？ C++中将时序点放置在以下位置：

1. The point of calling a function, after evaluating its arguments.
2. The end of the first operand of the && operator.
3. The end of the first operand of the || operator.
4. The end of the first operand of the ?: conditional operator.
5. The end of the each operand of the comma operator.
6. Completing the evaluation of a full expression. They are the following:
  - Evaluating the initializer of an auto object.
  - The expression in an "ordinary" statement—an expression followed by semicolon.
  - The controlling expressions in do, while, if, switch or for statements.
  - The other two expressions in a for statement.
  - The expression in a return statement.

让我们拿两条语句来分析一下，先来个简单点的：

`f = a + b;`

根据第6条的第2点，我们可以知道一个典型的以“;”结束的一条语句之后会插入一个时序点。再如：

`if(a>b) n=5;`

根据第6条的第3点，在`a>b`之后会插入一个时序点。

### 回到问题

让我们回到最初的问题，若我们写出了类似以下的语句，都将会出再未定义的行为：

```c++
x[i] = i++;
f = (i++) + i;
fun(i,i++);
i = i++;
```

对于函数的嵌套调用也可能产生副作用，如：

`fun(methodA(),methodB());`

`methodA`和`methodB`也可能产生副作用，这取决于它们是否直接(或间接)更改了对方或是`fun`所要访问的变量.

这些语句都有这样的共同特点:

1. 语句中包括产生副作用的操作符(或操作).
2. 程序运行结果依赖于产生副作用语句的执行顺序。

感谢chg.s及其在论坛上的帖子：http://www.chinaunix.net/jh/23/310576.html

----

相关参考：

1. http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1188.pdf
1. http://publications.gbdirect.co.uk/c_book/chapter8/sequence_points.html
1. http://msdn.microsoft.com/en-us/library/azk8zbxd(VS.80).aspx
