diff和patch

diff是基于行的比较。diff的输出有两种，一种给人看的，另一种给patch命令看的。

### 1，给人看的diff输出

#### 1.1，-y, output in two column

```txt
jerry@JerryOnVbox:~/workspace$ diff -y a.txt b.txt
if a = b:                           if a = b:
  output = a.toString()                       output = a.toString()
                                  >    save(a)
else                                else
  output = "no record found"                      |   output = "no record founds"
                                  >
                                  >  self.write(output)
 
def foo():                          def foo():
  print "hello"                           |     print("hi")
                                  >
                                  >  def doo():
                                  >      print("hello")
                                  >
                                  >  foo();
 
foo()                                 <
```

左边源文件a.txt，右边是b.txt。

```text
> 表示这一行是添加的(append)
|  表示这一行是改变(change)
```

### 1.2，-u output NUM (default 3) lines of unified context

方便查看文件间的不同：

```text
jerry@JerryOnVbox:~/workspace$ diff -u a.txt b.txt
--- a.txt   2012-05-24 13:23:18.115751347 +0800
+++ b.txt   2012-05-24 13:24:12.980307391 +0800
@@ -1,9 +1,16 @@
 if a = b:
   output = a.toString()
+  save(a)
 else
-  output = "no record found"
+  output = "no record founds"
+
+self.write(output)
  
 def foo():
-  print "hello"
+   print("hi")
+
+def doo():
+   print("hello")
+
+foo();
  
-foo()
```

第1行是源文件a.txt的时间戳，第2行是b.txt的时间戳

第3行前半部分-1,4是可以这样理解-表示源文件，1,4指从第一行到第四行。+(目的文件)1,7行。

#### 1.3，-c  output NUM (default 3) lines of copied context.

如果你想看完整的两个文件，你可以

```text
jerry@JerryOnVbox:~/workspace$ diff -c  a.txt b.txt 
*** a.txt   2012-05-24 13:23:18.115751347 +0800
--- b.txt   2012-05-24 13:24:12.980307391 +0800
***************
*** 1,9 ****
  if a = b:
    output = a.toString()
  else
!   output = "no record found"
   
  def foo():
!   print "hello"
   
- foo()
--- 1,16 ----
  if a = b:
    output = a.toString()
+   save(a)
  else
!   output = "no record founds"
! 
! self.write(output)
   
  def foo():
!   print("hi")
! 
! def doo():
!   print("hello")
! 
! foo();
```

### 2，给机器看的diff输出

为了让diff的结果，也就是patch尽可能的小些利于在网络上传递，你可以直接diff a.txt b.txt

```text
jerry@JerryOnVbox:~/workspace$ diff a.txt b.txt 
2a3
>   save(a)
4c5,7
<   output = "no record found"
---
>   output = "no record founds"
> 
> self.write(output)
7c10,15
<   print "hello"
---
>    print("hi")
> 
> def doo():
>    print("hello")
> 
> foo();
9d16
< foo()
```

输出主要有三部分组成：

11. 变动类型，范围：比如这里的2a3，4c5,7。其中的字母的意义为：`a(add),c(change),d(delete)`。字母前面的数字表示源文件a.txt变动范围，字母后面的表示文件b.txt对应的变动范围。
2. 源文件变动内容(即---上方的内容，内容前面的">"表示添加，而"<"表示删除)
3. 最新文件b.txt对应的变动内容(---下方的内容）

我们这样理解这段输出：

```text
2a3：      源文件(a.txt)第2行后面加上(a)目的文件(b.txt)的第3行内容。即 >>save(a)
4c5,7：    源文件的第4行，变为(c)，目的文件的5~7行。
7c10,15：  源文件的第7行，变为(c)，目的文件的10~15行。
9d16：     源文件的第9行，删除(d)，成为目的文件的第16行。也就是说目的文件的16行是个空行。
```

### 3，使用patch

经过diff命令，我们一般有三个文件，old文件，new文件，和changes.patch文件。这三个文件只要有其中的两个我们就能得到第三个。

我们重命名一下，将a.txt改为old.txt，将b.txt改为new.txt。我们先产生changes.patch文件。

```text
$ diff old.txt new.txt > changes.patch
```

#### 3.1，我们有old.txt和changes.patch，如何得到new.txt

```text
$ patch old.txt < changes.patch 
$ cat old.txt    #you will find the contect of old.txt identify with new.txt
```

#### 3.2，我们有new.txt和changes.patch，如何得到old.txt

```text
$ patch -R new.txt < changes.patch 
$ cat new.txt   #notice that the content of  new.txt became to original old.txt
```

### 4，有用的diff选项

#### 4.1，忽略一些你不关系的内容

- -i  忽略大小写 
- -b 忽略两个字母间的空白 
- -B 忽略空白行 

#### 4.2，递归比较目录

`$diff –r path/to/trunk  path/to/branches/v1.4`  #当前的版本和v.14相比做了哪些更改
 
----
Reference：

http://en.wikipedia.org/wiki/Diff
