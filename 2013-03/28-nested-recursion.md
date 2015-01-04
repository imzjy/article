21层嵌套的递归解决方案
========

刚才看到一篇文章《[21 nested callbacks](http://blog.michellebu.com/2013/03/21-nested-callbacks/)》，作者吐槽了一下当时他学编程时的一个趣事：为了写一个HTML的动画，他写了有21层嵌套的函数。由于作者主要是抒情，所以这样的英文很不好阅读。我就把他最重要的思想提取出来。

1，最初的实现，朴素的实现
其实这个小哥就是想把20个div依次展现在用户的眼前。他用了JQuery库的animate函数，这个函数接受一个回调，当动画完成时这个回调函数被执行。小哥最初的想法很朴素，那就是，当第一个div被显示出来的时候，传入回调函数来显示第二个div，代码类似于：

```javascript
$(".disappear").click(function(){
  $("#div1").animate({ "opacity": "100" },
    100,
    function(){$("#div2").animate({ "opacity": "100" },
      100,
      function(){$("#div3").animate({ "opacity": "100" },
        100,
----------omit for brevity----------
          function(){$("#div20").animate({ "opacity": "100" },
            100)           
})})})})})})})})})})})})})})})})})})})})})})})})
```

坦白讲这个想法也还行，至少能正确实现功能，就是代码太难看了，要整整21个回调函数。通常来讲这也是最符合人类直觉的，现实中人们就是这样解决问题的。这也可能是范凯在《Ruby社区应该去Rails化了》说NodeJS的编程风格是反人类的主要原因：

node.js的Event IO编程风格在我看来是“反人类”的，极其变态的。用来写代码上规模的应用，代码的可读性和可维护性都很差。Event IO是很底层的技术，我很难理解为何不封装成coroutine来使用。node.js只适合用来开发real-time类型的应用。

如果按这样的方式来实现，确实他妈的反人类，正如这个小哥自嘲他自己是“狂有耐心”。

2，函数式的实现，递归实现
从代码中看，第一直觉可能就是相似的代码太多了。如果想要更好看的代码，必须减少重复，也就是我们常说的DRY。单从代码外观上看这个函数明显有个“展开”，如果从代码的执行上看有个“收缩”的过程。这不就是递归吗？

1
2
3
4
5
6
7
8
9
10
11
12
13
14
function hideOrShowPrev($elem, opacity){
    $elem.animate({ "opacity": opacity },
        100,
        function(){
            var $toHide = $elem.prev();
            if($toHide){
                hideOrShowPrev($toHide, opacity);
            }            
    })
}
 
$("#start").click(function(){
   hideOrShowPrev( $('#row20'), 100);
});
这个实现是我Copy评论中的一个哥们的。
