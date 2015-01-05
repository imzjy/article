iframe间的跨域通信
==========

### 1，跨域的一个示例

当你需要操作一个内嵌iframe是，如果这个内嵌iframe和打开的网站不在同一个域中，你时常会遇到这样的报错：

> Unsafe JavaScript attempt to access frame with URL http:/www.d1.com from frame with URL http://www.d2.com. Domains, protocols and ports must match.

从报错信息中我们可以知道，浏览器是通过域名(domain)，协议(HTTP)，端口(Port)。也就是说这三点只要有一个不匹配那就是跨域(Cross domain)。

对于跨域，我们通常的解决办法是在原来的域添加一个文件，用该文件作为中间人来实现跨域。也就是说，先发消息到该文件，由该文件再操作同域的HTML。

HTML 5给我们带来了安全的跨域通信接口，即window.postMessage()方法。它方法原型是：

`window.postMessage(msg, domain);`

我们可以给指定的domain发送msg。而接收msg的iframe只要注册一个监听事件就可以了。我们看示例：

`www.d1.com/a.html`

```html
<html>
<head>
    <title>operate the iframe on other domain</title>
    <script>
        function sendMessage(){
            var frm = document.getElementById("iframe1");
            frm.contentWindow.postMessage("hello","*")
        }
    </script>
</head>
<body>
    <input id="send" type="button" onclick="sendMessage()" value="send message" />
    <br />
    <iframe style="width:300px; height:400px;" id="iframe1" src="http://www.d2.com/b.html">
    </iframe>
</body>
</html>
```

我们再看看监听的那个iframe

`www.d2.com/b.html`

```html
<html>
<head>
    <title>a frame which receive the message</title>
    <script>
        var OnMessage = function (e) {
            alert(e.data);
        }
        function init() {
            if (window.addEventListener) {  // all browsers except IE before version 9
                window.addEventListener("message", OnMessage, false);
            } else {
                if (window.attachEvent) {   // IE before version 9
                window.attachEvent("onmessage", OnMessage);
                }
            }
            };
            init();
    </script>
</head>
<body>
    <p>a iframe to receive the message</p>
</body>
</html>
```

在监听处理函数中我们可以判断具体的那个domain发来的消息。

### 2，浏览器支持

IE8+, FF3+, Chrome, Safari

IE8中需要注意的是msg这个参数只能是string，而其他浏览器支持JavaScript的object。变通办法就是发送一个在发送时JSON.stringfy格式化一下，而在接受端JSON.parse就可以了。

如果有向后兼容的需要，可以考虑这个[Hack](http://www.onlineaspect.com/2010/01/15/backwards-compatible-postmessage/): Backwards compatible window.postMessage()

Update:2012-08-30

前些日子我发现Tecent的一个Team的Blog的一篇文章，利用”about:blank”很好地解决的IE6和IE7下的iframe跨域问题，具体请猛击：[iframe跨域通信的通用解决方案](http://www.alloyteam.com/2012/08/lightweight-solution-for-an-iframe-cross-domain-communication/)。

### 3，注意事项

如果你在接受消息的iframe中通过JavaScript来修改DOM元素。要确保iframe已经加载完成，可以这样做：

```javascript
_overlay = document.getElementById("iframe1");
if(_overlay.attachEvent){
    _overlay.attachEvent("onreadystatechange", function(){
       if(_overlay.readyState === "complete" || _overlay.readyState == "loaded"){
             _overlay.detachEvent( "onreadystatechange", arguments.callee);
            sendMessage();
       }
    });
} else {
    if(_overlay.addEventListener){
        _overlay.addEventListener( "load", function(){
             this.removeEventListener( "load", arguments.call, false);
             sendMessage();
        }, false);
    }
}
```

参考： 

http://blog.css-js.com/javascript/javascript-iframe-readystate.html

http://msdn.microsoft.com/en-us/library/ie/cc197015(v=vs.85).aspx

https://developer.mozilla.org/en-US/docs/DOM/window.postMessage

http://www.alloyteam.com/2012/08/lightweight-solution-for-an-iframe-cross-domain-communication/
