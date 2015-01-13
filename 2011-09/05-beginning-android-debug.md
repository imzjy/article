Beginning Android Debug

For debugging my cellphone(Motorola Defy ME525) problem, I want to debug my cellphone using android toolbox.

### 1,preparations

Before starting to debug our android-enabled cellphone, you need download USB driver for a specific brand and model. To Defy ME525, downloading & installing the driver by link of USB and PC Charging Drivers - Motorola Mobility, Inc. USA.

We debug the android-enabled devices by ADB(Android Debug Bridge).It’s packaged in Android SDK. Please refer to  http://developer.android.com/sdk/index.html.

In Defy ME525, turning on the USB Debug option.

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201109/201109051637307911.png)

Android devices contains a little of Unix binary utilities. In order to facilitating the debug, installing BusyBox(contains a lot useful Unix utilities) in Android Market.

https://market.android.com/details?id=com.jrummy.busybox.installer&feature=search_result

Ok, all things done. Unplug USB cable and plug it back.

### 2,Debug the Android-enable devices

Open a windows command window(cmd.exe).Issue the follow commands to debug the android-devices.

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201109/201109051637314389.png)

Other command, such as logcat, sysctl, top, ps, can monitor android system status.For full functions of ADB, referring to official documentation.

http://developer.android.com/guide/developing/tools/adb.html
