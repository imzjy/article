写个简单的Windows服务
==========

### 题记

为了防止近视的增加，我想写个Windows服务定期提醒自己在看了一段时间电脑后可以让眼睛休息一下。我使用了VS2005，没想到现在.net平台的包装能力真的很强大。只需简单几步就可以创建一下Windows服务。许久没有写过step by step式的文章了，正好回顾一下。

### 1，什么情况下需要写windows服务？

一般来讲，当你的程序是一个类似守护进程的时候，你可以考虑将其写成windows服务。

程序的特点是，没有运行界面。在不需跟用户进行交互的情况下完成一些功能。

### 2，程序功能简述。

定期提醒自己将自己的computer锁定起来，让自己的眼睛得到休息。在锁定电脑之前给出提醒，若确定则锁定电脑，若点击取消则在一小段时间后再次提醒。

### 3，Implement

#### Step1, Create a Windows service project.

Open the Visual Studio 2005 development environment，and create a Windows Service Project. As following:

![](http://blog.chinaunix.net/photo/11680_080429163238.gif)

You can change path according to your favorite.

#### Step 2. Rename the “Servie1” to “NoticeServie.”[Not necessary].

![](http://blog.chinaunix.net/photo/11680_080429163343.gif)

#### Step 3. Add the Installer.

Double click the “NoticeService” in solution explorer to open the “NoticeService” design model.

Then you can see the design model in the left. Click the right button of the mouse in design model. As following:

![](http://blog.chinaunix.net/photo/11680_080429163214.gif)

Add the Installer for "NoticeService". You can find the `ProjectInstaller.cs”`in solution explorer after you click the Add Installer. Like following

![](http://blog.chinaunix.net/photo/11680_080429163315.gif)

#### Step 4. Add the code for service.

Open the code of "NoticeService"

![](http://blog.chinaunix.net/photo/11680_080429163418.gif)

and add the code as following:

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.ServiceProcess;
using System.Text;
using System.Threading;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace RestNotice
{
    public partial class NoticeService : ServiceBase
    {
        #region Import Windows API to lock workstation
        [DllImport("User32.dll")]
        public static extern void LockWorkStation();
        #endregion

        #region Method
        public NoticeService()
        {
            InitializeComponent();
            //set servercie property
            SetServiceProperty();
        }
        private void SetServiceProperty()
        {
            this.ServiceName = "Rest Notice to keep the sight";
            this.AutoLog = true;
            this.CanStop = true;
            this.CanPauseAndContinue = true;
        }

        protected override void OnStart(string[] args)
        {
            // TODO: Add code here to start your service.
            time.Elapsed += new System.Timers.ElapsedEventHandler(OnTimer);
            time.Enabled = false;

            //ready to perform the Windos Servers

            time.Interval = NoticeInterval;
            time.Enabled = true;

        }
        private void OnTimer(object sender, System.Timers.ElapsedEventArgs e)
        {
            time.Enabled = false;
            if (DialogResult.OK ==
                    System.Windows.Forms.MessageBox.Show("Using computer over 2 hours,Lock computer and have a rest?",
                        "Notice",
                        MessageBoxButtons.OKCancel,
                        MessageBoxIcon.Question,
                        MessageBoxDefaultButton.Button1,
                        MessageBoxOptions.ServiceNotification
                ))
            {
                //lock computer
                LockWorkStation();
            }
            else
            {
                //retry the notice after five minutes.
                time.Interval = RetryInterval; // 5 minutes
                time.Enabled = true;
                return;
            }
            //restore the timer
            time.Interval = NoticeInterval; // 2 hours
            time.Enabled = true;
        }
        protected override void OnStop()
        {
            // TODO: Add code here to perform any tear-down necessary to stop your service.
        }
        #endregion

        #region Field
        private System.Timers.Timer time = new System.Timers.Timer();
        #endregion
        #region Property
        private int NoticeInterval
        {
            get
            {
                try
                {
                    int interval = int.Parse(System.Configuration.ConfigurationManager.AppSettings["NoticeInterval"]);
                    return interval * 1000 * 60; //1000*60milliseconds = 1minutes
                }
                catch (Exception ex)
                {
                    EventLog.WriteEntry(ex.Source, ex.Source);
                    return 120 * 1000 * 60; //120 minutes
                }
            }
        }
        private int RetryInterval
        {
            get
            {
                try
                {
                    int interval = int.Parse(System.Configuration.ConfigurationManager.AppSettings["RetryInterval"]);
                    return interval * 1000 * 60; //1000*60milliseconds = 1minutes
                }
                catch (Exception ex)
                {
                    EventLog.WriteEntry(ex.Source, ex.Source);
                    return 5 * 1000 * 60; //120 minutes
                }
            }
        }
        #endregion
    }
}
```

Don’t forget adding the reference of `System.Wndows.Forms` and `System.Configuration` to the project.

#### Step 5, Add Application Configuration file to the project.

Click Project->Add New Item->Application Configuration file.

![](http://blog.chinaunix.net/photo/11680_080429163227.gif)

Add the following contents to the app.config.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
  <appSettings>
    <!-- The time, in minutes, sets the interval of the notices. defalut 120 minutes-->
    <add key="NoticeInterval" value="120"/>
    <!-- The time, in minutes, sets the interval of retring the notice. default 5 minutes-->
    <add key="RetryInterval" value="2"/>
  </appSettings>
</configuration>
```

#### Step 6,Bulid the Project.

Press the `F6` to build the project.

#### Step 7, Register the windows servers

When building successes, a exe file can be found in `\ProjectPath\bin\debug\`, (adjust the ProjectName according to your directory) named `RestNotice.exe`. You must register the `RestNotice.exe` before you start the service.

Open the command console. And type the command as following:

![](http://blog.chinaunix.net/photo/11680_080429163332.gif)

`installutil RestNotice.exe` to register the service.

After you register the service, you will find related server called "RestNotice" in Service Manager Console.

![](http://blog.chinaunix.net/photo/11680_080429163405.gif)

Now, a windows service completed. You will be informed to have a rest.

![](http://blog.chinaunix.net/photo/11680_080429163255.gif)

Press the OK locking the computer and have a rest.
Press the Cancel ignoring the information, which would be displayed about 5 minutes later.

