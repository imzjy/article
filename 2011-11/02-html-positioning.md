HTML中的几种定位方式
========

### 1，static(默认)

当你没有为一个元素(例如div)指定定位方式时，默认为static，也就是按照文档的流式(flow)定位，将元素放到一个合适的地方。所以在不同的分辨率下，采用流式定位能很好的自适合，取得相对较好的布局效果。

一般来说，我们不需要指明当前元素的定位方式是static——因为这是默认的定位方式。除非你想覆盖从父元素继承来的定位系统。

### 2，relative(相对定位)

在static的基础上，如果我想让一个元素在他本来的位置做一些调整(位移)，我们可以将该元素定位设置为relative，同时指定相对位移(利用top,bottom,left,right)。

有一点需要注意的是，相对定位的元素仍然在文档流中，仍然占据着他本来占据的位置空间——虽然他现在已经不在本来的位置了。

### 3，absolute(绝对定位)

如果你想在一个文档(Document)中将一个元素放至指定位置，你可以使用absolute来定位，将该元素的position设置为absolute，同时使用top,bottom,left,right来定位。

绝对定位会使元素从文档流中被删除，结果就是该元素原本占据的空间被其它元素所填充。

### 4，mix relative and absolute(混合相对定位和绝对定位)

如果对一个父元素设置relative，而对它的一个子元素设置absolute，如：

```html
<div id="parent" style="position:relative">
    <div id="child" style="position:absolute">
    </div>
</div>
```

则子元素的绝对定位的参照物为父元素。

利用混合定位，我们可以用类似下面的css来实现两列(Two Column)定位

```css
#div-parent {
 position:relative;
}
#div-child-right {
 position:absolute;
 top:0;
 right:0;
 width:200px;
}
#div-child-left {
 position:absolute;
 top:0;
 left:0;
 width:200px;
}
```

### 5, fixed(固定定位)

我们知道absolute定位的参照物是“上一个定位过的父元素(static不算)”，那么如果我想让一个元素定位的参照物总是整个文档(viewport)，怎么办呢？

答案是使用fixed定位，fixed定位的参照物总是当前的文档。利用fixed定位，我们很容易让一个div定位在浏览器文档的左上，右上等方位。比如你想添加一个信息提示的div，并将该div固定在右上方，你可以使用以下css

```css
.element  { position:fixed; top:2%; right:2%; }
```

### 6,float(浮动)

对于浮动，需要了解的是：

- 浮动会将元素从文档流中删除，他的空间会被其它元素补上。
- 浮动的参数物是父元素，是在父元素这个容器中飘。
- 为了清除浮动造成的对浮动元素之后元素的影响，我们在浮动元素之后加一个div，并将这个div的clear设置为both。
- 如果两个元素都设置了浮动，则两个元素并不会重叠，第一个元素占据一定空间，第二个元素紧跟其后。如果不想让第二个元素紧跟其后，可以对第二个浮动的元素使用clear。

### 7，reference

```text
Value     Description
static	  Elements renders in order, as they appear in the document flow. This is default.
absolute	The element is positioned relative to its first positioned (not static) ancestor element
fixed	    The element is positioned relative to the browser window
relative	The element is positioned relative to its normal position, so "left:20" adds 20 pixels to the element's LEFT position
inherit	  The value of the position property is inherited from the parent element
```

-----

参考：

http://www.barelyfitz.com/screencast/html-training/css/positioning/

http://davidwalsh.name/css-fixed-position

http://www.w3schools.com/cssref/pr_class_position.asp

http://www.hunuo.com/zhuanti/sheji/275.html
