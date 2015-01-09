理解JavaScript中原型继承
=====

### 1，解决上篇的问题先

前面一篇文章，我发了一堆的牢骚，想来也是很愚蠢的，只是被JavaScript搞的头疼，不爽而已。像许多东西你不懂的时候以为他是屎，当你懂了时候才知道他是宝。

书也是读第二遍的时候才能懂，08年能就读了爱民的《[JavaScript语言精髓与编程实践](http://book.douban.com/subject/3012828/)》，而且也通读了语言精髓的部分，而且还和他通邮件聊了一点。不过当前我也没有读懂，我在书上有所记录。

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201202/201202251147156453.png)

现在看来Crockford的《[JavaScript:Good Parts](http://book.douban.com/subject/3590768/)》中说的也对JavaScript确实有比较狗屎的地方，当然瑕不掩玉，JavaScript确定有着另人吃惊的能力。先来解决上篇的问题，我们再看看上篇的代码：

```javascript
function Shape(){
  this.area = function(){};
}
   
function Point(){
  this.x = 0;
  this.y = 0;
}
   
var p = new Point;
  
//为啥是undefine,因为instace没有prototype属性，prototype对于p来说只是一个普通地跟p.val一样是一个undefined的属性。
console.log(p.prototype);  
    
//为啥又是指向Point的function,因为p没有constructor，只有Point.prototype有，通过原型查找，即p.constructor == Point.prototype.constructor == Point;
console.log(p.constructor);
console.log(p.constructor == Point.prototype.constructor);  
console.log(p.constructor == Point);
   
console.log("-----------------------------");
   
p.prototype = new Shape();
console.log(p.area);          //为啥又是undefine，不是设置了原型对象嘛，我操。
//var p = new Point;做了下面三步：p={}; p.__proto__=Point.prototype=new Object(); Point.apply(p);
//也就是说p的原型已经确定是new Object()，即一个空对象。 
   
Point.prototype = new Shape();  //设置原型
console.log(p.area);          //TMD还是不行，我设置了类型的原型对象啊。p中没有area属性，p的原型new Object()中也没有area属性，当然就是undefined，无比的正确
   
Point.prototype.area = function(){};
console.log(p.area);          //你妈，为什么啊。同上，p的原型在定义时已经确定就他妈的是一个空对象
   
var p2 = new Point;
console.log(p2.area);         //我操，这时又可以了@#￥%……&*（
//var p2 = new Point;的工作过程：p2={},p2.__proto__=Point.prototype=new Shape();Ponit.apply(p2);
//关键是第27行我们已经设置了Point.prototype这个原型为new Shape();
  
Point.prototype.val = 10;
console.log(p2.val);         //这下好理解了，p2中未定义val，这时去原型Point.prototype中找，找到了为10.
 
Shape.prototype.val2 = 20;
console.log(p2.val2);       //p2中没有val2，去Point.prototype(即new Shape())中找,new Shape()的__proto__为Shape.prototype，终于找到了。
```

### 2，一些JavaScript的总结

先谢谢博客园的[汤姆的一张图](http://www.cnblogs.com/TomXu/archive/2012/01/12/2308594.html)：

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201202/201202251147176189.png)

#### 2.1 JavaScript中函数也是对象

如果感觉这不好理解，看下面的代码

```javascript
//函数第一种写法，更能看出函数也是obj
var f1 = function Point(){
    this.x = 0;
    this.y = 0;
}
 
//函数第二种写法，与上面等效
function f1(){
    this.x = 0;
    this.y = 0;
}
```

除此之外，函数的原型是`f1.__proto__ == Function.prototype; Function.__proto__ == Object.prototype; Object.__proto__ = null;`

 

#### 2.2 利用new 构造函数()来创建对象做了些什么

比如 var p = new Point();这句话做下以下工作：

```javascript
var p = {};
p.__proto__ == Point.prototype;    //很关键的一步，原型继承来自于这里
Point.apply(p);
```

刚才看Crockford的视频，看到了new的JavaScript实现：

```javascript
function new(func,arguments){
    var that = Object.create(func.prototype);   //创建一个对象，并将期__proto__设置为func.prototype指向的object instance.
    result = func.apply(that, arguments);
    return (typeof result === 'object' && result) ||  that;
}
``` 

#### 2.3 一些注意点

- 只有构造器有prototype属性，即Point.prototype。prototype是(指向)一个实例(instance)
- 实例中有__proto__属性，即p.__proto__;原型回溯时就通过些属性。
- p.prototype只是p的一个普通属性。系统没有对此有约定和特殊照顾。
- 构造器.prototype.constructor指向构造器自身，即Point.prototype.constructor == Point;
- p.constructor == Point.prototype.constructor == Point;

 
#### 2.4原型链的维护

如果你不想通过公开属性比如constructor来回溯整个原型链，你不用考虑太多。

但若你想回溯，就必须留心了。比如

```javascript
function MyObject(){};
function MyObjectEx(){};
 
MyObjectEx.prototype = new MyObject(); //这句话会使得下面成立
 
var o = new MyObjectEx();
console.log(o.constructor == MyObject);   //我们在建立原型链时，将constructor指向打乱了。
 
//解法1
MyObjectEx.prototype = new MyObject();
MyObjectEx.prototype.constructor = MyObjectEx;  //手动修改constructor指向
 
//上面解法的问题是MyObject.prototype.constructor其实应该指向MyObject这样才能完成原型回溯，这便有了解法2
 
//解法2
function MyObjectEx(){
    this.constructor = arguments.callee;
   //Or, this.constructor = MyObjectEx;
}
MyObjectEx.prototype = new MyObejct();
 
//这样MyObjectEx.Instance.constructor == MyObjectEx
//并且MyObjectEx.prototype.constructor = MyObject
```

#### 2.5 学JavaScript不能太纠结于实现的细节

你可以**纠结与语言的细节**，但不要纠结于实现的细节(SpideMonkey,JScript)。有些问题就是很奇怪。

比如：

```javascript
var b = {};
console.log(b.__proto__ instanceof Object)  //此处是false即使我用debugger看到他是Object
```
 

如果你还想看一些诡异的地方，移步至《[Wat](http://www.aqee.net/wat/)》
