亚马逊的负载均衡(Amazon Load Balancing)
=======

公司最近要将架构迁到云上，存储用S3，服务器用EC2。为了将我们的架构变的具有横向的伸缩性，我们使用AWS的Load balancing来做负载均衡。简单来说负载均衡就是讲大量的客户端访问分发到不同的后端amazon ec2 instances中。

Amazon的Load balancing配置起来也非常简单，就是将已存在的ec2 instance添加到load balancing中。之后你可以配置端口转发，即将客户访问的端口转发到合适的后台服务。当然也有些需要注意的地方：

### 1，从哪里找到Load Balancing的配置页面
就在你的EC2的Dashboard中就可以找到Load Balancing配置页面。

![aws-load-balancing](http://images.cnitblog.com/blog/72292/201303/27115408-ee4f8a53d11842939f16d81fe41357e8.png)

### 2，Port转发的配置

在使用Load Balancing之前要设置端口的转发，就在Listeners那个tab中。如果你使用HTTP协议，你就可以选择HTTP协议。如果你是TCP应用请选择TCP，看论坛上说可以使用的TCP![端口在是从1024起步的](https://forums.aws.amazon.com/message.jspa?messageID=343728)。如果你是选了HTTP，有个可能对应用来说比较有用的选项Stickiness，其实就是Load Balancer在HTTP协议上加了一个Cookie，借此来实现Session的功能。

### 3，Health Check

Load Balancing的另一个功能，或者说Feature就是Load Balancer维护一个ec2 instances pool。通过Health Check的instance会被添加到instances pool中等待load balancer分发过来的connections。如果某个instance通不过health check，那么他会从instances pool删除，load balancer不会再分发connections到这个instance。但是删除的instance会继续做health check当他的再次通过health check的时候会被再次添加到instances pool中。

Health Check分为两种类型：

1. HTTP应用，那么Health Check就是访问一个固定位置的URL，如果返回HTTP Status Code为200。那么load balancer就认为通过health check。可以根据你的业务在URL的服务端代码中做一些服务器的状态检查，但是不要太耗时。

2. TCP应用，那么Health Check就是发起一个TCP connections，如果连接成功，那么就认为通过了health check。

![health check](http://images.cnitblog.com/blog/72292/201303/27115411-b040135166c44d9b9e5d1ad94bd485df.png)

这里的Timeout就是访问URL或TCP连接的最大超时时间，如果在这个时间内(上图是10s)还是没有返回，那么就就认为unhealthy。

Interval是多久访问一次这个URL或发起一个TCP连接。上图是300s(5min)，这也是容许的最大值。

Unhealthy Threshold是指连续(consecutive)多少次访问失败，才把这个instance从instances pool中移除。

Healthy Threshold是指连续多少次成功访问，才再次把这个instance添加到instances pool中。

### 4，其他的问题
目前对我们的应用来说比较大的问题是，如何将每个instance生成的文件，正确的上传到S3的特定位置。这就引申到一个load balancing的本质：在后端是由多台服务器来提供服务。对于某些应用来说这没有问题，只要后端数据有个统一的访问接口，这都不是问题。但是对于一些应用还是需要在架构上做些调整来实现load balancing的透明化。切记，透明化才能让横向扩展变得容易，这也是用load balancing的初衷。
