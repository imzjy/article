 一个Transaction问题[ErrorCode: -2147217873]
 ====

昨天小王过来给我一片SN，让我查一下为什么程式老是在刷这一个SN时失败。我接过这一个SN，Debug了一下。发现在追踪到的程式中，一个Insert的语句报错：主键唯一性约束。

本来也觉得这太简单不过了，于是把追到这个sql要插入的数据拿出来，用select查询一下。可是却也没有找到相同的记录(record)，这下我有些摸不到头脑了。与是又tracing，但一次次都失败了。

今天上午和一个朋友聊这事，经他一提醒，找到了原因：原来我是在一个transaction中执行了几个Action，是这些Action中有些Action在唯性的主键插入了重复的值。为了再现问题，我写了个Transaction测试了一下，果然如此，且我们在VS中tracing时IDE也没有能给出具体哪一个SN重复了，只是给出Ora-0001,哎。看来这个只能靠经验了。

Now, Show the complete code:

```csharp
//-------------------------------------------
//Platform:Winxp + visual stdio2003 
//Language:Csharp
//-------------------------------------------
using System;
using System.Data.OleDb;
namespace ConsoleApplication1
{
 class Class1
 {
  [STAThread]
  static void Main(string[] args)
  {
   System.Data.OleDb.OleDbConnection sqlCon = new OleDbConnection("Provider=SQLOLEDB.1;Password=test;Persist Security Info=True;User ID=test;Initial Catalog=TestA;Data Source=TestA");
   sqlCon.Open();
   
   OleDbCommand sql1= new OleDbCommand("insert into userinfo values('CCCC','CCCC','CCCC')",sqlCon);
   OleDbCommand sql2= new OleDbCommand("insert into userinfo values('DDDD','DDDD','DDDD')",sqlCon);
   OleDbCommand sql3= new OleDbCommand("insert into userinfo values('CCCC','CCCC','CCCC')",sqlCon);
   OleDbTransaction myTrans = sqlCon.BeginTransaction();
   sql1.Transaction = myTrans;
   sql2.Transaction = myTrans;
   sql3.Transaction = myTrans;
   try
   {
    sql1.ExecuteNonQuery();   //Insert "CCCC" to table userinfo
    sql2.ExecuteNonQuery();   //now we can't find "CCC" in database, because this transaction isn't committed.
                           
    sql3.ExecuteNonQuery();   //Oops! Insert "CCCC" to table userinfo dulicated.
   }
   catch(Exception ex)
   {
    myTrans.Rollback();
    sqlCon.Close();
    Console.WriteLine(ex.Message);
    Console.ReadLine();
    return;
   }
   myTrans.Commit();
   Console.WriteLine("Insert Success!");
   Console.ReadLine();
  }

 }
}
```
 
Error message dump by vs2003:

```text
sql3.ExecuteNonQuery()
{System.Data.OleDb.OleDbException}
    System.Runtime.InteropServices.ExternalException: {System.Data.OleDb.OleDbException}
    ErrorCode: -2147217873
    Errors: {System.Data.OleDb.OleDbErrorCollection}
    Message: "语句已终止。\r\n违反了 PRIMARY KEY 约束 'PK_UserInfo'。不能在对象 'UserInfo' 中插入重复键。"
    message: "语句已终止。\r\n违反了 PRIMARY KEY 约束 'PK_UserInfo'。不能在对象 'UserInfo' 中插入重复键。"
    oledbErrors: {System.Data.OleDb.OleDbErrorCollection}
    Source: "Microsoft OLE DB Provider for SQL Server"
    source: "Microsoft OLE DB Provider for SQL Server"
```
