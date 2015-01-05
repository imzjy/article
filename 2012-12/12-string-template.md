模板引擎StringTemplate
=====

### 1,特点

1. 强制Model和View的分离，也就是View负责呈现，不能修改Model。同时View中不用来包括任何业务逻辑，详见作者的论文(中文,英文)。
2. Lazy-Evaluation，所有的Attribute直到st.ToString()调用时才evaluate.这样的好处是setAttribute是Order  Independent。
3. Recursive enable。

### 2,属性(attribute)

StringTemplate语法有两种组成元素，一种是属性(attribute)，另一种是普通字符(plain text)。在$…$中包围的是属性，其余的都是普通字符。比如：

`select $column$ from $table$ `

其中红色部分的$column$和$table$都是属性。在模板引擎呈现，即调用st.ToString()时，属性被实际值替换，而普通字符原封不动地输出。

我们可以通过下面的方式来向模板“填充”(push)属性：

```csharp
StringTemplate st = new StringTemplate("select $column$ from $table")
st.SetAttribute("column", "uid");
st.SetAttribute("table", "users");
 
Console.WriteLine(st.ToString());  //output: select uid from users
```

属性的填充方式很简单，就是调用attribute.ToString()方法的结果，如果attribute是null不会抛出异常，而是输出空字符串。

在.NET实现中attribute可以引用.net对象字段或属性(不区分大小写)，如果字段和属性同名则属性优先。attribute也可以是Dictionary或HashTable的Key，这样会找到该Key对应的值，然后在调用这个值的ToString()方法。示例：

```csharp
class Query
{
    public string column = "a";
    public string table = "t";
    public string Table { get { return "T"; } }
}
 
StringTemplate st = new StringTemplate("select $q.column$ from $q.TABLE$");
Query q = new Query();
st.SetAttribute("q",q);
 
Console.WriteLine(st.ToString());  //output: select a from T
```

#### 2.1,间接属性(indirect property names)

你可以通过下面的attribute.(anotherAttr)语法来引用间接属性：

```csharp
StringTemplate st1 = new StringTemplate("$q.(property)$"); //property是间接属性，也是一个attribute 
Query q = new Query();
st1.SetAttribute("q", q);
st1.SetAttribute("property", "table");
 
Console.WriteLine(st1.ToString());  //output: t
```

有些StringTemplate的保留字(reserved keyword)，是不能作为属性的：

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201212/201212122018033904.png)

如果attribute中的property和这些保留字重复了，StringTemplate就会报错，解决方案是使用间接属性：

```csharp
class Query
{
    public string first = "NumberOne";
}
 
StringTemplate st = new StringTemplate("select $q.(IndirectAttr)$");
 
Query q = new Query();
st.SetAttribute("q", q);
st.SetAttribute("IndirectAttr", "first");
Console.WriteLine(st.ToString());  //select NumberOne
//或者直接用Literal String: select $q.("first")$
```

#### 2.2,多值属性(multi-valued attribute)

所谓多值属性其实就是像数组一样的可迭代对象。多值属性通常有两种输出方式：

1. 类似于String.Join()的拼接。
2. 迭代。

*拼接*

```csharp
StringTemplate st = new StringTemplate("select $columns$ from users");
List<string> columns = new List<string>();
columns.Add("a");
columns.Add("b");
st.SetAttribute("columns", columns);
Console.WriteLine(st.ToString());  //output: select ab from users
 
 
StringTemplate st1 = new StringTemplate("select $columns; separator=\",\"$ from users");            
st1.SetAttribute("columns", "a");
st1.SetAttribute("columns", "b");    //此时columns变成multi-valued,作者讲其实SetAttribute应该叫做AddAtribute才对，对于同名attribute他不是替换而是添加
Console.WriteLine(st1.ToString());  //output: select a,b from users 
 
 
StringTemplate st2 = new StringTemplate("select $columns; separator=dilimiter$ from users");
st2.SetAttribute("columns", "a");
st2.SetAttribute("columns", "b");
st2.SetAttribute("dilimiter", ","); //separator也可以使expr
Console.WriteLine(st2.ToString());  //output: select a,b from users
```

*迭代*

```csharp
StringTemplate st = new StringTemplate("select $columns:{<i>$it$</i>}$ from users");  //迭代{...}中的anonymous template,并以自动填充it为当前元素
st.SetAttribute("columns", "a");
st.SetAttribute("columns", "b");  
Console.WriteLine(st.ToString());  //output: select  <i>a</i>  <i>b</i>  from users
 
StringTemplate st1 = new StringTemplate("select $columns:{col|<i>$col$</i>}$ from users"); //自动填充col为当前元素，同时it还是要填充的            
st1.SetAttribute("columns", "a");
st1.SetAttribute("columns", "b");
Console.WriteLine(st1.ToString());  //output: select  <i>a</i>  <i>b</i>  from users
```

*函数*
StringTemplate里面内置了一些函数用来操作multi-valued attributes，把他当做Lisp中的List一样操作，通过一些组合能实现牛逼功能。

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201212/201212121637312402.png)

```csharp
StringTemplate st = new StringTemplate("[$first(columns)$] [$last(columns)$] [$first(rest(columns))$]");  
st.SetAttribute("columns", "a");
st.SetAttribute("columns", "b");
st.SetAttribute("columns", "c");
Console.WriteLine(st.ToString());  //output: [a] [c] [b]
```

#### 2.3 属性的呈现(attribute render)

我们知道属性最后在模板中的呈现都是调用属性的ToString()方法，但是我们有时候想在模板呈现的时候改变某个属性的呈现，那么我们该怎么做呢？试想一下，我们对于DateTime，我们只想显示日期，而不想显示具体的时间，那我们怎么处理呢？一个办法是新建一个类型，然后重写ToString方法，但这样改动有点大，因为你需要在Model中所有用到这个DateTime的地方都要做类型转换。

StringTemplate提供的一个接口IAttributeRenderer用来做这种工作，该接口只负责一个类型的呈现，我们可以向一个模板注册这个呈现方式：

```csharp
class DateTimeRender:IAttributeRenderer
{
    public string ToString(object o)
    {
        DateTime dt = (DateTime)o;
        return dt.ToString("yyyy.MM.dd");
    }
}
 
 
StringTemplate st = new StringTemplate("$d$");
st.SetAttribute("d", DateTime.Now);
 
Console.WriteLine(st.ToString());
 
st.RegisterAttributeRenderer(typeof(DateTime), new DateTimeRender());  //register the attribute render for DateTime
Console.WriteLine(st.ToString());
```

### 3,StringTemplateGroup

#### 3.1 从文件中载入模板

模板时常是写在文件中的，比如一些作为html页面的模板。如果想从文件中装载模板我们可以使用StringTemplateGroup：

```csharp
string rootDirectoryOfTemplate = Path.Combine(AppDomain.CurrentDomain.BaseDirectory,"Query");
StringTemplateGroup group = new StringTemplateGroup("queryTemplate",rootDirectoryOfTemplate);
 
StringTemplate st1 =  group.GetInstanceOf("query");   //load  ROOT_PATH/query.st
st1.SetAttribute("func","sysdate()");
Console.WriteLine(st1.ToString());
 
StringTemplate st2 = group.GetInstanceOf("\\sub\\query");  //load  ROOT_PATH/sub/query.st
st2.SetAttribute("func", "sysdate()");
Console.WriteLine(st2.ToString());
```

#### 3.2 命名模板(Group Files)

如果想模块化模板，一个方式是使用单独的文件。但是如果模板很短小这样会产生很多文件，StringTemplate提供了Group Files用来定义短小的模板模块，你可以通过给通过名称来引用定义好的模板模块。命名模板的定义规则是：

```csharp
templateName(arg1, arg2, ..., argN) ::= "single-line template"
or
 
templateName(arg1, arg2, ..., argN) ::= <<
multi-line template
>>
or
 
templateName(arg1, arg2, ..., argN) ::= <%
multi-line template that ignores indentation and newlines
%>
```

命名模板还提供了模板参数，你可以通过SetAttribute来设置模板的参数。示例：

```csharp
string groupDef = @"
group mygroup;
 
vardef(type,name) ::= ""<type> <name>;""
 
method(type,name,args) ::= <<
<type> <name>(<args; separator="","">) {
  <statements; separator=""\n"">
}
>>
";

StringTemplateGroup stg = new StringTemplateGroup(new StringReader(groupDef));
var vardef = stg.GetInstanceOf("vardef");
vardef.SetAttribute("type", "int");
vardef.SetAttribute("name", "sum");
Console.WriteLine(vardef.ToString());  //output: int sum;
```
 

### 4,子模板(subtemplate)

#### 4.1 匿名子模板(anonymous subtemplate)
我们可以对属性或多值属性应用匿名子模板，语法我们在多值属性的迭代中已经见识了：$attr:{ <anonymous template> }$。匿名模板还可以嵌套：

```csharp
StringTemplate st = new StringTemplate("$x:{<b>$it$</b>}:{<li>$it$</li>}; separator=\"\n\"$");
st.SetAttribute("x", 1);
st.SetAttribute("x", 2);
st.SetAttribute("x", 3);
Console.WriteLine(st.ToString());
```

这样我们就可以对每个元素先应用`<b>`，然后在应用`<li>`。

对于多值属性，我们还可以对每个属性交替地应用不同的子模板，语法跟上面的就跟上面应用多个匿名模板很类似，将“：”变成“，”：

```csharp
StringTemplate st = new StringTemplate("$x:{<red>$it$</red>},{<blue>$it$</blue>}; separator=\"\n\"$");
st.SetAttribute("x", 1);
st.SetAttribute("x", "jatsz");
st.SetAttribute("x", 2);
st.SetAttribute("x","git");
Console.WriteLine(st.ToString());
```

#### 4.2 条件包含子模板

```text
$if(x)$
...
$elseif(y)$
...
$elseif(z)$
...
$else$
...
$endif$
```

除了false, null, empty(list,hastable)视作false以外，其他的值都被视作true。我们可以通过条件表达式来包含(include)不同的子模板：

我们共有三个模板文件，分别位于Views目录下的index.st, sub/login.st, sub/logout.st，文件的内容如下：

```text
===index.st
$if(loggedin)$
   $sub/logout(lnk=linkUrl)$
$else$
   $sub/login(lnk=linkUrl)$
$endif$
 
===sub/login.st
<a href="$lnk$">Please click to login</a>
 
==sub/logout.st
<a href="$lnk$">Please click to logout</a>
```

我们的程序代码如下：

```csharp
StringTemplateGroup stg = new StringTemplateGroup("index", AppDomain.CurrentDomain.BaseDirectory + "views");
var stIndex = stg.GetInstanceOf("index");
stIndex.SetAttribute("loggedin", true);
stIndex.SetAttribute("linkUrl","http://example.com/logout");
Console.WriteLine(stIndex.ToString());
 
 
stIndex.Reset();  //or stIndex.RemoveAttribute("loggedin");
stIndex.SetAttribute("loggedin", false);
stIndex.SetAttribute("linkUrl", "http://example.com/login");
Console.WriteLine(stIndex.ToString());
```

### 5,杂项

#### 5.1 未涉及的部分

* Group Interface
* Template Inheritance

#### 5.2 链接

本文示例使用的是StringTemplate v3版。

http://www.stringtemplate.org/

http://www.antlr.org/wiki/display/ST/StringTemplate+3.0+Printable+Documentation#StringTemplate30PrintableDocumentation-6Groupinterfaces
