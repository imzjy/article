写一个lstree
======

### 1，缘起

有的我们拿到一个文件，通常是我们不太清楚的文件，比如你拿到了一个朋友传给你的源代码，如果你可以一眼看出这个源代码的目录结构那该有多好啊。

我以前的做法是：

> `$ls –R`

但是这样看不出目录结构的层级，我们是否可以自己写一个类似pstree的工具来完成这个任务？

当然可以，比如我们想看GNU coreutils源代码目录结构：

```text
~/repo/coreutils$ lstree  | grep '/$'
m4/
gl/
    m4/
    lib/
    modules/
    tests/
po/
doc/
man/
lib/
src/
old/
    textutils/
    sh-utils/
    fileutils/
gnulib/
tests/
    mv/
    rm/
    chown/
    dd/
    split/
    id/
    tail-2/
    pr/
    chmod/
    df/
    ln/
    readlink/
    rmdir/
    cp/
    ls/
    misc/
    fmt/
    chgrp/
    mkdir/
    install/
    du/
    touch/
build-aux/
scripts/
    git-hooks/
gnulib-tests/
```

这样就可以清楚地知道GNU coreutils是怎么组织目录的。

# 2，源代码

[jatsz/coreutils-ex](https://github.com/jatsz/coreutils-ex)

`git clone git://github.com/jatsz/coreutils-ex.git`

Have fun!
