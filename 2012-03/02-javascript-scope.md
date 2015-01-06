JavaScript作用域
=========

以下是笔记和自己理解，不一定正确。

----

JavaScript的作用域主要有以下特征：

1. 词法作用域(Lexical Scope)和函数作用域(Function Scope & Local Scope)。这是JavaScript的静态的特征，很多问题都是由此引起的。我的理解Hoisting也是由此造成。
2. 作用域链(Scope Chain)和执行上下文(Execution Context)。这是JavaScript的动态特征。

### 1，词法作用域(Lexical Scope)和函数作用域(Function Scope & Local Scope)
这是JavaScript静态的特征，也是词法分析时的特征。在执行前进行词法分析时，就可以将变量的作用域确定下来。JavaScript的function很神奇，这里也会用作词法分析的时作用域的单位。即函数内都是一个Scope，函数外是一个Scope。

### 2，作用域链(Scope Chain)和执行上下文(Execution Context)
当你调用一个函数时会创建一个执行上下文，被调用函数再去调用另一个函数时，又会创建一个执行上下文。比如：

```javascript
function a(){
    function b(){
    }
    b();
}
a();
```

首先JavaScript引擎会创建一个Global EC(Executioln Context)，当你a()调用函数a的时候会创建一个EC，当你在a的内部调用b()的时候又会创建一个EC。这是一个函数调用栈的结构。即 Global EC->a EC –>b EC。

每个EC中会关联一些对象：变量对象(Variable Object,记录函数同级内定义的变量)，活动对象(Active Object记录函数内及函数参数变量)。而这些对象构成了作用域内可查找的对象。还有一个对象就是作用域对象(Scope Object)，它记录了函数运行时引用到其父作用域的变量——这也是Closure的产生原因。

JavaScript静态决定了变量的作用域，并在调用(动态)时创建Execution Context，其中通过Variable Object，Active Object，Scope Object包含引用的变量。而Scope Object保存了当前函数引用其外部函数的变量(通过Lexical Analysis很早有就可以决定了)——这构成了闭包本身。

具体的实现可能是写时复制(Copy-On-Write)，当引用一个变量，JavaScript引擎先在当前EC的作用域中查找变量定义及当前值。如果找不到，再去上一级EC中查找，直到Global EC。这也就是作用域的查找，其本质也就是栈的递归。当需要修改别的EC中变量时，将该变量复制到当前EC的作用域对象(Scope Object)中。换个说法Scope Object中保存的都是当前函数用到的变量的“引用”，只有需要改变该Scope Object中变量的时候才去：

1. copy一份。
2. 改变变量值。
3. 保存在当前EC的Scope Object中。
