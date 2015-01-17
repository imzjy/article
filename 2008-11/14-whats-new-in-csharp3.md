C#3.0新特性简述
======

随着Visual Studio2008的发布，C#3.0也跟着和大家见面了。依个人之见，C#是当前最先进的语言——虽然我知道讨论哪门语言孰好孰坏从来都会被人攻击。到不是夸耀说C#设计多么优良，然后再无所不能，而是因为C#吸收了很语言的优点，而且是较年轻的语言，所以先进也再所难免。

我们来简单看看C#3.0一些新特性，这里需要你了解C#，了解一些委托的概念。

如果简单地讲C#3.0引入了一些动态语言，函数式语言的语素。这些语素是：

1. 扩展方法(Extension Method)，【动态地】给已有类型添加方法；
1. Lambda表达式(Lambda Expression)，创建匿名小函数；
1. 表达式树(Expression Tree), 将函数视做数据，function as data；
1. 匿名类型(Anonymous Type)；
1. 对象初始化表达式(Object Initialization Expression), 创建匿名类型的方法；
1. 隐式类型的局部变量（Implicitly Type Local Variables），引用匿名类型的方法；

下面我们依次，简要地介绍这些新特性，最终以一下示例结尾。

### 一， 扩展方法，给已有类型添加方法。

在一些动态语言中，一个类型的方法是可以动态添加的，而这在静态的编译型的语言中，却不太可能。例如我们现在有一个这样的需求，将一个字符串中的空格转为下划线；

我们在C#3.0以前的做法是，写一个静态方法，去做这个转换：

```csharp
static class Extend
{       public static string SpaceToUnderscore(string s)
        {
            char[] charArray = s.ToCharArray();
            string result = null;
            foreach (char c in charArray)
            {
                if (char.IsWhiteSpace(c))
                    result += "_";
                else
                    result += c;
            }
            return isUpper ? result.ToUpper() : result;
        }
}
```

然后在需要将空格转换为下划线的地方调用Extend类的静态方法

```csharp
string s = “I am jerry chou”;
string converted = Extend.SpaceToUnderscore(s);
```

而针对些需求，最好的办法是可以扩展string类型，给string类型增加一个方法SpaceToUnderscore，C#3.0允许你扩展一个已存在类的方法，包括string类型，因些你可以扩展string类型，例如：

```csharp
static class Extend
{
        /// <summary>
        /// String Extension Method,transform the white space to underscore.
        /// </summary>
        public static string SpaceToUnderscore(this string s) //Extension Method,Notice [this] position

        {
            char[] charArray = s.ToCharArray();
            string result = null;
            foreach (char c in charArray)
            {
                if (char.IsWhiteSpace(c))
                    result += "_";
                else
                    result += c;
            }
            return isUpper ? result.ToUpper() : result;
        }
}
```

注意this引用加在类型string之前，表示该方法是扩展已有类型string的方法。经过扩展之后我们可以这样写代码：

```csharp
string s = “I am jerry chou”;
string converted = str.SpaceToUnderscore(s); //调用例的SpaceToUnderscore方法。
```

这个特性，看起来很cool,确实如此！

但这个特性有些地方需要澄清:

1. 方法`SpaceToUnderscore`和string的实例`str`并非动态(Run-time)绑定，而是C#编译器，在编译期静态地(compile-time)，编译器会将你的代码转换为静态方法的调用;
1. Extension Method的优先级低于类型的实例化方法(Instance Method);
1. Extension Method跟随着他所在namespace,例如上面的extension method的有效范围是整个Extend所在的namespace；
1. 对于建模来说，优先使用继承来扩展一个类型；

### 二， Lambda表达式；

对于函数式语言来说，将函数作为参数传递最常见不过了。在非函数语言中你也可以将函数作为参数传递，例如在C中你可以将一个函数指针作为参数传递。但这样会带来二个问题，一是函数定义满天飞，源代码中充斥着小函数的定义，这些小函数太难于管理，这对于大型项目来说是个致命的灾难。二是由于每个函数都需要一个函数名(准确地讲是：method signature，包括函数名和参数类型)，这会导致命名冲突。

C#2.0给出的解决方案是匿名方法（Anonymous Methond）。C#3.0的Lambda表达式给出了更加优雅的解决方案。我们来看看MSDN中的一个例子：

```csharp
class Test
{
    delegate void TestDelegate(string s);
    static void M(string s)
    {
        Console.WriteLine(s);
    }
    static void Main(string[] args)
    {
        // Original delegate syntax required
        // initialization with a named method.
        TestDelegate testdelA = new TestDelegate(M);

        // C# 2.0: A delegate can be initialized with
        // inline code, called an "anonymous method." This
        // method takes a string as an input parameter.
        TestDelegate testDelB = delegate(string s) { Console.WriteLine(s); };

        // C# 3.0. A delegate can be initialized with
        // a lambda expression. The lambda also takes a string
        // as an input parameter (x). The type of x is inferred by the compiler.
        TestDelegate testDelC = (x) => { Console.WriteLine(x); };

        // Invoke the delegates.
        testdelA("Hello. My name is M and I write lines.");
        testDelB("That's nothing. I'm anonymous and ");
        testDelC("I'm a famous author.");

        // Keep console window open in debug mode.
        Console.WriteLine("Press any key to exit.");
        Console.ReadKey();
    }
}
/* Output:
    Hello. My name is M and I write lines.
    That's nothing. I'm anonymous and
    I'm a famous author.
    Press any key to exit.
*/
```

我们以这样的方式创建Lambda函数：

```csharp
(x) => x*x;
```

其中`=>`前面的是函数参数列表（无需给出参数类型，编译器自动推断），后面的x*x是函数体（表达式-表达式的值即函数的返回值，或语句块）。

我们可以通过委托来引用该函数，也可以用该函数构造表达式树。

###三，表达式树(Expression Tree),

将函数视做数据，Function as data.

### 四，三个相关的新特性：匿名类型，对象初始化器，隐式类型的局部变量

我们解决了匿名函数，还有一问题需要解决：匿名类型，在c#3.0中通过三个新增特性来解决这个问题。

1. 引入隐式类型；
1. 创建匿名类型的方法：Object Initializer，对象初始化器的调用也被称作对象初始化表达式。
1. 引用类型的方法：Implicitly Typed Local Variable，隐式类型的局部变量；

我们先来看一段C#3.0的代码：

```csharp
object obj = new { LastName = "Anderson", FirstName = "Brad" };
Console.WriteLine("Type:\t{0}\nToString:\t{1}", obj.GetType(), obj.ToString());
```

我们通过对象初始化表达式`new { LastName = "Anderson", FirstName = "Brad" }`创建了一个匿名类型，然后通过`object`(所有类型的基类)引用这个类型。通过打印结果：

```text
Type:   <>f__AnonymousType0`2[System.String,System.String]
ToString:       { LastName = Anderson, FirstName = Brad }
```

我们可以看出该类型是一个匿名类型，它的字符化表示，显示了该匿名类型的值。

但怎么样引用匿名类型中的成员？对于此c#3.0引入了隐式类型的局部变量。

```csharp
var itlv = new { LastName = "Jerry", Age = 26, IsMale = true };
Console.WriteLine("Implicitly Typed Loca Variables({0}):\nLast Name[{1}]\tAge[{2}]\tIsMale[{3}]\n",itlv.GetType(), itlv.LastName, itlv.Age, itlv.IsMale);
```

通用使用`var`关键字定义的变量，我们就可以引用匿名类型的成员了。

对于匿名类型，这儿也有几点需要注意:

1. 对于匿名类型，在编译期，编译器会给创建的匿名类型分配一个类型名，在运行期匿名类型和普通类型并没有什么不同。
1. 匿名类型直接派生自`object`。
1. 匿名类型的属性是只读的。

另外一点要提的是，微软的新技术`LINQ`(Language Integrated Query)，中需要大量利用这些C#3.0的新特性，学习LINQ技术的朋友不防先把这些新的特性学习完了之后再去看LINQ；

综合的例子：


```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Linq.Expressions;

namespace NewFeature
{
    class Person
    {
        public int ID;
        public int IDRole;
        public string FirstName;
        public string LastName;
    }

    static class Extend
    {
        /// <summary>
        /// String Extension Method,transform the white space to underscore.
        /// </summary>
        /// <param name="s"></param>
        /// <param name="isUpper"></param>
        /// <returns></returns>
        public static string SpaceToUnderscore(this string s, bool isUpper) //Extension Method,Notice [this] position
        {
            char[] charArray = s.ToCharArray();
            string result = null;
            foreach (char c in charArray)
            {
                if (char.IsWhiteSpace(c))
                    result += "_";
                else
                    result += c;
            }
            return isUpper ? result.ToUpper() : result;
        }


    }

    class Program
    {
        static void Main(string[] args)
        {
            CSharpNewFeatures();

            QueryAsMethod();

            Console.ReadKey();
        }

        static void CSharpNewFeatures()
        {
            //(1),Extension Method
            string str = "I'm jerry chou";
            Console.WriteLine("Extesion Method for string:\n{0}\n",str.SpaceToUnderscore(true));

            //(2),Lambda Expressions
            // delegate void Action(void);
            Action doAction = delegate() { Console.WriteLine("I'm nothing, just use Anonymous Method"); };
            Action doLambdaAtion = () => { Console.WriteLine("I'm anything, just use Lambda Expression\n"); };
            doAction();
            doLambdaAtion();

            //(3),Expression Tree
            Expression<Func<Person, bool>> e = p => p.ID == 1;
            BinaryExpression body = e.Body as BinaryExpression;
            MemberExpression left = body.Left as MemberExpression;
            ConstantExpression right = body.Right as ConstantExpression;
            Console.WriteLine("Expression Tree:\n{0}",left.ToString());
            Console.WriteLine(body.NodeType.ToString());
            Console.WriteLine(right.Value.ToString() + "\n");


            //(4),Anonymous Types,
            //(5),use Object Initializaion Expressions
            object obj = new { LastName = "Anderson", FirstName = "Brad" };
            object obj2 = new { LastName = "Jerry", Age = 26, IsMale = true };
            Console.WriteLine("Type:\t{0}\nToString:\t{1}", obj.GetType(), obj.ToString());
            Console.WriteLine("Type:\t{0}\nToString:\t{1}\n", obj2.GetType(), obj2.ToString());

            //(6),Implicitly Typed Local Variables
            var itlv = new { LastName = "Jerry", Age = 26, IsMale = true };
            Console.WriteLine("Implicitly Typed Loca Variables({0}):\nLast Name[{1}]\tAge[{2}]\tIsMale[{3}]\n",itlv.GetType(), itlv.LastName, itlv.Age, itlv.IsMale);
            //itlv.Age = 99; //Anonymous Type cannot be assigned to -- it is read only


        }
        /// <summary>
        /// LINQ中SQOs(Standard Query Operators)，最终会在Compile-Time被编译器转换为函数调用
        /// </summary>
        static void QueryAsMethod()
        {
            string sentence = "the quick brown fox jumps over the lazy dog";
            // Split the string into individual words to create a collection.
            string[] words = sentence.Split(' ');

            // Using query expression syntax.
            var query = from word in words
                        group word.ToUpper() by word.Length into gr
                        orderby gr.Key
                        select new { Length = gr.Key, Words = gr };

            // Using method-based query syntax.
            var query2 = words.
                GroupBy(w => w.Length, w => w.ToUpper()).
                Select(g => new { Length = g.Key, Words = g }).
                OrderBy(o => o.Length);

            foreach (var obj in query)
            {
                Console.WriteLine("Words of length {0}:", obj.Length);
                foreach (string word in obj.Words)
                    Console.WriteLine(word);
            }

            // This code example produces the following output:
            //
            // Words of length 3:
            // THE
            // FOX
            // THE
            // DOG
            // Words of length 4:
            // OVER
            // LAZY
            // Words of length 5:
            // QUICK
            // BROWN
            // JUMPS
        }
    }
}
```
