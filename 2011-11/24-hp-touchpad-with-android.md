HP Touchpad with Android
===============

Recently, I buy a tablet called HP TouchPad, it has excellent hardware: 1.2Ghz CPU, 1G RAM, 9.7inch Screen. The built-in operating system for TouchPad is HP webOS. In point of UI view, webOS is beautiful and apple-like. But there is main weakness of webOS: lack of software applications. Like apple store or android market, HP also have the online application marketing called App Catalog. But there are just have little of apps.

The CM team do a amazing job, they made Android port for the TouchPad. To experience the Touchpad with Android system, I updated my TouchPad to Android. Generally this rom is fast and useful even if in alpha version. Of course some bugs in alpha version, to feedback to the CM team. I need connect the my TouchPad with wired USB line with adb tools.

1, Install the CyanogenMod 7 to HP TouchPad
There a lot of tutorials on internet, you can follow the tutorials to install CyanogenMod android.

http://liliputing.com/2011/11/how-to-install-cyanogenmod-7-1-android-alpha-3-on-the-hp-touchpad.html

http://www.opinionless.com/updating-your-hp-touchpad-to-cyanogenmod-android-alpha-3/

 

2,Connect the HP TouchPad with adb
Follow the post:http://rootzwiki.com/topic/7281-wired-adb-not-working-for-you-fix-is-right-here/

First, you need update the USB driver by Android SDK Manager.

After that you re-plug your TouchPad, you will see “Android Tablet” in your Device Manager. Right click “Android Tablet” and select “Update Driver Software…”.

 

You will find driver(labeled with HTC….) suitable for TouchPad. In this point you do all of your job. Open “cmd.exe” and issue the “adb devices” command to check result.

 

3,How to use logcat
a, view logs

>adb shell logcat   //view and block for incoming log

>adb shell logcat –d  //view and exit

b,view Warnings

>adb shell logcat –d *:W    //show all of warnings

>adb shell logcat –d ActivityManager:W  //only show warnings associated with ActivityManager

c,view recently 10 line logs and exit

>adb shell logcat –t 10

d,view log with specific format

>adb shell logcat –d –v long  

alternatives:

brief — Display priority/tag and PID of originating process (the default format). 
process — Display PID only. 
tag — Display the priority/tag only. 
thread — Display process:thread and priority/tag only. 
raw — Display the raw log message, with no other metadata fields. 
time — Display the date, invocation time, priority/tag, and PID of the originating process. 
long — Display all metadata fields and separate messages with a blank lines.

e,clear logs & helps

>adb shell logcat –c  //clear logs

>adb shell logcat –help //help information
