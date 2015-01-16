Oracle数据的批量插入
========

前两天接到一个需求——需要编程将SQL Server中的数据插入至Oracle。数据大约有20多万条记录。开始的时候我采取了直接构建SQL插入的方式，结果耗时太长。为了提高性能我上网找了资料。最终采用DataAdapter批量插入至Oracle，提高了性能。


### 一，直接构建SQL语句插入 

```vb
sw.Start()
''''Read Z02J from SQL Server
Dim sqlCmd As New SqlCommand()
sqlCmd.Connection = sqlConnection
sqlCmd.CommandText = "SELECT * FROM  Z02J"

Dim sqlDr As SqlDataReader
sqlDr = sqlCmd.ExecuteReader()

Dim cmdInsertZ02J As New OracleCommand()
cmdInsertZ02J.Connection = oraConnection
cmdInsertZ02J.CommandText = BuildSQLStatement(SQLType.Insert,"z02j")

Dim plantLever, material, oldMaterialNum, materialDescription As Object
While sqlDr.Read()
	plantLever = ReadSqlDataReader(sqlDr, 0, "")
	material = ReadSqlDataReader(sqlDr, 1, "")
	oldMaterialNum = ReadSqlDataReader(sqlDr, 2, "")
	materialDescription = ReadSqlDataReader(sqlDr, 3, "")
	''Insert to Oracle table Z02J
	cmdInsertZ02J.Parameters.AddWithValue(":plantLever", plantLever)
	cmdInsertZ02J.Parameters.AddWithValue(":material", material)
	cmdInsertZ02J.Parameters.AddWithValue(":oldMaterialNum", oldMaterialNum)
	cmdInsertZ02J.Parameters.AddWithValue(":materialDescription", materialDescription)
	cmdInsertZ02J.ExecuteNonQuery()
End While
sw.Stop()
Loger.Info("Reading z02j form sql sever used", sw.Elapsed.TotalSeconds.ToString())
```

### 二，采用DataAdapter实现批量插入

```vb
sw.Start()
''''Read Z02J from SQL Server
Dim sqlCmd As New SqlCommand()
sqlCmd.Connection = sqlConnection
sqlCmd.CommandText = "SELECT * FROM  Z02J"

Dim sqlDr As SqlDataReader
sqlDr = sqlCmd.ExecuteReader()

Dim cmdInsertZ02J As New OracleCommand()
cmdInsertZ02J.Connection = oraConnection
cmdInsertZ02J.CommandText = BuildSQLStatement(SQLType.Insert,"z02j")

Dim dtSqlZ02J As New DataTable
dtSqlZ02J.Columns.Add("plantLever")
dtSqlZ02J.Columns.Add("material")
dtSqlZ02J.Columns.Add("oldMaterialNum")
dtSqlZ02J.Columns.Add("materialDescription")

Dim plantLever, material, oldMaterialNum, materialDescription As Object
While sqlDr.Read()
	plantLever = ReadSqlDataReader(sqlDr, 0, "")
	material = ReadSqlDataReader(sqlDr, 1, "")
	oldMaterialNum = ReadSqlDataReader(sqlDr, 2, "")
	materialDescription = ReadSqlDataReader(sqlDr, 3, "")
	dtSqlZ02J.Rows.Add(plantLever, material, oldMaterialNum, materialDescription)
End While
sw.Stop()
Loger.Info("Reading z02j form sql sever used", sw.Elapsed.TotalSeconds.ToString())

sw.Start()
Dim oraDa As New OracleDataAdapter()
oraDa.InsertCommand = cmdInsertZ02J
oraDa.InsertCommand.Parameters.Add(":plantLever", OracleType.Char, 255, "plantLever")
oraDa.InsertCommand.Parameters.Add(":material", OracleType.Char, 255, "material")
oraDa.InsertCommand.Parameters.Add(":oldMaterialNum", OracleType.Char, 255, "oldMaterialNum")
oraDa.InsertCommand.Parameters.Add(":materialDescription", OracleType.Char, 500, "materialDescription")

oraDa.InsertCommand.UpdatedRowSource = UpdateRowSource.None
oraDa.UpdateBatchSize = 20    '''Adjust the batch size based on testing result

oraDa.Update(dtSqlZ02J)
sw.Stop()
Loger.Info("Insert to oracle used", sw.Elapsed.TotalSeconds.ToString())
```

在我的环境中批量插入24万笔记录用时大约260s左右。
貌似SQL Server中.net驱动程序提供了SqlBulkCopy类来提高大量数据导入的性能。有需要的朋友可以查下MSDN。
