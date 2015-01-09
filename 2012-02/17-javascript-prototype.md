JavaScript中的原型继承
==========

下面的理解是错的，只是个笔记。代表我曾经的思考。

学习JavaScript时需要将prototype和__proto__分清，Quora中有一篇解释挺好。

---

对于原型继承我现在仍旧比较模糊，但我感觉这完全不是以前子类，父类似的继承。他们有着完全不同的东西。

原型是一个object，JavaScript中没有类型的概念。 JavaScript中所有的东西除了基本类型，就是object。一个object的原型也是一个object。我们看代码：

 

```javascript
function Person(){};
function Worker(){};
 
var w = new Worker(); 
w.prototype=new Person();   //w(一个object)的原型也是一个object
w.prototype.say = function{alert("hi")}; 
``` 

这里的`say`方法只添加到当前的对象(object)w中(直的吗？这个说法其实是模糊的)，并不影响Worker()这个函数。 所以当

```javascript
var w2=new Worker();
```

并不会有`say`函数的实现。即w与w2是两个独立的object.

如果说w与w2区别就是w对象多了一个say函数？如果这么说的话那`w.prototype.say=function{};`与`w.say=function`区别是什么呢？

我能想到的区别就是`w.say`是给当前object加一个属性，而`w.prototype.say`是给w的原形对象(即通过new Person()创建的一个object)加一个属性。

我们来看一段代码：

```javascript
var w1 = new Worker();    //implicit prototype link 
w1.prototype = new Person();     //explict prototype property
w1.prototype.say = function(){alert('hi')};
 
var w2 = new Worker();
w2.prototype = new Person();
w2.say = function(){alert('hi')};
 
var w3 = new Worker();   //implict prototype link to Worker
 
 
Worker.prototype.say = function(){};  //Worker prototype adding say can be access by w1.w3
Person.prototype.say = function(){};  //explicit prototype, can't be access by w1.w3
```

到目前为止我还是不理解，为什么`w1.say`是`undefined`, `w3.say`确是`function`。

 

我想用图来解释上面一段代码，注意下图中都是对象(object)，没有类，即使函数也是对象（想想JavaScript中内置Function对象）：

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201202/201202171352432673.png)
