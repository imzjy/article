理解JavaScript中的原型继承(2)
=======

两年前在我学习JavaScript的时候我就写过两篇关于原型继承的博客：

* 理解JavaScript中原型继承
* JavaScript中的原型继承

这两篇博客讲的都是原型的使用，其中一篇还有我学习时的错误理解。今天看《Understanding Scopes》这让我从新思考了一下原型继承，
更重要的是站在一个继承设计者的角度再看一下原型继承。

在传统的面向类的继承体系中，我们有个Best Practices是优先使用(对象)组合代替(类)继承，而原型继承是这个思想的一个运用。
和面向对象和函数式编程一样，使用几乎任何语言都可以实现这样的思想，我以前学的只是这个思想的一个JavaScript实现，而已。

基于原型的继承其实是一种组合式的继承，朴素的说法就是子域中属性找不到的话就去父域中找找，这里的父域是用原型(__proto__)去引用的，
依次递归整个原型链。最终的实现其实就是对象的组合。子对象包含父对象的引用。既然是继承必然涉及到重名问题，子对象和父对象各自相当于一个作用域，重名问题的处理也是就近(可覆盖shadow/隐藏hide)原则，即子作用域的同名属性会起作用，隐藏了父作用域的同名属性，但是由于是组合，这两个属性是独立的。我们用伪代码看看：

```javascript
aParent = {name:’jerry’}
aChild = {__proto__:aParent, name:’frank’}
```

aChild中的name和aParent中的name是各自独立的。我们aChild.name=’unknown’并不会改变aParent.name。


有一点要拿出单独说说，造成迷糊的最大根源就是误解，对于如下代码：

```javascript
aParent = {name:’jerry’}
aChild = {__proto__:aParent}
```

若我们取aChild.name的值，我们很容易resolve，那就是子域中找不到，去父域中找，找到了jerry。
但是对于：aChild.name = ‘frank’这样的赋值代码我们会产生歧义(ambiguous)，我们可能有两中含义：

1.更新父域中的name属性为frank。
2.设置子域中的name属性为frank。

JavaScript选用的方式是第2种。即设置(新建)子域自己的name属性为frank，并隐藏了父域中的name属性。
我们通常误以为JavaScript是按1的方式工作，其实不是。

另外类(模版)其实在编程语言的实现中是可有可无的，像JavaScript压根就没有类(模版)，他只有对象，new Point()只不过是一个语法糖，
跟aObj = createObject()是一样的，只是调用一个方法去生成一个对象，而已。
