Ruby中的Mixin
======

当我们谈到继承，我们通常会分开为接口继承和实现继承。如果是单继承，无论是实现继承还是接口继承，都容易理解和使用。即便如此，在C++的著作中，还是提到当我们在继承一个类的时候，不仅仅要想到继承了实现，还要想到一并继承了接口。

多继承更是复杂，很容易走到菱形继承这样一个怪圈。在C#中，只有接口的多继承，并没有实现的多继承——我们不可以指定两个或两个以后的类作为父类。

Ruby中的Mixin是对多重实现继承的一个实现，即实现部分以模块的方式单独出来，模块有其特有的属性，比如不能实例化，不能继承别的类和被别的类继承等 。松本有一个例子很好：

```ruby
module WriteStream
    def write(str)
        puts str
    end
     
    def conflict
        puts "conflict"
    end
end
 
module ReadStream
    def read
        puts "read data"
    end
 
    def conflict
        puts "conflict-read"
    end
end
 
class Stream
    def getstream
        puts "get stream"
    end
end
 
class ReadWriteStream < Stream
    include WriteStream
    include ReadStream
end
 
rw = ReadWriteStream.new
rw.getstream
rw.read
rw.write("haha")
rw.conflict
```
 
这个例子就是网络编程中常常会用到的`Stream`, `ReadStream`, `WriteStream`, `ReadWriteStream`，在C++中这常常是一个菱形继承，而Ruby巧妙地采用了Mixin，从而避免了菱形继承。

在Ruby下的运行结果为：

```text
get stream
read data
haha
conflict-read
```
 

即使这样，还是回避不了最根本的问题：方法Resolve，即决定到底使用谁的方法。我们在上例中故意制造了一个冲突的方法conflict，我们从运行结果可以看到方法Resolve中结果是ReadStream的conflict方法。我们可以将程序的28行和29行对调：

```text
include ReadStream
include WriteStream
```

这时我们再次运行这段脚本，结果如下：

```text
get stream
read data
haha
conflict
```

注意最后一行，调用conflict方法结果的差别，我们可以知道Ruby中的Mixin是基于include时的顺序来决定方法调用的顺序。
