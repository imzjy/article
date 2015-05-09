RESTful实现中的几点细节
=======================

### 无状态

RESTful是基于无状态的HTTP协议的，所以在具体实现的时候不要把传统的基于状态的模式套入进来，既然使用了RESTful那么很大的一个优点就是易于扩展，那么无状态是保证扩展的一个几乎是必须条件。

在想要对我们的资源进行保护的时候我们特别想要状态，原因很简单：假如没有状态我们怎么进来的访问是有权限的呢？其实这点也很好理解，我们平时用来表示状态而维护的Session也就是一个跟随HTTP一起发送的标示符而已，所以我们也采用类似的方式，比如基于Token的方式，我们每次请求资源的时候带上相应的Token用来做权限识别。

我以前有次将ASP.NET的应用放到Amazon的Load Balancer的后面，结果出现了错误原因就是我们在服务器上维护了一个Session的状态，但是后面有多台服务器维护着各自的Session，也就是说本来想给A服务器的Session信息在经过均衡负载的时候给了B服务器，所以出现了错误，好再Amazon得Load Balancer已经考虑到这个问题，后来我们启用的Session Sticky来解决了这个问题。

RESTful API中ST指的就是(State Transfer)我们在访问资源的时候带上这些State将State带给任意一台Server，Server都可以处理这个请求返回对应的资源，这才是RESTful方式，也是可扩展的保证。

### 怎么样表示时间

现在基本上通用的传输格式都是JSON，XML基本看不到了，XML中无疑义的标签太多，确实不好用，这个我很早的博客中已经说到过，我很讨厌XML。JSON可以表示的数据结构有：

- map
- array
- string
- bool
- number

这基本已经覆盖了我们常用的数据结构，通过任意组合我们可以实现业务中很复杂的数据表示。但中间有个问题就是，我们怎么样表示时间？

JavaScript中又time这个对象，但是JSON中却不支持种对象表示，这也不奇怪Text-Based的东西已经在Unix的世界证明他得有点，我们也不需要多出一种数据类型，而是我们怎么样表示日期这种数据类型。通常的做法也有两种：

- 基于[ISO8601](http://en.wikipedia.org/wiki/ISO_8601)
- 基于Epoch的时间戳(JavaScrpit中得`(new Date()).getTime()`)

两种方式都可以，ISO8601的方式比较容易阅读有时区的信息，而Epoch的方式在程序间的通用性更高，在JSON中直接使用`number`就可以表示了。我个人倾向于选择第二种，即基于时间戳的方式。反正这些字符都不会直接就用来显示给用户，都需要处理一下，那么选择更加易于处理的Epoch的方式更加方便。

### 查询，排序，输出表示

我们知道HTTP的方法对应的CRUD是:

- POST -- Creation
- GET  -- Retrieve
- PUT  -- Update
- DELETE -- Delete

这个我们基于标准就可以了，但是对于用户的`GET`方法如果让用户筛选出自己想要的数据呢？HTTP的Query String就是用来干这个的，通常的做法是：

- 筛选：`status=online,quited` 通过`,`来分隔多个字段
- 排序：`sort=+id,-mtime` 在排序字段前面使用`+`号表示升序，用`-`表示降序
- 输出方式：`output=json` 支持多种输出方式来保证兼容性
- 分页：`offset=2&page_id=5` 将分页输出的状态通过Query String传输给服务器




