怎么样解释依赖注入？[提问而非回答]
=======

网上一个朋友问人注入是怎么回事，我一时语塞。我并不能很好的用尽量通俗的语言来表达这个意思。我说，我写一个代码片段吧，也许这样容易理解些。但发现效果并不明显。

代码示例如下：

```csharp
public interface IDisplay
{
    void Display(string message);
}
 
public class LCD:IDisplay
{
    public void Display(string message)
    {
        Console.WriteLine("Display In LCD");
    }
}
public class CRT:IDisplay
{
    public void Display(string message)
    {
        Console.WriteLine("Display In CRT");
    }
}
 
 
public class Desktop
{
    public IDisplay displayDevice = null;
    public void ShowMessageOnScreen(string message)
    {
        displayDevice.Display(message);
    }
}
```

清风醉  5:15:08 PM

```csharp
public void Main()
{
    Desktop desktop = new Desktop();
     
    //注入LCD的实现
    desktop.displayDevice = new LCD();
    desktop.ShowMessageOnScreen("Display on LCD");
 
    //注入CRT的实现
    desktop.displayDevice = new CRT();
    desktop.ShowMessageOnScreen("Display on CRT");
 
}
```

附带地我又加了一些说明：

```text
清风醉  5:15:08 PM
Desktop(电脑)依赖显示设备(displayDevice)来显示信息
清风醉  5:15:31 PM
Desktop留一个接口IDisplay
cnblogs  5:16:01 PM
？？
清风醉  5:16:02 PM
你可以向这个接口IDisplay注入符合规范的实现（LCD或CRT）
清风醉  5:16:13 PM
听不懂？
cnblogs  5:16:29 PM
嗯 有点懵
清风醉  5:16:50 PM
呵呵
清风醉  5:16:58 PM
可能是我太术语化了
清风醉  5:17:09 PM
你懂面向对象吗？
cnblogs  5:17:29 PM
只能说理解
清风醉  5:18:49 PM
通常我们说的注入，就是通过多态，来改变被注入者的行为
```

当我说完这些时，我越发地语塞了。我知道我已经说不清楚了，越解释越让人迷糊。本来我准备将Martin Fowler的文章发给他看看，后来也放弃了。

进而一步，怎么样才能将一个技术问题向别人说清楚，明白？

努力向其靠近…
