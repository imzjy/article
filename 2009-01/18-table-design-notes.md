数据库设计
=====

最近做了一个项目，对特定领域的数据库表格的设计有些感想。项目完成后总是无意中想到，总感觉自己先前吃了个大亏，现在这些感想总结一下。

### 一，来些实际的吧。

看书是我的一个主要业余生活，但看理论性较强的书总是让我很头痛，因为知道这会很有用，但较真的话，一时也说不上来哪里有用。所以我很感谢那些写实践，然后回到理论的书。

我们在大学时上数据库时总是那几张表，S表，C表，SC表。S表是学生表，C表是课程表，SC是学生选课关系表。可是我们工作了，总是要面对客户的。客户需要一个学生管理系统，让你设计表格你怎么设计，思路是什么？客户需要一个HR的假期管理系统，你又如何设计后台数据库表格？我的经验是：

### 二，从领域入手。

比如学生信息系统，哪些数据客户关心的。收集到客户关心的数据后，接下来最重要的工作是找出哪些数据是基本资料（Master Data），哪些资料是交易资料（Transcation Data）。这一步很重要，是自然而然地将数据分割，建立数据库表格的一个关键。例如学生信息管理系统中，S表，C表是Master Data，SC表是Transcation Data。再如HR的请假系统，用户信息是Master Data，假期类型也是Master Data，而每一次的请假是Transaction Data。

在Master Data和Transaction Data区分的时候有一点需要注意，这就是Transaction表可能有层级。如上例，当SC(学生选课关系表)是Transaction Data时，那么学生成绩表呢？这也是Transaction Data，但这个Transaction Data往往依赖于学生选课表。这时从学生成绩表的角度来看SC表倒成了Master Data。这在设计时需要注意。

另一个设计数据库表格需要考虑是关系。关系是什么?关系就是数据间的联系，用通俗的话讲就是：belongs to, has many。

反映到业务领域中就是一个学生可以选多门课（has many），每一个成绩只能属于一个学生（belongs to），等等，你还可以找出更多。

关系在数据库中是通过外键来实现的。定义好这些关系，以符合业务模型。

还有一点需要留意的是数据完整性，这可以通用主键，约束来实现。

### 三，几点说明。

关于Master Data和Transacton Data的区分，我是从SAP的表格设计中借鉴来的。在SAP中数据表被分成三类，其定义及说明如下：

- Master data（资料主档） is data which is frequently accessed, but which is rarely updated.

	An example of master data is the data contained in an address file, for example, name, address, and telephone number.

- Transaction data（交易主档） is data that is changed frequently.

	An example oftransaction data is the stock of goods in a warehouse, which changes each time an order is processed.

- Organizational data（配置主档） is customizing data that is entered when the system is configured and is then rarely changed.

	The table with country keys is an example.

数据库重构似乎比代码重构要难的多，采用原型的方法，经多次迭代可以做出更好的数据库结构设计，但这往往是不允许的。因此你需要积累经验。
