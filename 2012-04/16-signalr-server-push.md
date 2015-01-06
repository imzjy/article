使用SignalR实现asp.net服务器端的推送(Server Push)
====================

我们在开发Web应用时，有时候需要将Server端的的信息Push到客户端。常见的一个场景就是微博应用，需要将一个用户的收听实时消息推送到Web端，也就是用户的更新用户的Timeline。

对此通用的解决方案就是Long Polling——支持XMLHttpRequest的浏览器都可以使用，使得其适用范围广。对此需要注意的就是Server端的处理能力，最好能用类似Node.js的Non-Block式的并发。GitHub有个项目SignalR使得的在asp.net中实现Server Side的Push变得简单。为了使用SignalR，我们需要在NuGet中搜索SignalR并安装。

安装完成后我们便可以使用SignalR了，我们先看Client端的实现：

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
 
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Welcome to Microblog</title>
    <script src="../Scripts/jquery-1.6.4.js" type="text/javascript"></script>
    <script src="../Scripts/jquery.signalR.js" type="text/javascript"></script>
    <script src="../signalr/hubs"></script>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        <div>
            <span>MicroBlog ID:</span><input type="text" id="uid" name="uid" value=" " />
            <input type="button" name="refreshTimeline" id="refreshTimeline" value="Refresh Timeline" />
        </div>
        <ul id="messages"></ul>
    </div>
    </form>
    <script type="text/javascript">
        $(function () {
            // Proxy created on the fly
            var conn = $.connection.microBlogServer;
 
            // Declare a function so the server can invoke it
            conn.newMessage = function (msg) {
                $('#messages').append('<li>' + msg + '</li>');
            };
            conn.notify = function(notice) {
                $('#messages').append('<li>[system notice]:\t' + notice + '</li>');
            }
 
            // Start the connection
            $.connection.hub.start();
 
 
            //call server side refresh when all things ready
            $("#refreshTimeline").click(function() {
                conn.refreshTimeline($('#uid').val());
            });
        });
    </script>
</body>
</html>
```
服务器端也十分简单：

```csharp
public class MicroBlogServer:Hub, IDisconnect
{
    private static Dictionary<string, bool> cancelQueue = new Dictionary<string, bool>();
 
    public void RefreshTimeline(string uid)
    {
        cancelQueue.Add(this.Context.ConnectionId, false);
 
        var msgTask = new Task(new Action<object>(PushUserMessage), uid);
        msgTask.Start();
         
    }
 
 
    private void PushUserMessage(object uid)
    {
        while (true)
        {
            if (cancelQueue[this.Context.ConnectionId])
            {
                cancelQueue.Remove(this.Context.ConnectionId);
                return;
            }
 
            string msg = GetNewMessage(uid.ToString());
            Caller.newMessage(msg);  //push new message to client
 
            string notice = GetSystemNotification();
            if (!string.IsNullOrEmpty(notice))
                Clients.notify(notice);
        }
    }
 
    public System.Threading.Tasks.Task Disconnect()
    {
        if (cancelQueue.Keys.Contains(this.Context.ConnectionId))
        {
            cancelQueue[this.Context.ConnectionId] = true;
        }
        return null;
    }
 
    #region User Message Generator
    private string GetNewMessage(string uid)
    {
        Thread.Sleep(3000);
        return string.Format("message from xxx to {0}  ({1})", uid, DateTime.Now);
    }
 
    private string GetSystemNotification()
    {
        if (new Random().Next(6) >= 5)
            return "system will shutdown for maintenance";
        else
            return string.Empty;
    }
    #endregion
}
```
