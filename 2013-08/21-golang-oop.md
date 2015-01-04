Go对OO的选择
======

Go摒弃了许多OO的概念，但是还是很好的继承了OO的精髓——消息传递。我猜这个是学了Smalltalk的。通常我们说OO，我们会说这三大特性：对象，继承，多态。

### 1，Go中的对象
对于GO来说他的类型系统也分为两类：value type和reference type。value type就是内存中的内容，reference其实也是类似引用地址的指针。这样Go中的对象很自然的分为两类的：内容和引用内容的地址。Go的一个哲学就是让“天下没有隐晦的东西”。所以Go的对象在内存中的表示和其定义是一一对应的。有点“what you see is what you get”的感觉。

而在Go中，实现对象特征的是struct，其实这个好理解。当年C++之父Bjarne Stroustrup在从C语言捣腾C++的时候也是先扩展C中的struct，只不过，Bjarne Stroustrup太贪心，做的太多的。这个在学术上是有意义的，但在工程上并不买账。

Go中一切直白，没有隐藏的this指针。struct定义决定了struct内存的布局。但是Go添加了method，其实就是附加在struct上的一系列方法。我们可以通过struct的变量(相当我们OO中的实例)来调用这些方法。这些其实就是写语法糖而已。让原本C中的:

`sayHello(Person *p, char *msg);`

变成了类似于：
```golang
p := new(Person)
p.sayHello(msg string)
```

即使这小小的一变，在意义上变化大着了。这里的p是variable，Go称这样的variable为receiver。其实就是OO中的消息传递，而这个接受者就是p这个变量。

Go中有一点小的改进，调用语法上取消了对struct的变量和变量指针的区别。在上例中`p := new(Person)`中的p其实是new返回的指向Person变量的一个指针。但是我们仍然可以用点号来调用：`p,sayHello()`。

Go中的对象就这些，没有别的了。

### 2，Go中的继承
C++中的继承是很隐晦的，子类的constructor会自动调用父类的constructor，等等，等等。我们所谓的继承，其实是为了一种共享。这个共享，是通过嵌入来实现的。传统的OO语言中把这个工作交给编译器了，通过一些语法支持，编译器会创建一个父类对象的实例，然后通过类似base的指针去引用父类对象。好处就是创建时相对会简单，在工程上的缺点就是如果你不了解这些语法规则，那么你写的代码中有很多的坑——最可怕的是你并值知道有这些坑。

Go仍然是本着“all things are obvious”，组合就是组合，即把一个类型嵌入到另一个类型中。看个例子：

```golang
package main
 
import "fmt"
 
type Cellphone struct {
    brand string
    name string
    number string
    cost float32
}
 
func (c *Cellphone) showNumber() {
    fmt.Println("number:" + c.number)
}
 
type Person struct {
    Cellphone
    name string
    age int
}
 
func (p *Person)showPersonalInfo() {
    fmt.Printf("name:%s\tage:%d\t", p.name, p.age)
    p.showNumber();
}
 
func main() {
    p := Person{Cellphone{"moto", "Defy", "+86-13844448888", 2000}, "jerry", 31}
     
    p.showNumber()
 
    fmt.Println(p.brand) //output:moto
 
    fmt.Println(p.name)  //output:jerry
 
    p.showPersonalInfo()
 
}
```

直接将一个类型定义中引用需要嵌入的类型。Go做了一些语法上的支持：

1. 可以直接调用嵌入类型的方法，比如p.showNumber()。或是直接引用嵌入类型的字段p.brand
1. 可以嵌入多个类型。例子中没有显示。
1. 每个类型只能嵌入一次。
1. 当嵌入的类型和当前类型类型有重名的时候，当前类型覆盖(重写?)嵌入(父类？)类型的字段。这个模拟了子类overwrite父类父类的功能。比如例子中的p.name显示的是Person这个struct的name。
1. 当嵌入的类型超过一个，并且有字段有重名的情况。这时候我们可以明确地引用比如p.Cellphone.name。否则编译时会有类似:xxx ambigous的错误。

Go的继承也就这么多了，他的想法就是，让显性(obvious)的东西保持显性。即使使用了语法糖，也绝不在后面做小动作。

### 3，Go中的多态
短答案：Go中没有多态。面向对象中的多态其本质是方法的分发。通过类似于virtual table的东西记录下分发的规则。有复写的时候方法分发给当前实例(子类)方法，没有复写的时候分发给父类相应的方法。Go中不允许不同类型的赋值，所以从根本上不支持传统OO中的多态。

Go中通过interface来实现(契约式)方法的分发。interface定义了方法的签名，任意类型只要实现了该方法，我们就认为这个类型实现了这个接口。这个不需要在定义类型的时候指定该类型所要实现的接口的方式被称之为“非入侵式的接口(non-invasive interface)”。

Go虽然不容许不同类型间的赋值，但是接口是个例外(接口在Go的内部也是一种特别的type)。只要一个类型实现了该接口，我们就可以将该类型的变量赋值给该接口的变量：

```golang
//Interfaces
type Shaper interface {
    Area() float32
}
 
//Square
type Square struct {
    border float32
}
 
//we can assign the variable of Square to variable of Shaper(interface)
var ishaper Shaper = &Square{20.0}
```

这样Shaper的变量就可以引用任意一个实现了该接口类型的变量了。在底层接口变量其实是一个带着两个数据的指针：一块数据是该receiver(即引用的实际变量)，另一块是该接口实现的方法表指针。借助于这点Go多态也就完善了。Go中称这个位type assertion。其实也就是OO中的类型推断。我们可以通过类似这样的语法去看变量是否实现了接口，或者是从接口中得到具体的类型：

```golang
ishaper = s  //assign a variable to interface variable
fmt.Println(ishaper.Area())
 
//tye assertion, get value from interface
if v, ok := ishaper.(*Square); ok {
    fmt.Println(v)
}
 
//type assertion to test value implement a interface
//type assertion is only applied on interface, so we cast the s to empty interface
if v, ok := interface{}(s).(Shaper); ok {  
    fmt.Println(v.Area())
}
```

好了，现在不难写出来体现多态的方法了，记住本质就是方法分发(method dispatch)：

```golang
func PrintArea(s Shaper) {
    fmt.Printf("The area is %v\n", s.Area())
}
```

如果你想实现可以接受任意参数的函数怎么办？Go中的空接口可以实现这个功能，空接口其实就是没有任何方法的接口：

```golang
type Any interface{
 
}
```

任何类型都实现了空接口，也就是说Any接口的变量可以引用任意一个其他类型的变量，在利用type assertion，我们可以写出通用的方法：

```golang
func PrintArea(s interface{}) {
    if v, ok := s.(Shaper); ok {
        fmt.Printf("The area is %v\n", v.Area())    
    }
}
```

完整示例：

```golang
package main
 
import "fmt"
 
//Interfaces
type Shaper interface {
    Area() float32
}
 
//Square
type Square struct {
    border float32
}
 
func (s *Square)Area() float32 {
    return s.border * s.border
}
 
//Rectangle
type Rectangle struct {
    width float32
    height float32
}
 
func (r *Rectangle)Area() float32 {
    return r.width * r.height
}
 
//Polymorphism
func PrintArea(s interface{}) {
    if v, ok := s.(Shaper); ok {
        fmt.Printf("The area is %v\n", v.Area())    
    }
}
 
func main() {
    s := new(Square)
    s.border = 2.0
 
    var ishaper Shaper = s  //assign a variable to interface variable
    fmt.Println(ishaper.Area())
 
    //tye assertion, get value from interface
    if v, ok := ishaper.(*Square); ok {
        fmt.Println(v)
    }
 
    //type assertion to test value implement a interface
    //type assertion is only applied on interface, so we cast the s to empty interface
    if v, ok := interface{}(s).(Shaper); ok {  
        fmt.Println(v.Area())
    }
 
    //Type switches
    switch ishaper.(type) {
    case *Square:
        fmt.Println("Square type")
    }
 
    r := &Rectangle{10.0, 15.0}
    //a interface variable is a pointer in essence, so can pass the variable r(a pointer)
    PrintArea(s)    
    PrintArea(r)
}
```

Go的多态也讲完了。
