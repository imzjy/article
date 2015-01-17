设计模式之模板方法(Template Method)
========

开场白借用《设计模式》中的关于模板方法的一句引言：

> 定义一个操作中的算法的骨架，而将一些步骤延迟到子类中.Template Method模式使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。

通过这个开场白可以看出，这个模式仍就是变与不变之间的抉择。我在写程序时也时常有这样的情况需要处理。有个操作有中有些是有可能变化的，有些却是固定不变的。例如我接手一个电子商务助手的开发工作，这个工作中便有一项是将名片中的姓名及住址记录下来。我便想定义以下操作（Platform:WinXp+C# in Visual Studio2003）;

```c++
public void AddToDatabase(string name ,string address)
{
    OpenDatabase();
    InsertToDatabase(name,address);
    CloseDatabase();
}
```

这是一般数据操作所共有的部分，也就是说这部分一般并不会发生变化。但`OpenDatabase()`,`InsertToDatabase()`,`CloseDatabase()`的操作却有千差万别。不同的数据库打开方式是不一样的，操作数据的操作也有区别，这些都是变化部分。经过思考我写出了以下的抽象类用来向数据库中添加姓名和住址。

```csharp
namespace TemplateMethod
{
    public abstract class DatabaseOperator
    {
        public DatabaseOperator()
        {
        }
        //公共接口，用来向数据库中添加记录
        public void AddToDatabase(string name ,string address)
        {
            OpenDatabase();
            InsertToDatabase(name,address);
            CloseDatabase();
        }

        //特有的操作
        protected abstract void OpenDatabase();
        protected abstract void InsertToDatabase(string name,string address);
        protected abstract void CloseDatabase();
    }
}
```

为了可以支持不同的数据库，我将特化部分的函数定义为`abstract`以便重载。现在我定义一个支持txt文档的具体类(Concrete class),这里我将其命名为：`TxtDatabaseOperator`.具体的定义如下：

```csharp
using System;
using System.Text;
using System.IO;

namespace TemplateMethod
{
    public class TxtDatabaseOperator:DatabaseOperator
    {
        private FileStream fs = null;
        public TxtDatabaseOperator()
        {
        }

        protected override void OpenDatabase()
        {
            fs = File.Open(@".\Database.txt",FileMode.Append,FileAccess.Write);
        }
        protected override void CloseDatabase()
        {
            fs.Close();
        }

        protected override void InsertToDatabase(string name, string address)
        {
            name += "|";
            byte[] byteName = new UTF8Encoding(true).GetBytes(name);
            fs.Write(byteName,0,byteName.Length);
            address += "\r\n";
            byte[] byteAddress = new UTF8Encoding(true).GetBytes(address);
            fs.Write(byteAddress,0,byteAddress.Length);
            fs.Flush();

        }

    }
}
```

上面的类`TxtDatabaseOperator`是针对txt文本数据库的操作，是将姓名及住址添加至`Database.txt`文档中。

下面我们使用该类记录相应的姓名和住址，代码如下：

```csharp
using System;

namespace TemplateMethod
{
    class CMain
    {
        [STAThread]
        static void Main(string[] args)
        {
            //操作Text数据库
            TxtDatabaseOperator txtOp = new TxtDatabaseOperator();
            txtOp.AddToDatabase("JerryChow","苏州新区");
            txtOp.AddToDatabase("AncoZhou","Suchow SND");
            txtOp.AddToDatabase("Tangtang","Suchow SIP");
        }
    }
}
```

这样我就可以在本地的`Database.txt`文档中记录以`|`分隔的姓名和住址，看起来是这个样子的：

```text
JerryChow|苏州新区
AncoZhou|Suchow SND
Tangtang|Suchow SIP
```

上面的操作图示如下：

![](http://blog.chinaunix.net/photo/11680_070926114025.gif)

看起来我的工作做完了，但这时另一个需求是需要将上面的信息添加至Access数据库中，毕竟Txt文档太透明化了，几乎什么编辑器都可以打开，谁都可以看到。

不过庆幸的是用了Tempate Method，这似乎可以帮助我们更好地应对这个需求的变化。我再从`DatabaseOperato`r派生出了针对Access数据文件操作的类，命名为：`MdbDatabaseOperator`.

```csharp
using System;
using System.Data.OleDb;

namespace TemplateMethod
{
    /// <summary>
    /// MdbDatabaseOperator 的摘要说明。
    /// </summary>

    public class MdbDatabaseOperator:DatabaseOperator
    {
        private OleDbConnection con = null;
        private OleDbCommand cmd = null;
        public MdbDatabaseOperator()
        {
            con = new OleDbConnection();
            cmd = new OleDbCommand();
            con.ConnectionString = @"Provider=Microsoft.Jet.OLEDB.4.0;Data Source=.\Database.mdb;Persist Security Info=False";
        }

        protected override void OpenDatabase()
        {
            con.Open();
            cmd.Connection = con;
        }
        protected override void CloseDatabase()
        {
            con.Close();
        }

        protected override void InsertToDatabase(string name,string address)
        {
            try
            {
                cmd.CommandText = string.Format("INSERT INTO UserInfo(Name,Address) VALUES('{0}','{1}')",name,address);
                cmd.ExecuteNonQuery();
            }
            catch(Exception e)
            {
                Console.WriteLine(e.Message);
                this.CloseDatabase();
                Console.ReadLine();
            }
        }


    }
}
```

通过这个类我们就可以操作Access数据库,而操作方式可以跟操作Txt文档的方式一模一样，这便是神奇的地方。我们在`Main()`函数中添加操作Access数据库的部分：

```csharp
using System;

namespace TemplateMethod
{
    class CMain
    {
        [STAThread]
        static void Main(string[] args)
        {
            //操作Text数据库
            TxtDatabaseOperator txtOp = new TxtDatabaseOperator();
            txtOp.AddToDatabase("JerryChow","苏州新区");
            txtOp.AddToDatabase("AncoZhou","Suchow SND");
            txtOp.AddToDatabase("Tangtang","Suchow SIP");


            //操作Access数据库
            MdbDatabaseOperator mdbOp = new MdbDatabaseOperator();
            mdbOp.AddToDatabase("JerryChow","苏州新区");
            mdbOp.AddToDatabase("AncoZhou","Suchow SND");
            mdbOp.AddToDatabase("Tangtang","Suchow SIP");

        }
    }
}
```

这时类图看起来是下面这个样子的：

![](http://blog.chinaunix.net/photo/11680_070926160407.gif)

对Template Method模式做个总结吧，当你需要固定某一操作顺序或是从一堆变化中找到了不变的那个部分运算(操作)。将即有的算法(操作)的部分写成Template方法，在Template方法中调用那些封装变化的虚函数。在Conrete类中重载那个封装变化的虚函数。

Template Method模式应该是我们常用的一个模式，虽然很多时候我们是在不知觉中运用了这个模式。模式的本质仍旧是将变化部分抽象出来，因为这些变化部分时常耦合在我们的设计中，所以将其分离出来并不是一件简单的事。设计模式给了我们很多解耦合，封装变化的通用设计，这无疑使我们减少了犯错的机率。站在巨人的肩膀上感觉真好!
