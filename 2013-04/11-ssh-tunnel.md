SSH Tunnel
======

用处你懂得。

### 1，打开ssh tunnel端口转发

```text
ssh -qCNgf user@a-proxy-server -D 127.0.0.1:1234
-q quite mode
-C compress the data
-N only port forward(do not execute the command)
-g allow remote hosts to connect the local forwarded ports
-f run in brackground
```

### 2，配置Firefox

![Alt Text](http://images.cnitblog.com/blog/72292/201304/11103352-fa9cf53490da42baacc294ef74e76ef7.png) 

![Alt Text](http://images.cnitblog.com/blog/72292/201304/11103355-6b5ffbf5eb694f5496adf33faa285fad.png)

为了防止DNS污染，可以让remote来做DNS解析。在Firefox的地址栏输入 about:config

![Alt Text](http://images.cnitblog.com/blog/72292/201304/11103400-0075ef213f8741779948847af9170d0c.png)
