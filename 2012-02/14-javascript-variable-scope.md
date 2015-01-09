Javascript中的变量作用域
=====

以下内容是我看《Javascript内核》这本书学到的。

1. Javascript变量作用域为（整个）函数体内有效，没有块作用域。
2. Javascript的函数是在局部作用域内运行的，在局部作用域运行的函数体可以访问其外层的变量和函数。
3. Javascript的作用域为词法作用域。词法作用域是指：其作用域在定义时（词法分析时）就确定下来的，而并非在执行时确定。

 

作者有一个极好的例子：

```javascript
var str = "global";
 
function scopeTest() {
    alert(str);
    var str = "local";
    alert(str);
}
 
scopeTest();
```

你也许会认为这断程序的运行结果是：

```text
global
local
```

那你就错了，真正的结果是：

```text
undefined
local
```

因为在函数scopeTest的定义中，预先访问了未申明的变量str，然后才是对str的初始化，所以第一个str会返回undefined错误。

那为什么函数这个时候不去访问外部的str变量呢？这是因为，在词法分析结束后，构造作用域链的时候，会将函数内定义的var变量放入该链，因此str在整个函数scopeTest内都是可见的（从函数的第一行到最后一行），由于str变量本身是未定义的，程序顺序执行，到第一行就会返回未定义。第二行将str赋值，所以第三行str将返回local。

换种说法上面的代码也等价于：

```javascript
var str = "global";
 
function scopeTest() {
    var str; 
    alert(str);
    str = "local";
    alert(str);
}
 
scopeTest();
```
