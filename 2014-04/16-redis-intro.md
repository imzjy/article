Redis简介
=====

Redis是一个偏重于in-memory的key-value数据库，这样讲有点儿不准确，但是很容易将Redis简单分类。
更准确的讲Redis是一个数据结构的存储服务。它的value不仅仅只有string，他的value可以是下面几种：

* string
* list
* set
* zset(ordered set)
* hash

正是它有不同的数据结构，将其于其他的NoSQL数据库区别开来。在传统的关系数据库中只有表格这种灵活，复杂的数据结构，
我们的应用数据最终都将转换成table这种数据结构进行存储，这么多年过来，事实证明这是可行的，但是我们可以做的更好。
在传统关系数据库中，我们这种可行通常牺牲了两个东西：首先是性能，其次是复杂度。而这两点正是Redis试图解决的。
在Redis中，若你的建模结果发现key-value更适合你，那么你就用key-value。若你的模型中确实需要hash，那么为什么不直接选key-hash？
用更加直接的数据结构是Redis所提倡和擅长的。

### 1.运行Redis服务

为了运行Redis服务，我们需要下载源码，编译，安装Redis。Redis推荐从源代码安装Redis，这样能保证安装到最新版本的Redis。
我是在Windows上测试Redis，所以讲下Windows下的编译安装，如果你不想自己编译，可以直接下载编辑好的Win32或Win64编译好的版本。

首先，从https://github.com/MSOpenTech/redis下载源代码，直接“download as ZIP”。
如果你不想自己编译，直接使用redis-2.6/bin/release下的编译好的可执行文件。编译过程也十分简单，
用VS2010打开redis-2.6/msvs/RedisServer.sln,然后直接编译，不出意外，
你就可以从msvs的Debug或者Release目录(根据你的编译选项)找到编译好的可执行文件。我们来看看这些编译好的可执行文件和这些文件的功能。

* redis-server  #服务器
* redis-cli        #命令行客户端
* redis-benchmark    #性能测试
* redis-check-aof & redis-check-dump #处理可能损坏的dump文件

Redis使用相对简单，特别是测试时候，只要一个redis-server就可以了，所谓的redis服务的安装就是将redis-server加到可执行目录，
然后自启动就可以。对于初次使用，我们只需要：

`>redis-server`

这样redis就在6379向我们提供服务了，一个可以测试的完整的redis server已经成功建立了。

当然，我们可以配置一些redis server的一些行为，但这不是我们这里讨论的重点。简单讲我们可以

`>redis-server /path/to/redis.conf`

redis.conf的文件和说明，可以在redis-2.6/redis.conf中找到，更多的说明参考：http://redis.io/topics/config

### 2.做一些简单测试
在我们编译好的文件中有redis-cli.exe，这个是redis自带的命令行客户端，我们可以通过这个命令行客户端来操作redis server。我们直接：

`>redis-cli`

就可以连接上我们本机上的redis服务了。更多的选项可以`>redis-cli –help`

对5种数据结构的简单操作：
```text
--string
redis 127.0.0.1:6379> set users:jcu:name "Jerry Chou"
OK
--list
redis 127.0.0.1:6379> lpush users:jcu:cities Beijing
(integer) 1
redis 127.0.0.1:6379> lpush users:jcu:cities Shanghai
(integer) 2
redis 127.0.0.1:6379> lpush users:jcu:cities Guangzhou
(integer) 3
--set
redis 127.0.0.1:6379> sadd users:jcu:likes music
(integer) 1
redis 127.0.0.1:6379> sadd users:jcu:likes book
(integer) 1
redis 127.0.0.1:6379> sadd users:jcu:likes sport
(integer) 1
redis 127.0.0.1:6379> sadd users:jcu:likes book   #re-adding book will not added to the set
(integer) 0
--ordered set
redis 127.0.0.1:6379> zadd users:jcu:scores 99 cs
(integer) 1
redis 127.0.0.1:6379> zadd users:jcu:scores 90 music
(integer) 1
redis 127.0.0.1:6379> zadd users:jcu:scores 80 math
(integer) 1
redis 127.0.0.1:6379> zadd users:jcu:scores 60 art
(integer) 1
--hash
redis 127.0.0.1:6379> hset users:jcu:securities hr 001
(integer) 1
redis 127.0.0.1:6379> hset users:jcu:securities rd 002
(integer) 1
redis 127.0.0.1:6379> hset users:jcu:securities ls 008
(integer) 1
 
--output
redis 127.0.0.1:6379> get users:jcu:name
"Jerry Chou"
 
redis 127.0.0.1:6379> lrange users:jcu:cities 0 -1
1) "Guangzhou"
2) "Shanghai"
3) "Beijing"
 
redis 127.0.0.1:6379> smembers users:jcu:likes
1) "music"
2) "sport"
3) "book"
 
 
redis 127.0.0.1:6379> zrange users:jcu:scores 0 90
1) "art"
2) "math"
3) "music"
4) "cs"
 
redis 127.0.0.1:6379> hget users:jcu:securities rd
"002"
```

#### 2.1 命令的分类
分类是帮助记忆的最好方式，在官方页面：http://redis.io/commands 已经将命令进行了分类：

image

基本就可以分为操作5种数据结构的命令，数据库管理状态命令，订阅/发布管理，事物(transaction)命令。
通过分类我们可以更加快速的找到我们所需要的命令。

### 3.在具体的应用中使用Redis
redis-cli是我们命令行的客户端，我们在将Redis集成到自己的应用中的时候不可能用redis-cli命令行工具。
Redis的官方网站上列出的Redis支持的语言绑定，对于常见的语言我们可以直接使用。
我们通过一个简单的聊天程序来看看怎么在项目中使用Redis。

#### 3.1 聊天程序分析
首先我们来想想我们的应用需求，然后抽象成模型，最后对应于相应的数据结构。对于一个聊天程序我们需要什么？

* 好友
* 能发消息给好友
* 能查看聊天记录
* 自己的个性设置
* 上面这些需求是一个聊天程序的核心。对于好友，其实就是人们间的关系，对于单个用户来说的话就是me to many users，
也是一种一对多的关系，而且好友具有不重复性和无序性。对应于Redis的数据结构正好是Set。

而能够发消息给好友是我们聊天交流的基础，细分开来还可以分为可以给在线好友发送消息和可以给离线好友发送消息，这里我们为了简化，
我们只考虑给在线好友发送消息的情况。当一个用户上线了，这个用户可以说：I am ready,我可以收消息了，
换个说法就是我在监听所有好友发送给我的消息。抽象出来这是一个观察者模式，对应于Redis，我们可以用订阅/发布功能来实现。

聊天记录其实就是一个有序的列表，这个太直白不过了，自己个性设置，我们可以看做一个用户有许多属性，这里我们用hash来实现。

* 好友 –> Set
* 能发消息给好友  -> Pub/Sub
* 能查看聊天记录  -> ZSet
* 自己的个性设置  -> Hash
 

#### 3.2 聊天程序的总体架构和技术选择

image

https://docs.google.com/drawings/d/1WArrjazS-1cwCoBysHqj4QDJ56oveUhHXSrt4IPp8PY/edit?usp=sharing

技术选择总体来说是个人偏好，你可以根据自己的需要来设计自己的架构和选择合适的技术。

#### 3.3 聊天程序源代码
https://github.com/jatsz/chat-app-with-redis
