Web开发中的跨域(cross domain problem in web development)
==========

### 1，什么是跨域？

要说跨域先说说“同源策略(same origin policy)”，同源策略是指网页上的脚本只能访问只能访问跟自己同源(host+protocol+port)的网页属性和方法。比如你在你的index.html中用iframe加载了`http://www.google.com/index.html`，那么`http://www.google.com/index.html`上的脚本就这能操作`http://www.google.com`上的内容。比如iframe内的脚本就不能访问iframe外的DOM。同样你也没有办法通过JavaScript来访问iframe里装载的页面。

这样考虑主要是为了安全性，如果你进入的一个恶意网站，他将网银用iframe装载进来，然后在你输入的时候用JavaScript操作DOM获取iframe中网银输入的口令，密码，那就悲催了。

### 2，那该怎么办？
有时我们真的需要和其他网站通信，那该怎么办？

如果是单向通信，你想从别的获取数据，并使用数据来改变当前的DOM，即显示数据，那么JSONP是个不错的选择。JSONP原理就是插入一个script标签，向另一个域请求js文件。比如：`http://example.com?callback=showmsg`。那么我们就在我们页面中插入:

```html
<script src=”http://example.com?callback=showmsg”></script>
```

然后我们在定义callback函数

```javascript
function showmsg(msg){
 
  alert(msg);
 
}
```

而exampe返回的是个json(javascript)

`showmsg(“we are here”);`

这使得，我们先前的回调函数得以执行。

如果你需要双向通信，目前有两个办法比较常用：

- 通过Flash加上crossdomain.xml来实现。
- HTML5的postMessage。

 
------
Reference：

http://www.cnblogs.com/rainman/archive/2011/02/20/1959325.html

http://easyxdm.net/wp/
