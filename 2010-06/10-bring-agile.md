来一点敏捷
=======

这两天在看敏捷的相关东西。看来看去，大体上敏捷的设计原则讲的都是一个东西。以前对开放-封闭原则（Open-Closed Principle）总是感觉模糊，现在感觉也就是利用接口隔离，依赖于稳定的抽象的另一种说法。

### 来点例子

我们有一个网页，需要根据报表页面生成PDF供用户下载。

```csharp
void ResponseToUser(string fileName)
{
    PDFGenerator pdfGenerator = new PDFGenerator();
    Send(pdfGenerator.Generate(fileName)));
}
```

然而没过多久，用户需要生成XLS表——因为用户需要利用XLS来进行统计。

```csharp
void ResponseToUser(string fileName)
{
    XLSGenerator xlsGenerator = new XLSGenerator();
    Send(xlsGenerator.Generate(fileName)));
}
``` 

### 分析变化

在满足这个需求时，我们的改动点有两个：一个是实现`XLSGenerator`类，另一个是改动`ResponseToUser`函数。此时`ResponseToUser`函数依赖于生成器的细节。由于需求变化，我们知道这个细节不是稳定的，我们必须找一个相对稳定的抽象，基于这个稳定的抽象来保持`ResponseToUser`函数的稳定性，同时确保可扩展性。

来看看代码吧：

```csharp
void ResponseToUser(IGenerator generator, string fileName)
{
    Send(generator.Generate(fileName)));
}
```

此时`Send`依赖于稳定的抽象来生成不同类型报表。对于`OCP`原则来说，`ResponseToUser`函数此时是可扩展——传入不同的生成器。不可修改——`ResponseToUser`函数不需要修改，而由调用者来决定是需要PDF来是需要XLS。

