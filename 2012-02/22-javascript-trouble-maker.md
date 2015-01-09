JavaScript让人很头疼
=======

想当年搞C++的面向对象时，很多问题只要花一些时间就可以搞定，想的很清楚明白。可是最近搞JavaScript好多问题搞不清楚，会用却搞不清楚很让人不爽。

```javascript
function Shape(){
  this.area = function(){};
}
 
function Point(){
  this.x = 0;
  this.y = 0;
}
 
var p = new Point;
 
console.log(p.prototype);    //为啥是undefine
console.log(p.constructor);  //为啥又是指向Point的function
 
console.log("-----------------------------");
 
p.prototype = new Shape();
console.log(p.area);          //为啥又是undefine，不是设置了原型对象嘛，我操
 
Point.prototype = new Shape();
console.log(p.area);          //TMD还是不行，我设置了类型的原型对象啊
 
Point.prototype.area = function(){};
console.log(p.area);          //你妈，为什么啊
 
var p2 = new Point;
console.log(p2.area);         //我操，这时又可以了@#￥%……&*（
```

Output:

```text
undefined
function Point() { this.x = 0; this.y = 0; }
-----------------------------
undefined
undefined
undefined
function () { }
```

我什么时候能搞清楚啊！我看了一堆文章，我TMD的还是有5年以上编程经验的Programmer，我居然还精通于面向对象编程。遇到JavaScript我栽了。你还别给哥一段代码说：这样写就对了，哥知道怎么样写可以，但哥搞不清楚他内部的关系啊，有没有！！！谁能画张图将上面的引用关系，闲置对象,类型对象都画出来，让我醍醐灌顶一次吧。
