JavaScript中的函数上下文和apply,call
=============

下面内容摘抄自《JavaScript内核》。

-----

在Java或者C/C++等语言中，方法(函数)只能依附于对象而存在，不是独立的。而在JavaScript中，函数也是一种对象，并非其他任何对象的一部分，理解这一点尤为重要，特别是对理解函数式的JavaScript非常有用，在函数式编程语言中，函数被认为是一等的。

函数的上下文是可以变化的，因此，函数内的this也是可以变化的，函数可以作为一个对象的方法，也可以同时作为另一个对象的方法，总之，函数本身是独立的。可以通过Function对象上的call或者apply函数来修改函数的上下文：

call和apply通常用来修改函数的上下文，函数中的this指针将被替换为call或者apply的第一个参数，我们不妨来看看2.1.3小节的例子： 

```javascript
//定义一个人，名字为jack
var jack = {
    name : "jack",
    age : 26
}
//定义另一个人，名字为abruzzi
var abruzzi = {
    name : "abruzzi",
    age : 26
}
//定义一个全局的函数对象
function printName(){
    return this.name;
}
 
//设置printName的上下文为jack, 此时的this为jack
print(printName.call(jack));
//设置printName的上下文为abruzzi,此时的this为abruzzi
print(printName.call(abruzzi));
 
print(printName.apply(jack));
print(printName.apply(abruzzi));
```

只有一个参数的时候call和apply的使用方式是一样的，如果有多个参数：

```javascript
setName.apply(jack, ["Jack Sept."]);
print(printName.apply(jack));
setName.call(abruzzi, "John Abruzzi");
print(printName.call(abruzzi));
```

得到的结果为： 

```text
Jack Sept. 
John Abruzzi
```

apply的第二个参数为一个函数需要的参数组成的一个数组，而call则需要跟若干个参数，参数之间以逗号(,)隔开即可。
