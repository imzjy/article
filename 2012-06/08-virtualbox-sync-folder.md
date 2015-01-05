Synchronize the folders between Windows and Ubuntu in VirtualBox
======

### 1, Why do this

Recently, I keep working in my guest operating system which is Ubuntu 12.4 LTS. I got some project documents from my co-workers. It’s better to read the documents from Ubuntu directly, instead of switch between guest operating system(Ubuntu) and host operating system(Windows 7).

A simple idea came out: I want a way to sync a folder between Ubuntu and Windows. rsync maybe a handy tools intended for sync files and folder across different machines.

### 2, Preparations

#### 2.1, Install the rsync

I am cygwin fan, there is package built with the cygwin, we just use it. We can get and install the package by cygwin’s setup.exe.

#### 2.2, Install the ssh daemon in Ubuntu(guest operating system)

```shell
$sudo apt-get install ssh
$ss –l  #check ssh daemon is running
```

#### 2.3, Enable the VirtualBox port forwarding

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201206/201206081439042698.png)

Adding the port forwarding for ssh, as such:

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201206/201206081439043079.png)

#### 2.4,Create the sync folder

We also need create the sync folder both in Windows 7 and Ubunt, in which our file keep sync.

```shell
$mkdir –p /cygdrive/c/VirtualBox/Rsync/data/   #cyginw on Windows 7
$mkdir –p /home/jerry/Rsync/data/              #Ubuntu
```

### 3, Well done

It’s time to show off. I put some files in the folder of `/cygdrive/c/VirtualBox/Rsync/data/`.  I want the guest operating system, Ubuntu, can also sync all of this file. Just type:

`$rsync.exe -avzP  --rsh='ssh -p 2222' /cygdrive/c/VirtualBox/Rsync/data/ jerry@localhost:/home/jerry/Rsync/data/`

When system prompt you typing the jerry’s password, just type it and enter.

All things done! Now you can view/edit the file in Ubuntu. Wow? You edited file and you want to sync this to Windows? No problem. Open the cygwin on Windows, type:

`$rsync.exe -avzP  --rsh='ssh -p 2222' jerry@localhost:/home/jerry/Rsync/data/ /cygdrive/c/VirtualBox/Rsync/data/`

Even more, You may want a small shell scripting to make it automatically. Like this:

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201206/201206081439059732.png)

Have fun!
