Detect hotkeys conflict using Spy++
=========

As mentioned before, I am often frustrated by hotkey conflicts when I using windows, especially in Emacs.(there are a lot of key bindings.)

To find what program intercept the hotkeys, you can using following approach:

### 1,Open Spy++(spy++ comes with visual studio) 

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201101/201101101706225345.png) 

click log icon as above picture.

### 2,Message options window will pop up after you click log icon. 

select [All Windows in System] in multiple choose box. as following: 

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201101/201101101706247306.png) 

### 3,Click Messages tab in Message Options, and mark up the keybord&hotkey boxes. 

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201101/201101101706278404.png)

### 4,After you select, press OK button. You will see message window. 
![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201101/201101101706285797.png)

The windows message be displayed in above window as you press keyboard. Now we inspect  the first record(hotkey) and find out which program intercept this hotkey.

### 5, As you see, I marked the “Window Handle” in red rectangle which is 0003004C. Now, click Find Window icon on Spy++ toolbar. 

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201101/201101101706293157.png) 

A pop up window as following, you put 0003004c after label of Handle, and press OK. 

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201101/201101101706304171.png) 

### 6, Oh, at this point you know who is troublemaker. 

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201101/201101101706313025.png)

You can also press Synchronize button to track the process in Spy++.
