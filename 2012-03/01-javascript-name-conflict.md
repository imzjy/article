JavaScript中变量名重名
=======

今天看到园子里的[一篇文章](http://www.cnblogs.com/snandy/archive/2012/03/01/2373237.html)，进的是变量名的重名问题，我们直接来看代码:

```javascript
var a;
function a() { 
}
alert(typeof a);
```

这里alert的结果是function。但如果我将代码改一行，声明之后立即assign a value:

```javascript
var a=1;        // 注意变化，声明后立即赋值
function a() {
}
alert(typeof a);
```

这时输出的却是number，为什么？博主的解释并不在理，他的意思是`var a=1;`被解释成：`var a; a=1`。解释没错，但没能解释为什么第二个代码输出是number。

我们还可以将代码再变化一下：

```javascript
var a=1; 
a = function () {   //注意变化
}
alert(typeof a);
```

经过思考，我的理解是：`function foo(){}`**这种形式的函数声明是在词法解析(lexical analysis)时就可以确定的**，也就是说跟var a;类似这种变量及定义都可以在词法解析时确定。换个说法就是这些都是静态可以确定的。

而JavaScript是动态语言，他的变量只是一个引用而已，可以在运行时(runtime)指向任何类型实体。所以变量的类型也是运行时变化的，我们可以通过例子看一下：

```javascript
var a=1; 
console.log(typeof a);
 
a = function() { 
}
console.log(typeof a);
 
a = "";
console.log(typeof a);
```
