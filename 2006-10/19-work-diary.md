C#[该行不属于与此关系相同的数据集]解决
=====

今天用C#写一个用oleDB连接数据库的例子，其中有新建一个Relation。

```csharp
DataRelation CusOrdRel = new DataRelation("CusOrds",
NwDataSet.Tables["Customers"].Columns["CustomerID"],
NwDataSet.Tables["Orders"].Columns["CustomerID"]);
```

之后将关系图Print出来：

```csharp
//Print out nested customers and their orders ids
foreach(DataRow CusRow in NwDataSet.Tables["Customers"].Rows)
{
  Console.WriteLine("CustomerID: "+CusRow["CustomerID"]+"CompanyName: "+CusRow["CompanyName"]);
  foreach(DataRow OrdRow in CusRow.GetChildRows(CusOrdRel))
  {
    Console.WriteLine("\t OrderID:",OrdRow["OrderID"]);
  }
}
```

在我运行程序的时候报错：

`该行不属于与此关系相同的数据集。`

奇怪，我已建立Customers table的CustomerID和Orders table的CustomerID之间的关系，为什么，在用`CusRow.GetChildRows(CusOrdRel)`的时候，却显示：

`该行不属于与此关系相同的数据集`

最的查询的MicroSoft的网站，找到了问题所在。

在建立DataSet的Relation后，要将该Relation写回DataSet。在建立Relation后添加以下语句，将Relation写回DataSet：

`NwDataSet.Relations.Add(CusOrdRel);`

剩下再用`CusRow.GetChildRows`就可以将子Columns显示出来了。