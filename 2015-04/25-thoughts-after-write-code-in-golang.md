Go语言-笔记和开发感受
====================

### 类型嵌入

Go语言使用类型嵌入来模拟通常面向对象中得继承。

- 接口嵌入的只能是接口，不能事结构
- 结构可以嵌入结构和接口
- 可以直接嵌入也可以当做变量嵌入

#### 直接嵌入和当做变量嵌入

```go
type A struct {
  Name string
}

//直接嵌入
type B struct {
  *A
  Age int
}

//当做变量嵌入
type C struct {
  V *A
  Gender string
}
a := *A{"zjy"}
b := &B{a, 32}
c := &C{a, "male"}

//直接嵌入可以使用被嵌入类的字段
fmt.Println(b.Name == "zjy")

//当做变量嵌入需要使用qualifier
fmt.Println(c.V.Name == "zjy")
```
#### 接受对象

b.Name的接受对象(receiver)是B内部的A，而不是B。如果A有相关方法，那么相关方法的的接受对象是B累不的A结构体，而不是B，B没有这个方法，也不是这个方法的Receiver。

这样的组合(composition)很纯粹，就是将两个结构绑在一起，起了一个新的名字而已。

#### 名称冲突

组合的一个问题就是名称冲突，解决是规则很简单

- 外层的名称覆盖内层的名称。(outter name hide the more deeply nested name)
- 同一层有相同名称会出现 Ambiguous，如果你访问了这个重名字段编译时会报错。如果你根本不使用这个字段，压根就没有什么问题。
- 如果避免报错，访问重名的类型，你可以加上类型的qualifer，类似`c.V.Name`。

命名冲突的解决也是基于类型组合的，在本质上就两块内存，名字重了，你需要特别指明你想访问的时那一块内存。

### 大小写控制的访问范围

Go语言使用名称的大小写来控制访问范围，从结构上Go得项目有一下组成

- 包(Package)
- 结构(Struct)

包变量和方法如果是小写的，那么访问的范围就是整个包（如果包由几个文件组成，这几个文件都可以访问这个变量），也就是说只要属于这个包得都可以访问这个变量。

结构体变量和方法如果是小写的，那么访问的范围*也是*同一个包。也就是说同一个包中的符号(无论大小写)，整个包中都可以使用。访问只加在package-level.

### 写Go代码给我带来的两点思考

使用Go语言开发，使得我站在更低的一个层次看以前的那些面向对象的代码是怎么工作的。同时让思考可以通过一些简单的抽象来实现程序的功能。他让我思考怎么样组合现有的结构来实现程序，这个锻炼了我的感觉。

有了这个感觉，我发现我对程序的复杂度把控又提高了。也就是说，我能感觉到当前新增的代码增加的是指数级的复杂度还是线性的复杂度。比如我们通常喜欢写一些通用的代码，像Http应用的Filter，但是通常Filter带给程序的是指数级的复杂度，用好了这个复杂度可以将问题一次性解决。但是如果你解决的是一个单独的问题，你加上了Filter你带来的好处是指数级的，但是给程序添加的复杂度是指数级的，这分明是得不偿失的。

我们写程序是，在遇到抉择的时候，最要考虑的一点就是你的改动影响的范围，给程序增加的复杂度是指数级还是线性的。我们通常选择那些线性的，虽然看起来线性的可能啰嗦一点，但是随着程序的增大，你的难度也是可控的。

而指数级的东西通常都是完全解决一个切面的问题，这个切面的领域相对独立。这样你使用一个指数级的复杂度的构造去解决指数级的问题。

### Go语言错误处理的优缺点

Go语言的Error Handling是立即检查式的，一旦有错误可能发生的地方，立马返回一个错误值(其实Error是一个Struct，是一个值语义)。这样的好处就是你可以保持错误点得环境，比如变量值，当前的Stack Frame等等信息。但是坏处就是错处处理散布的在程序各个地方，影响的程序的可读性。让人看不清程序的主要逻辑。

另一种Exception-based的方式恰恰相反，错误处理集中，但是丢失了很多错误发生时的细节。

如果一个应用对错误很敏感，比如文件系统，驱动，底层服务，那么立即检查式的方式能更好保证程序的行为。但是如果是逻辑复杂，可以容忍错误的环境，比如说Web开发中，还是Exception-based的方式更加易于使用。

### Go语言不太适合的地方

Go语言似乎填补了一个空白，那就是基础服务的语言。这样的语言不需要像C那般繁重，也不能像C++，Python那样不可控。所以像Docker这样的东西特别适合用Go来实现，但是文件系统，驱动程序还是要C来实现。

Web应用的基础部分可以使用Go来开发，但是如果偏向业务逻辑复杂的场景，使用Go来开发又不够灵活，不如Python，Ruby，JavaScipt来得更直接。比如你像给客户端回复的JSON增加一个属性，如果你是Go你至少需要使用一个匿名类型来实现，但是如果是动态语言，你直接添加这个属性就好的。如果像这样的业务端的数据结构经常变化，你用Go来实现会非常的累，针对业务所一些小修改，你还是要绕个弯或者加个层。sigh!