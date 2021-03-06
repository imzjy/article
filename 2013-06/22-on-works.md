工作二三事
======

### 性能
设计系统时是要考虑性能的，否则等性能出题出来的时候是非常棘手的。大多数的情况都是当前的生产环境正在运行，留给你的操作时间不多，不会给你太多时间调优。而当你发现问题时，你也不容易改动已经在生产环境的代码。

我常遇到的性能瓶颈最后都出在的数据存储这一层。比如说数据库，如果说数据是应用的核心，那么数据库无疑是核心的管理者。当数据库遇到了性能问题解决起来也颇为棘手。一来，还是生产环境，留给你操作的时间和改动范围不能太大。其次，如果在架构的时候和后期的维护的时候没有对数据库访问组件的管理那么数据库的操作会分布的到处都是，稍微改动就是牵一发而动全身。嗯，嗯，我知道这是架构问题，这是管理问题，但这更是现实问题。初始架构是都知道将数据的访问单独列为一层，但当你的生产环境运行了一年，二年呢。面对棘手的问题，紧张的开发时间，直接存取数据库通常都是最“有效”的，但是等性能问题出来时，你会被绑的死死的，不知道怎么办。

当下解决性能的方式都是将性能的焦点变的“可横向扩展”，比如负载均衡。对于创业团队来说可以做的一种方式就是将专业的事交给专业的人去做。比如，我们逐渐将数据层从数据库转到了S3，让S3自己解决性能问题去。我们只要规范的用就可以了。

时常我们会觉得买别人的服务很贵，不如自己来更省钱。其实不然，很多时候我们是可以计算的。比如说我们每天工资400块。那么平摊到每个小时大约就有50块。如果你平均每月要花费1天时间去捣腾什么数据库，服务器，源代码管理，如果有优秀的服务供应商，每个月的费用又不超过400块，通常你就可以买服务。有一点很明确的就是，我们不是靠捣腾数据库赚钱，不是靠捣腾服务器赚钱，更不是靠捣腾源代码管理软件赚钱，这不是我们的核心。

对了，出于兴趣，我最近在看MySQL。

### 三十岁
无论我承认与否，我确实是个30岁的程序员。我目前还是靠写程序为生。随着年龄的增长自己还是有许多的变化的，我不在像以前那样花那么多的时间在研究代码和技术的学习上，这里面有两方面的因素。首先，我工作了这么些年，研究过许多技术，即使来了一样新的东西我学习的也很快。学习更多的是惯性和喜好，已经没有了刚毕业时的新鲜感。其次，这也是很多悲观的人看到的，家庭的事，公司的事多了，留给自己的时间少了。并且随着年龄的增大专注度会越来越低，但是经验和逻辑性会越来越强。

必须承认的另一点就是程序员需要大段的专注时间，这段时间你是活在程序里的。现在每年都有段时间我会活在程序里，上班想的是程序，下班想，吃饭想，睡觉想，连做梦都是想。但这确实很伤身体。每当我从沉浸中走出来时，我会明显感觉身体不适的信号。所以现在如果不是很必要我已经不再选择这样了，而是选择相对平稳和慢一点的节奏去把事情做好。对此我有招独门秘籍：笔记本。拿个小笔头把每天的事做好，做好就收，这样很有计划和节奏的完成一些任务。

### 下一个三年
我和公司的合同到今年12月份就结束了，在不那么忙的时候我时常会想想我的下一个三年做些什么？有一点比较明确的是我不想当个单纯的程序员了，原因就是当个单纯的程序员对我来说越来越不“好玩”了。当然产生这个念头不是一天两天的了，在这过程中我也顺带了学了许多别的。比如说管理，我学了许多管理的理论知识。每当我感觉不舒服的时候我都会想：如果我是Manager，我该怎么做？这让我反思和学到了很多。还有就是创业，而且随着年龄的增大创业的想法越来越实际，那些当年“gorgeous”的理想越缩越小。

所以下个三年我最有可能的是：

1. 加入一个创业公司，往市场端走走，离客户更近。好吧，其实还是为了2。
1. 和别人合伙开个小店。
1. Project Leader或Project Management，同样还是为了2。
1. 继续做我的大龄程序员。为2赚点钱。

结论很简单：一辈子做什么事都是犯2，人称2范。
