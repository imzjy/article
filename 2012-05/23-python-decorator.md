Python中的装饰器(decorator)
=======

想理解Python的decorator首先要知道在Python中函数也是一个对象，所以你可以

- 将函数复制给变量
- 将函数当做参数
- 返回一个函数

函数在Python中给变量的用法一样也是一等公民，也就是高阶函数(High Order Function)。所有的魔法都是由此而来。

### 1，起源
我们想在函数login中输出调试信息，我们可以这样做

```python
def login():
    print('in login')
 
def printdebug(func):
    print('enter the login')
    func()
    print('exit the login')
 
printdebug(login)
```

这个方法讨厌的是每次调用`login`是，都通过`printdebug`来调用，但毕竟这是可行的。

### 2，让代码变得优美一点
既然函数可以作为返回值，可以赋值给变量，我们可以让代码优美一点。

```python
def login():
    print('in login')
 
def printdebug(func):
    def __decorator():
        print('enter the login')
        func()
        print('exit the login')
    return __decorator  #function as return value
 
debug_login = printdebug(login)  #function assign to variable
debug_login()  #execute the returned function
```

这样我们每次只要调用debug_login就可以了，这个名字更符合直觉。我们将原先的两个函数`printdebug`和`login`绑定到一起，成为`debug_login`。这种耦合叫内聚:-)。

### 3，让代码再优美一点

`printdebug`和`login`是通过`debug_login = printdebug(login)`这一句来结合的，这一句似乎也是多余的，能不能在定义login是加个标注，从而将printdebug和login结合起来？

上面的代码从语句组织的角度来讲很难再优美了，Python的解决方案是提供一个语法糖(Syntax Sugar)，用一个@符号来结合它们。

```python
def printdebug(func):
    def __decorator():
        print('enter the login')
        func()
        print('exit the login')
    return __decorator  
 
@printdebug  #combine the printdebug and login
def login():
    print('in login')
 
login()  #make the calling point more intuitive
```

可以看出decorator就是一个：使用函数作参数并且返回函数的函数。通过改进我们可以得到：

- 更简短的代码，将结合点放在函数定义时
- 不改变原函数的函数名

在Python解释器发现`login`调用时，他会将`login`转换为`printdebug(login)()`。也就是说真正执行的是`__decorator`这个函数。

### 4，加上参数

#### 4.1，login函数带参数

`login`函数可能有参数，比如login的时候传人user的信息。也就是说，我们要这样调用login：

```python
login(user)
```

Python会将login的参数直接传给`__decorator`这个函数。我们可以直接在`__decorator`中使用user变量：

```python
def printdebug(func):
    def __decorator(user):    #add parameter receive the user information
        print('enter the login')
        func(user)  #pass user to login
        print('exit the login')
    return __decorator  
 
@printdebug 
def login(user):
    print('in login:' + user)
 
login('jatsz')  #arguments:jatsz
```

我们来解释一下`login('jatsz')`的调用过程：

```text
[decorated] login('jatsz') =>  printdebug(login)('jatsz')  =>  __decorator('jatsz')  =>  [real] login('jatsz')
```

#### 4.2，装饰器本身有参数

我们在定义decorator时，也可以带入参数，比如我们这样使用decorator，我们传入一个参数来指定debug level。

```python
@printdebug(level=5)
def login
    pass
```

为了给接收decorator传来的参数，我们在原本的decorator上在包装一个函数来接收参数：

```python
def printdebug_level(level):  #add wrapper to recevie decorator's parameter
    def printdebug(func):
        def __decorator(user):    
            print('enter the login, and debug level is: ' + str(level)) #print debug level
            func(user)  
            print('exit the login')
        return __decorator  
    return printdebug    #return original decorator
 
@printdebug_level(level=5)   #decorator's parameter, debug level set to 5
def login(user):
    print('in login:' + user)
 
login('jatsz')
```

我们再来解释一下`login('jatsz')`整个调用过程：

```text
[decorated]login(‘jatsz’) => printdebug_level(5) => printdebug[with closure value 5](login)(‘jatsz’) => __decorator(‘jatsz’)[use value 5]  => [real]login(‘jatsz’)
```

### 5，装饰有返回值的函数

有时候login会有返回值，比如返回message来表明login是否成功。

```python
login_result = login('jatsz')
```
我们需要将返回值在decorator和调用函数间传递：

```python
def printdebug(func):
    def __decorator(user):    
        print('enter the login')
        result = func(user)  #recevie the native function call result
        print('exit the login')
        return result        #return to caller
    return __decorator  
 
@printdebug 
def login(user):
    print('in login:' + user)
    msg = "success" if user == "jatsz" else "fail"
    return msg  #login with a return value
 
result1 = login('jatsz');
print result1  #print login result
 
result2 = login('candy');
print result2
```

我们解释一下返回值的传递过程：

```text
...omit for brief…[real][msg from login('jatsz') => [result from]__decorator => [assign to] result1
```

### 6，应用多个装饰器

我们可以对一个函数应用多个装饰器，这时我们需要留心的是应用装饰器的顺序对结果会产生。影响比如：

```python
def printdebug(func):
    def __decorator():    
        print('enter the login')
        func() 
        print('exit the login')
    return __decorator  
 
def others(func):    #define a other decorator
    def __decorator():
        print '***other decorator***'
        func()
    return __decorator
 
@others         #apply two of decorator
@printdebug
def login():
    print('in login:')
 
@printdebug     #switch decorator order
@others
def logout():
    print('in logout:')
 
login()
print('---------------------------') 
logout()
```

我们定义了另一个装饰器others，然后我们对login函数和logout函数分别应用这两个装饰器。应用方式很简单，在函数定义是直接用两个@@就可以了。我们看一下上面代码的输出：

```shell
$ python deoc.py
***other decorator***
enter the login
in login:
exit the login
---------------------------
enter the login
***other decorator***
in logout:
exit the login
```

我们看到两个装饰器都已经成功应用上去了，不过输出却不相同。造成这个输出不同的原因是我们应用装饰器的顺序不同。回头看看我们login的定义，我们是先应用others，然后才是printdebug。而logout函数真好相反，发生了什么？如果你仔细看logout函数的输出结果，可以看到装饰器的递归。从输出可以看出：logout函数先应用printdebug，打印出`enter the login`。`printdebug`的`__decorator`调用中间应用了others的`__decorator`，打印出`***other decorator***`。其实在逻辑上我们可以将logout函数应用装饰器的过程这样看（伪代码）：

```
@printdebug    #switch decorator order
(
    @others
    (
        def logout():
            print('in logout:')
    )
)
```

我们解释一下整个递归应用decorator的过程：

```text
[printdebug decorated]logout() =>
printdebug.__decorator[call [others decorated]logout() ] =>
printdebug.__decorator.other.__decorator[call real logout]
```

### 7，灵活运用

什么情况下装饰器不适用？装饰器不能对函数的一部分应用，只能作用于整个函数。

login函数是一个整体，当我们想对部分函数应用装饰器时，装饰器变的无从下手。比如我们想对下面这行语句应用装饰器：

```python
msg = "success" if user == "jatsz" else "fail"
```

怎么办？

一个变通的办法是“提取函数”，我们将这行语句提取成函数，然后对提取出来的函数应用装饰器：

```python
def printdebug(func):
    def __decorator(user):    
        print('enter the login')
        result = func(user) 
        print('exit the login')
        return result      
    return __decorator  
 
def login(user):
    print('in login:' + user)
    msg = validate(user)  #exact to a method
    return msg  
 
@printdebug  #apply the decorator for exacted method
def validate(user):
    msg = "success" if user == "jatsz" else "fail"
    return msg
 
result1 = login('jatsz');
print result1
```

来个更加真实的应用，有时候validate是个耗时的过程。为了提高应用的性能，我们会将validate的结果cache一段时间(30 seconds)，借助decorator和上面的方法，我们可以这样实现：

```python
import time
 
dictcache = {}
 
def cache(func):
    def __decorator(user):    
        now = time.time()
        if (user in dictcache):
            result,cache_time = dictcache[user]
            if (now - cache_time) > 30:  #cache expired
                result = func(user)
                dictcache[user] = (result, now)  #cache the result by user
            else:
                print('cache hits')
        else:
            result = func(user)
            dictcache[user] = (result, now)
        return result      
    return __decorator  
 
def login(user):
    print('in login:' + user)
    msg = validate(user)  
    return msg  
 
@cache  #apply the cache for this slow validation
def validate(user):
    time.sleep(5)  #simulate 10 second block
    msg = "success" if user == "jatsz" else "fail"
    return msg
 
result1 = login('jatsz'); print result1  
result2 = login('jatsz'); print result2    #this login will return immediately by hit the cache
result3 = login('candy'); print result3
```

---
Reference：

http://stackoverflow.com/questions/739654/understanding-python-decorators      --Understanding Python decorators

http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html   --Python装饰器学习（九步入门）

http://www.python.org/dev/peps/pep-0318/   --PEP 318 -- Decorators for Functions and Methods
