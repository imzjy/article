Git常用命令
=======

因为项目中用到了Git(GitHub)，而Git的命令，概念也比较多，我这里记录一下。

### 1，概念

Git是分布式版本控制系统，在本身Git的设计中没有所谓的中央库。当然在实际开发中我们一般会设定一个中央库以方便管理，比如GitHub上的库作为中央库。但是这不是Git强制的，是Best Practice，是我们为了方便管理在概念上设置的。这个中央库约定俗成叫做：origin。

Git中只有本地库和远端库(remote repository)。Git一般是三级级提交：

1. 我们先提交到暂存区(stage)，通git add  .|filename

2. 再提交到本地库(这也是Git比SVN好的地方，适合频繁提交)，通过git commit –m “you comments here”

3. 最后当我们觉得需要将这些代码分享的时候我们在提交到远端库(remote)，通过git remote add  [remote name]  git://github.com/octocat/Spoon-Knife.git 添加远端库，通过git push [remotename]  master将本地库的更新推送到远端库。

Git的metadata比较集中，在库所在的目录有一个.git目录，所有的metadata都在这个目录下。

### 2，Git的配置

git有三个配置文件，分别是repo/.git/config，$HOME/.gitconfig，/etc/gitconfig。

- repo/.git/config 库级别的配置文件，只对当前库有效，优先级最高(git config –local)
- $HOME/.gitconfig 用户级别的配置文件，对当前用户有效，优先级次之(git config –global)
- /etc/gitconfig 系统全局配置文件，对整个系统有效，优先级最低(git config –system)

```text
git config --list    #查看当前有效配置
git config --global color.ui true   #设置color.ui为true
```text

git支持自动完成，也就是说你输入`git conf`然后按`tab`键，系统会自动扩展为`git config`。对于选项这依然有效，比如`git config –global –color.[tab]`你会看到许多可选项。

### 3，查看命令

#### 3.1，查看Git当前库的状态

```text
git status [-s]    # -s是简短的输出，左列是暂存区的状态，右边是工作区的状态
```

#### 3.2，显示当前连接的remote repo

```text
git remote -v
```

#### 3.3，显示branch，在Git中branch就是一个working context(工作上下文)，你可以很随意的新建一个branch来创建一个工作上下文。

```text
git branch  [-v]
```

#### 3.4，显示文件的每一行都是谁最后修改的

```text
git blame a-file.c
```

#### 3.5，以简洁的方式显示branch的graph

```text
git log --graph --pretty=oneline  [-5]   # -5显示最近5笔log。
```

#### 3.6，显示最近两次commit的详细信息，包括文件改动

```text
git log –p –2          #-p会打印出改动的diff结果
git show <commit-id>   #想看特定的commit
```

### 4，本地库的操作

#### 4.1,创建版本库

```text
git init  reponame  #创建本地库
git clone git@github.com:jatsz/snippets.git    #以远程clone的方式创建版本库
```

#### 4.2，添加文件到暂存库(stage)

```text
git add file   #将file加到版本库中，其实是stage中。
git add –u     #将所有tracked files的更新添加到stage
git add .      #注意这个点号，这是将所有改动添加到stage
```

#### 4.3，将暂存库提交(commit)到本地库

```text
git commit –m “you comments”   #将stage中的改动提交到本地库
```

### 5，远程库操作

#### 5.1，添加一个远程库

```text
git remote add upstream git://github.com/octocat/Spoon-Knife.git   #新建一个远程库，并命名为upstream
```

#### 5.2，从远程库获取代码

```text
git fetch upstream          #获取
git merge upstream/master    #合并到当前开发分支，这步如果不做你看不到文件的更新，git status显示“Your branch is behind 'origin/master' by 1 commit, and can be fast-forwarded.”
```

#### 5.3，将本地更新Push到远程库

```text
git push upstream master   #将本地master上传到upstream
```

#### 5.4，删除远程库

```text
git remote rm upstream   #删除名为upstream的远程库
```

### 6，查看文件修改(diff)

通常，我们的每个文件有4份影像：本地工作区，暂存区(stage)，本地版本库 (local repo)，远程版本库(remote repo)。所以我们通过不同的diff选项来比较不同位置的文件影像。

#### 6.1，工作区与暂存区的比较

```text
git diff  [file-name]
```

#### 6.2，暂存区与本地库的比较

```text
git diff –cached [file-name]
```

#### 6.3，工作区与本地库的比较

```text
git diff HEAD [file-name] 或 git diff master  [file-name]     #HEAD通常是master的别名
```

#### 6.4，本地库与远程库的比较

这个比较麻烦些，我们先要获取远程源代码

```text
git fetch upstream    #这里upstream是远程代码库
git diff master   upstream/master
```

### 7，撤销(reset)与反悔(revert)

Git的撤销是指你叫工作区的修改加到暂存区的，你现在想把它撤回——不改变文件。反悔是指，你想用暂存区的影像(staged snapshot)覆盖工作区的文件。

Git中的撤销和反悔也要考虑到：工作区，暂存区，本地库。

#### 7.1a，从暂存区撤销(Unstage)

```text
git reset – readme.txt #将readme.txt unstage，如果想unstage所有的文件直接 git reset
```

#### 7.1b，从暂存区反悔，用暂存区文件覆盖工作区文件

```text
git checkout –  readme.txt    #你将丢失所有unstaged的修改
```

#### 7.1c，从本地库反悔，用本地库的snapshot来覆盖工作区的文件

```text
git checkout HEAD – readme.txt  #丢失所有staged和unstaged的修改
```

#### 7.2a，从本地库撤销到暂存区(Undo commit)

```text
git reset –soft HEAD^     #HEAD是指当前版本，HEAD^表示当前提交的上次提交，
```

#### 7.2b，从本地库直接撤销到工作区(undo commit => undo stage)

```text
git reset –mixed HEAD^
```

### 8，创建里程碑(tag)

#### 8.1，为最新的release创建一个里程碑

```text
git tag rev-1.1 –m “create tag for release v 1.1”
```

#### 9，杂项

#### 9.1，忽略一些文件：添加.gitignore文件

`.gitignore`文件的作用范围是当前文件夹和所有子文件夹。可以使用通配符。实例：

```text
.DS_Store 
*.pyc 
*.avi 
*.mp4 
*.wmv
```text

#### 9.2，不要轻易用git reset –hard

如果你想要恢复前面的版本，你可以先用`git checkout HEAD^^ [—cached] – README` 找出最近的更改，然后在`git commit –m "delete added line to readme file"`。

这样的好处是这个历史记录都保存的比较完整，log history的graph也比较好看懂。而你`用git reset –hard HEAD^^`会彻底丢失历史。如果你真这样做了只有这样找回历史记录了的：

```text
git reflog  -10
git resest –hard HEAD@{2}
```
 
-----
Reference:

http://kb.cnblogs.com/page/132209/

http://book.douban.com/subject/6526452/       --《Git权威指南》 蒋鑫

http://marklodato.github.com/visual-git-guide/index-en.html  -- A Visual Git Reference
