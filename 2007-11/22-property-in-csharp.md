C#中的属性(Property)
===========

最近一直在看Jeffrey的《.net框架设计 Via C#》，很好的一本讲述C#.net本质的书。推荐给所有C#以及.net平台的Programmer。看着看着偶有所得便就想拿出来写写，和大家分享。顶着南瓜大的头(最近天气变冷，近几年来首次感冒了，最大的感觉是就头变得有南瓜那么大......)，写一写属性(Property)，今天是感恩节，也算是我感恩自己可以读到这很么多前辈们写的好书，感恩自己南瓜大的脑袋还能看得懂前辈们的技术文章。

### 1, What is property?

此处属性(Property)，指的是C#提供的一种以方便的语法访问一个方法的手段。而非另外一种属性(Attribute).下同。

属性是什么？本质上讲属性是方法，表面上看属性是字段。这样讲或许有些绕，看如下代码：

```csharp
//Platform: WinXp + Visual Studio2003(C#)
using System;
using System.Text;
namespace Class1
{
    class Person
    {
        public Person(string name, int age)
        {
            _name = name;
            _age = age;
        }
        private string _name;
        private static int _age=0;

        public static int Age   //属性---本质是函数         (1)
        {
            get
            {
                return _age;
            }
            set
            {
               if(value<1 || value>100)
                   throw new ArgumentOutOfRangeException("value","人能活到100岁以上,请思考一下.");
               else
                   _age = value;
            }
        }
        public string this[int n]  //有参属性
        {
            get
            {
                StringBuilder sb = new StringBuilder();
                for(int i=0; i<n;i++)
                {
                    sb.Append(_name);
                }
                return sb.ToString();
            }
            set
            {
                _name = value;
            }
        }
    }
    class ExcelProgram
    {
        [STAThread]
        static void Main(string[] args)
        {
            Console.WriteLine(Person.Age);   //属性--用起来像字段 (2)
            Person per = new Person("Jerry",25);
            Console.WriteLine(per[4]+ " "+Person.Age);          (3)

            Console.ReadLine();
        }
    }
}
```

这里我定义了一个很简单的类`Person`,该类有两个字段(fileds)，分别是`_name`和`_age`代表着一个人的"姓名"和"年龄".代码中的(1)处(以红色字标出),我定义了一个属性`Age`。而在(2),(3)处，我分别使用了属性和有参属性(待会讲述)。

### 2，How can we use property in C#?

**Define a property**

在C#中，定义一个属性很简单：

```csharp
public int Age
{
   set{};
   get{};
}
```

其中`public`指出了该属性的可访问性；`int`指出了属性的返回类型；`Age`是属性名。其中的`get`和`set`是两个方法分别用来设置和获取属性。

对于CLR/CLS来讲并没有属性(Property)这个概念，属性(Property)这个概念是虚拟出来的，是为了使用的方便，上面的代码，等同于下面这样定义的方法(记住了--属性的本质是方法):

```csharp
public int set_Age()
{}
public int get_Age(int value)
{}
```

在属性中，你甚至可以分别为`set`和`get`定义不同的可访问性，像这样：

```csharp
public int Age
{
   protected set{};
   get{};
}
```

**Use a property**

使用属性比定义属性还简单。属性的使用和字段使用方法是一样的，例如你可以这样用字段(在上例中若定义一个无参构造(default ctor)并将字段(fields)的访问性设为`public`即可)：

```csharp
Person perJerry = new perJerry{)
perJerry._name = "Jerry";
perJerry._age = 25;
```

属性允许你也同样的语法来实现：

```csharp
Person perJerry = new perJerry{)
perJerry.Name = "Jerry";
perJerry.Age = 25;
```

**Essential of property**

属性(Property)的本质是方法，口说无评，我们来看看刚才上面的一段程序，对于CLR来看是什么样子的。我们利用ILDasm来反汇编刚来的那段程序，如下图

![](http://blog.chinaunix.net/photo/11680_071122153144.gif)

图上红色的三角形，标着pro Age说明Age是一个属性(Property)，其实这部分是属性的元数据，为什么这样讲呢，我们双击打开pro Age可以看到如下内容

![](http://blog.chinaunix.net/photo/11680_071122154013.gif)

该部分只有方法的定义，并没有实现部分，那么属性的实现部分在哪里呢？你可能会注意到了，真正实际`get`的方法是`get_Age()`.第一幅图中红色三角形上面的四个method实际上实现了属性(的操作).让我们再双击method`set_Age`看看

![](http://blog.chinaunix.net/photo/11680_071122154622.gif)

可以看出`set_Age`方法，实现了Age属性中的set操作.为了再次验证属性的本质是方法，我们在Person类中再添加一个方法`get_Age()`,形如：

```csharp
public int get_Age()
{
  return _age;
}
```

当试图编译代码时，会出现以下错误信息：

`类"Class1.Person"已经定义了一个具有相同参数类型的名为"get_Age"的成员`

既然属性(property)的本质是方法(method)，这下就简单了。下面这些属性的特性也理所当然了：

1. 你可以定义静态(static)属性，上例中我便给出了static属性；
1. 你可以分别定义set,get。也可以只定义一个set(只写属性)或是只定义一个get(只读属性)；
1. 你可以分别为set,get设定访问类型--就像你可以分别是set_Age method和get_Age method分别设定访问类型一样；
1. 属性也可以有参数；

### property with parameter.

你也许会问第一幅图中的`get_Item`和`set_Item`是什么，这便是有参属性。有参属性也称作索引器(Indexer).有参属性只能像下面这样定义(利用参数检索一个类(或实例)的相关信息)

```csharp
public string this[int n]
{
  get
  {
    StringBuilder sb = new StringBuilder();
    for(int i=0; i<n;i++)
    {
      sb.Append(_name);
    }
    return sb.ToString();
  }
}
```
当编译器看到这样的定义时，会自动添加一个属性`pro Item`,并用`set_Item`和`get_Item`两个method来实现该属性。之后我们便可以像这样的使用属性:

```csharp
Person per = new Person("Jerry",25);
Console.WriteLine(per[4]);
```

### Something you must notice.

- 一般在编译过程中若生成release版本(打开release选项)，属性会被内联。而在Debug版本则不会被内联系，因为如果内联代码的话，很难单步执行调试.
- 属性并不是CLR/CLS支持的，因此并不是所有.net语言都支持属性。当你所使用的语言不支持属性时，你完全可以定义方法来实现相应的功能。
