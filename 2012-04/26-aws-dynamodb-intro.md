Amazon DynamoDB 介绍
=================

### 数据模型概念 - Tables, Items, and Attributes

DynamoDB数据库有表(tables)，数据项(items)和属性(attributes)构成。一个数据库有若干张tables，一张表有若干items，每个数据项有若干attributes。

在关系型数据库中，一张tables有columns组成。每个records都有相同的属性。然而DynamoDB是NoSQL数据库。也就是除了主键外，每个item都是可以任意自定义的，没有columns的概念，也不受其束缚。唯一的要求就是不要每个item不要超过64 KB大小。这就是所有item name和item value加起来的大小不要超过64 KB。

每个item的attribute都是key-value的结构。每个attribute的value部分既可以使单值(single-valued)也可以是个组合(multi-value)。如果是组合的话，这个集合(set)中值是不允许有重复的。

我们来看一个例子，我们的网上商店，为了保存商品，我们这样的tables结构：

`Products( id, ...)`

有个主键来标识这本书，然后用attributes来描述这本书的细节，比如：

```text
{ 
   Id = 101                                       
   ProductName = "Book 101 Title"
   ISBN = "111-1111111111"
   Authors = [ "Author 1", "Author 2" ]
   Price = -2
   Dimensions = "8.5 x 11.0 x 0.5"
   PageCount = 500
   InPublication = 1
   ProductCategory = "Book" 
}                                    
{
   Id = 201 
   ProductName = "18-Bicycle 201"
   Description = "201 description"
   BicycleType = "Road"
   Brand = "Brand-Company A"
   Price = 100
   Gender = "M"
   Color = [ "Red", "Black" ]
   ProductCategory = "Bike"
}
{
   Id = 202 
   ProductName = "21-Bicycle 202"
   Description = "202 description"
   BicycleType = "Road"
   Brand = "Brand-Company A"
   Price = 200
   Gender = "M"
   Color = [ "Green", "Black" ]
   ProductCategory = "Bike"
}
```

注意商品Book的Aurthors和Bike的Color属性，它们就是multi-value。这是一种类似JSON的结构(JSON-like)。需要注意的是DynamoDB不允许atrributes的value为空(null)或空字符串(empty string)。

### 主键 – Primary Key
当你创建表格时，除了表名(table name)以外还需要一个主键。DynamoDB支持下面两种主键(primary keys)：

#### Hash类型的主键：

主键是某个attribute的hash值。DynamoDB会为这个主键atrributes创建一个unordered hash index。上例中Product有个id作为主键。他是这张表Hash属性(attributes)。

#### Hash and Range类型的主键：

主键是两个attribute组合而成。第一个属性是hash attributes。第二个属性是range attribute。DynamoDB会在hash attribute上创建一个unordered hash index，在range attribute上创建一个sorted range index。例如，Amazon维护了一些论坛，每个论坛有许多讨论话题(threads)，每个thread又有许多回复(replies)。你可能这样设计表格：

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201204/201204261113066726.png)

Thread和Reply表都有hash & range类型主键。对Thread表来说，每个forum都有若干个subjects。这样ForumName就可以做hash atrribute，subject就可以做range attribute。注意，你必须考虑到，DynamoDB并不支持表格间的join查询。例如你必须在Reply表的id中保存ForumName和subject。这样你就可以parse这个id来查找相应的Forum和Subject。

### DynamoDB的数据类型

DynamoDB支持两种数据类型：

1. 标量(scalar) —— 数字(Number)或字符串(String) 
1. 多值组合(multi-valued) —— 数字的组合(Number set)或字符串的组合(String set)

字符串 是以二进制UTF8来编码的。主键以外的字符串的大小没有什么限制。当然不能超过item大小(64 KB)。可以参见Limits in Amazon DynamoDB。

当你使用Scan或Query接口来返回一个有序的结果时会用到字符串的比较。字符串的比较是基于ASCII值的比较。

数字 是正的或负的整数或小数。小数可以精确到小数点后38位。序列化后的数字是以String类型来传给DynamoDB的，然而DynamoDB当数字一样处理它们。

字符串集和数字集 需要注意的就是集合中不可以有重复的值，另外集合也是无序的


---
Reference

http://docs.amazonwebservices.com/amazondynamodb/latest/developerguide/DataModel.html
