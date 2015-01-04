术和器
====

### 术
最近在带几个兄弟完成互联网项目，我是中途才加入的，其实他们开始的时候已七七八八完成的差不多了，
前端的小伙临时起意拍拍屁股走人了。我觉得可惜，决定尝试去带他们产出一个好的结果。项目管理这样的事，
难的就是相信项目可以成，并且按照心中所设想的按部就班的完成一个个小任务。考验项目的成败的往往是心力，而不是能力。
在团队遇到困难，迷茫的时候，你是否依然坚定。这个坚定来自于两方面：

首先，你相信，并且知道项目总是会遇到这样那样的困难，只要自己按着节奏努力，总是会有好的结果的。
你是否可以凭借你的经验和毅力看的到这样的结果。但这样还不够，你必须使你的团队也看到这样的希望，即使他们看不到那团热火，
也要让团队能看见那微弱的光线。依我的经验来看项目大多数都死在这个阶段，一旦遇到阻力，遇到意外，
我们就对我们开始时候决定产生的怀疑，这是万万要不得的。这个时候沉住气，走过去，那又是一片海阔天空。
而且这也让你的团队形成一道无形的门槛，很多人看不到这样的门槛，这便是你的优势。

其次，勿忘初心。这个坚定是对初心的坚定，在特定时期我们会遇到特定的困难，这些困难各有不同，
我们需要根据事实情况解决这些困扰团队的困难，其底线就是不要忘记我们的初心，我们是准备做什么的，这些决定是否违背了我们的初心。

### 器
在管理团队时候让我对于架构设计有了更深一步的看法。我对核心开发人员的一个要求就是无论是谁，只要拥有我们GitHub仓库的权限，
他就可以通过git clone, install.sh, run.sh这简单的几步就可以在自己的电脑运行我们的项目。当时这是针对当前项目人员配置的一个考虑。
后来发现，即使拥有完备的开发团队，这种架构上的松散，对配置的精简也是必要的。我们写程序的人都知道，花时间最多的通常有两项：
一个是环境配置，另一个是调试。我们要将环境配置的难度降低，避免一些无端的时间消耗。
对于调试，通过日志和热加载可大大减少调试有关的时间消耗。

在学软件设计，或者是软件工程时，我们时常会提到高内聚。这次有机会让我站在工程角度去看高内聚的含义。
理想中，我们的项目的一个相关功能集(features set)可以在项目无缝的被集成。我们是网页相关的开发，对于功能集的开发者，
他不需要知道太多外面的东西，他可以新建一个目录，在里面添加相应的urls映射，相关的资源文件，对应的业务代码，等等。
这些在实体上理应放在同一个文件夹下，并且在框架载入的时候自动加载这些必须的选项，而不需要额外的配置。
在工程上，我们可以将这个功能集外包出去，随便给一个人，他就可以按部就班的开发。这才是高内聚。

如果要展开来说，这也会涉及另一些软件设计的知识，比如软件应该对扩展开放，对修改封闭。
最终很多功能集的实现其实只是系统的一个插件(Plugin)而已，利用系统的已有功能接口来扩展系统。

---
最近工作很忙，杂七杂八的事情多，对于我个人来说将这些事情分解，记录在Google Keep中，执行完成，这很重要。