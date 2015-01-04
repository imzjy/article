使用GoAgent向GitHub提交代码
=====

今天大中华局域网又发疯了，很多网站都无法打开。不知道是软件故障还是因为高考。但是作为程序员无论他是否发疯该提交代码的还是要提交代码。这里教大家一手用GoAgent提交代码。

### 1，修改Git的协议

GitHub容许我们用两种方式提交代码，一种是SSH，还有一种就是HTTPS。

HTTPS:

![](http://images.cnitblog.com/blog/72292/201306/07112034-d83f719becd54afcb90a9b3822a4f4a5.png)

SSH:

![](http://images.cnitblog.com/blog/72292/201306/07112037-c59da0d8f44c4618b9694256bb799446.png)

如果你的库是以SSH方式提交代码的话，我们先要将SSH改为HTTPS：

![](http://images.cnitblog.com/blog/72292/201306/07112041-e3714049e62e40f39e832fe3e67c3168.png)

 

### 2，设置环境变量

我是用的Cygwin的，可以这样设置环境变量，以让Git在提交的时候使用http proxy：

`$declare -x HTTPS_PROXY="127.0.0.1:8087"`

### 3,向GitHub提交代码

到这一步已经差不多了，但是如果你直接push代码会有这样的报错：

```text
SSL certificate problem: unable to get local issuer certificate while accessing https://github.com/jatsz/s3uploader.git/info/refs 
fatal: HTTP request failed
```

我们可以临时设置环境变量让Git跳过certificate的检查：

`$env GIT_SSL_NO_VERIFY=true git push`

![](http://images.cnitblog.com/blog/72292/201306/07112046-a17008b708a24378af418e90dd59c229.png)

 
---
参考：

http://stackoverflow.com/questions/128035/how-do-i-pull-from-a-git-repository-through-an-http-proxy

http://stackoverflow.com/questions/3777075/ssl-certificate-rejected-trying-to-access-github-over-https-behind-firewall
