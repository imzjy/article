Jeffrey新书——《Windows Via C/C++》
======

早上的时候，起了些雾，坐厂车经过金鸡湖甚至不能看见湖面。

Jeffrey的08年新书《Windows Via C/C++》出版了，这本书应该是原书的第五版了，前一版《Programming Application for Microsoft Windows》，中文译作《Windows核心编程》，在Windows编程界应该是家喻户晓了。这本书并不是快餐，很可能并不能直接从书中抄些代码到自己的项目中。但却不可不读。

在技术作家中，我很喜欢Jeffrey。原因是Jeffrey能把复杂的东西讲的很明了，究其原因。我想应该有两方面，一是Jeffrey从事Windows开发，教学多年对Windows很了解。其次是Jeffrey很好的文风，善于从浅处讲起，然后再一步步地引出坚难晦涩的部分。有一个缓冲，很容易让人接受。这在本书的前言部分Jeffrey自己也做了说明。Jeffrey很强调基础部分的理解，即Jeffrey所说的Building block的理解。在Overview中Jeffrey是这样说的:

> Microsoft Windows is a complex operating system. It offers so many features and does so much that it's impossible for any one person to fully understand the entire system. This complexity also makes it difficult for someone to decide where to start concentrating the learning effort. Well, I always like to start at the lowest level by gaining a solid understanding of the system's basic building blocks. Once you understand the basics, it's easy to incrementally add any higher-level aspects of the system to your knowledge. So this book focuses on Windows' basic building blocks and the fundamental concepts that you must know when architecting and implementing software targeting the Windows operating system. In short, this book teaches the reader about various Windows features and how to access them via the C and C++ programming languages.

> Although this book does not cover some Windows concepts—such as the Component Object Model (COM)—COM is built on top of basic building blocks such as processes, threads, memory management, DLLs, thread local storage, Unicode, and so on. If you know these basic building blocks, understanding COM is just a matter of understanding how the building blocks are used. I have great sympathy for people who attempt to jump ahead in learning COM's architecture. They have a long road ahead and are bound to have gaping holes in their knowledge, which is bound to negatively affect their code and their software development schedules.
The Microsoft .NET Framework's common language runtime (CLR) is another technology not specifically addressed in this book. (However, it is addressed in my other book: CLR via C#, Jeffrey Richter, Microsoft Press, 2006). However, the CLR is implemented as a COM object in a dynamic-link library (DLL) that loads in a process and uses threads to execute code that manipulates Unicode strings that are managed in memory. So again, the basic building blocks presented in this book will help developers writing managed code. In addition, by way of the CLR's Platform Invocation (P/Invoke) technology, you can call into the various Windows' APIs presented throughout this book.

> So that's what this book is all about: the basic Windows building blocks that every Windows developer (at least in my opinion) should be intimately aware of. As each block is discussed, I also describe how the system uses these blocks and how your own applications can best take advantage of these blocks. In many chapters, I show you how to create building blocks of your own. These building blocks, typically implemented as generic functions or C++ classes, group a set of Windows building blocks together to create a whole that is much greater than the sum of its parts.

很早就说过了——Jeffrey每次的出手(指出书)都能让我快乐很久。不看电视，不想个人琐事，端一杯Coffee，拿起Jeffrey的书读上几页，快哉！


上个月的总结差点忘记写了，在办公室时没有写，但回家了还是补在了日记上，有时坚持是种习惯，习惯了，也就坚持下来了。

最近在公司基本上都是修改别人的代码，在几次让凌乱的代码把我折腾的坐立不安的时候，也越发让我知道“重构(Refactoring)”的重要性了，我对一些能预知功能的，小函数模块进行了重构，让一个大怪物缩小了近一半。可奈何我重构功底太浅，也只能做些功能性的，小的重构，并不能给整个项目代码带来很大的变化。在接下来的时间中，我需要抽出一些时间，借这个机会，将《重构——改善即有代码的设计》好好看一下了。

4月的份的《程序员》来了，我浏览了一下，其中有两篇文章个人觉得很好：一是熊节的对一个项目重构的分析；还有一个是蔡学镛写的有关软件“肥胖”的一个思考。常听见美女说“哎呀，我又长胖了！”，可又有几个人在意如今软件的肥胖问题呢。即然不愿意让自己的女友长的如此肥胖，那在写软件的时候也手下留情，别让自己的软件如此肥胖。

