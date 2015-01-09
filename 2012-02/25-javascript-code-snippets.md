JavaScript代码片段
=======

### 1，模版替换（跟Crockford学的）

```javascript
var template = '<table border="{ border }">' +
    '<tr><th>Last</th><td>{ last } </td></tr>' + 
    '<tr><th>First</th><td>{ first }</td></tr>' +
    '</table>'
 
var data = {
    first: 'Jerry',
    last: 'Chou',
    border: 2
}
 
mydiv.innerHTML = template.supplant(data);
 
//实现
if(typeof String.prototype.supplant !== 'function'){
    String.prototype.supplant = function (o){
        return this.replace(/{ ([^{}]) }/g,
            function(a, b){
                var r = o[b];
                return typeof r === 'string' ? r : a;
            }
    }
}
```

### 2,模拟块作用域(Block Scope)

我们知道在JavaScript中没有作用域(block scope)，所有函数体内定义的变量都会被hoisting(即提到函数的顶部)。为了模拟类似C/Java/C#语言中的块作用域(block scope)，我们可以使用以下代码片段。这也是我们看别人写的类库比如JQuery时常见到的形式——定义后立即调用。

```javascript
(function(){
    //bla..bla
}());
```

比如下面的代码使用该技术模拟了一个块作用域：

```javascript
function foo() {
    var x = 1;
    if (x) {
        (function () {
              var x = 2;
              // some other code
        }());
    }
    // x is still 1.
}
```

至于为什么定义了一个函数作用域就立即调用？因为函数的定义并不会执行函数体上的代码，当们在函数定义后加上()，进行调用时，才会执行函数体内的代码——更严谨的说法是：函数在调用时(加上”()”)才会创建执行环境(Execution Context)。

---
参考

[[翻译]JavaScript Scoping and Hoisting](http://www.cnblogs.com/betarabbit/archive/2012/01/28/2330446.html)
