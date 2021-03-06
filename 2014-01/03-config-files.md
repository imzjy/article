聊聊程序的配置文件
======

可能是移动应用的广泛普及，为了安全性的考虑现在的移动应用大都运行在一个沙箱中，无论是有系统支持的运行时沙箱还是逻辑上的沙箱。
比如现在的应用大多数只能写自己的安装目录，从而将自己的运行环境和其他应用的运行环境隔绝开来。

早些时候我写过nodejs和git的库和配置文件可以选择安装位置，比如 global, system, local等。这是一个进步，
他改变了我们对配置文件存放位置的思考。同时现在的云存储，云同步更进一步改变了我们对配置文件的思考。
通俗的讲，现在的配置文件更加的偏向了Unix配置文件的风格——高内聚的配置文件，即将配置文件和使用这个配置文件的程序放在一起。
然而这个原则也太过精简，在实际使用的时候我们还要对他做一些扩展。

 

我分开来说，先说说配置文件。

早些时候Windows使用注册表来统一管理程序的配置文件，并通过系统API来统一存取这些这个配置文件。
随着应用数量的增长这个注册表出现了两个明显的问题，其一是注册表越来越大。其二是对注册表的误操作会导致应用或者的系统崩溃。
在.NET作为Windows系统框架后，Windows做出了一些调整。这个调整是一个补救
，那就是.NET应用大多使用app.config这个配置文件来决定应用程序的行为。这个类似于早期的ini配置文件。注册表大多是系统级应用使用的，
对于第三方应用还是使用app.config来的方便和直接。

Unix在早期鼓励就将一个应用的配置文件放在应用的同一个目录。对于系统全局的配置还专门在文件结构中增加了/etc这个系统全局配置目录。
大多数引用会使用当前用户的配置，如果找不到才去/etc目录找。在一些rc(run command)中也是先执行/etc的rc，
然后再执行当前用户目录下的rc，这样当前用户有机会改变全局的设定。

其实如果你仔细看这些变化，高内聚是最值的注意的。配置文件离使用配置文件的程序更加近了。
这也就是把相关的东西放在一起。

 

再来看看库的依赖。

在Unix上/usr/lib和/usr/local/lib是系统库于用户自安装库的目录。像nodejs更加深化了这种结构，可以让库存在于三个等级，系统级，
用户级和项目级。node的应用会从项目级开始依次寻找依赖的库。这样做有个优点就是一个库的不同版本可以同时运行，同时为了节约空间，
可以在用户级和系统级共享一个库。

对于库的依赖Windows早期的做法是在链接期指定，后来的DLL出现了，可以依赖注册过的DLL。.NET就更加宽泛了一点，如果你不指定DLL，
程序会使用当前程序目录下的DLL，当然GAC中的DLL和本地的DLL发生冲突时Resolve到底引用的是哪个DLL还是很头疼。

由此来看，一个运行环境比如node或是Windows文件的loader，采用统一的，可预见的库依赖还是很有必要的。

 

理想的情况是，我们将包含程序的目录随意拷贝到一个的电脑中，这个程序就可以按照预期正确的执行，
而不用管这个电脑是使用了几年的电脑还是一台新装的电脑。为了保持新安装电脑和使用了几年的电脑的行为的同步，
云同步最近又流行了起来。让你惊讶的莫过于你买了一个新的iPad，当你用自己的账号登陆，没过几分钟，
这台新iPad和你刚刚失去的iPad使用上一模一样，你熟悉的应用还在，并且你对这些应用的配置还保存着，
你可以和以往一样使用这台新的iPad而不用花上半天时间来装软件，配置软件。

苹果的文件规范，提到了这点。对于一个应用，首先他是一个*.app文件夹，这个文件夹包含了运行这个程序所有的依赖。
所谓的安装和卸载软件就是这个文件夹拖到或是移出/Applications目录。其次*.app其实是一个沙箱环境，他将当前应用和其他应用隔离开来。
在这个沙箱环境中将数据分为“不可变”的应用程序代码及资源，需要“同步的可变”数据，比如用户配置文件，应用程序的状态记录等，
还有部分是“不需同步的可变”数据，比如日志，缓存，临时文件等。

 

我们在做架构决策的时候，或是写代码的时候，了解上面的这些，我们可以知道配置文件是放哪里，程序怎么样打包发布，
程序的数据该如何同步。而这些看似随意的决定，恰恰是体现”设计”的，最重要的他对程序产生一种不那么可见的影响，
让程序变的更好，或是更坏。

 

参考：

---

https://developer.apple.com/library/mac/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html

http://unix.stackexchange.com/questions/65700/is-it-safe-to-add-to-my-path-how-come
