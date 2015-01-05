用Git应付一些临时工作
======

### 1，Intruduction

我们有时候会接到一些临时的工作，这些工作时常在计划之外，比如现在一个Bug来了，你需要及时修复。但你从上次发布以后又改了许多，并且有的改动已经stage，有的已经commit，有的已经push，这怎么办呢？

为了澄清我们的讨论，我们先看一张图

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201207/201207061103379949.png)

那么就有四种情况要处理：

1. Working Directory changed, but not staged
2. Staged but not commit
3. Commit but not push to remote
4. Your remote repo changed but not send pull request

### 2，Working Directory Changed和Staged but not commit

对于未提交到本地库的代码，我们可以使用git stash命令，将Working Directory和Index(Stage)的改动暂存起来。

```shell
git stash list   #列出所有stash
git stash        #将当前的Work Directory和Index的改动暂存起来
git stash apply stash@{0}    #将0号stash的状态返回
git stash drop stash@{0}     #将0号stash删除
git statsh clear             #删除所有stash
```

### 3，Committed but not push to remote

这种情况下最好新创建一个branch来修改Bug。这个branch就是基于上次的Release。

```shell
git branch –v         #显示当前的branch
git log –10 –oneline  #显示log
git branch release   <commit-sha1>   #基于sha1的commit新建一个branch
git checkout release      #切换到release这个branch
git branch –d release     #删除一个branch
git merge master release  #release的改到merge到master
```

### 4，Your remote repo changed but not send pull request

这种情况，你还是新建一个branch去修改bug，改动后上传到Your remote，然后在pull request的时候选择哪个修改bug的branch。

### 5，Others

有时候我想临时忽略一个文件，不要让他被track，比如我的在本地访问Amazon S3比较慢，我想给我的Python代码加一个临时Cache，我不想提交(追踪这个文件的改动)这个文件。

我们可以：

```bash
git update-index --assume-unchanged <file>        #临时ingore一个文件的改动
git update-index --no-assume-unchanged <file>     #继续track这个文件
```
