Go项目源代码组织
================

### 引言

我们在管理项目源代码结构的时候，最终总是要落实到具体文件和文件夹，还有文件和文件夹得之间关系的描述。比如我们传统的C项目，我们使用文件来存储源代码和头文件，用文件夹来存储不同的模块，最后用Makefile来描述这些文件和文件夹的关系。而我们在Visual Studio中新建项目的时候使用文件和文件夹来存储源代码，用`*.sln`项目文件来描述文件间的关系。Visual Studio正是使用了这个项目文件最终编译和链接。像这样的情况还有很多，比如Python中使用文件夹来描述包。

总结起来，我们通常都是使用文件来存储源代码，使用文件夹来作为模块的划分，最终使用描述文件来描述文件和文件夹的关系。

Go语言比较强调工程性，所以Go使用了`约定`的方式来组织文件和文件夹，这样可以省去了Makefile。只要你符合Go项目的约定放置源代码文件和文件夹，Go自动去约定的目录寻找和编译代码。

要编译连接一个Go的项目说，你至少需要按Go得约定设定：

- Go语言工作空间(`GOPATH`)
- 项目源代码(`src/`目录)

### Go语言工作空间

Go使用它自己的工作空间来组织它所有的代码，即所有代码都必须放到某一个Go的工作空间(Workspace)中才能编译链接。这个工作空间使用环境变量`GOPATH`来指定，我们可以使用下面的命令来查看当前的设定。

```text
➜  src  go env
GOARCH="amd64"
GOBIN=""
GOCHAR="6"
GOEXE=""
GOHOSTARCH="amd64"
GOHOSTOS="darwin"
GOOS="darwin"
GOPATH=""
GORACE=""
GOROOT="/usr/local/Cellar/go/1.4.2/libexec"
GOTOOLDIR="/usr/local/Cellar/go/1.4.2/libexec/pkg/tool/darwin_amd64"
CC="clang"
GOGCCFLAGS="-fPIC -m64 -pthread -fno-caret-diagnostics -Qunused-arguments -fmessage-length=0 -fno-common"
CXX="clang++"
CGO_ENABLED="1"
```

上面病没有设置Go的工作空间，我们可以使用下面的命令来将当前目前设为Go的工作空间：

```text
➜  gowks  export GOPATH=`pwd`
➜  gowks  go env | grep GOPATH
GOPATH="/Users/zjy/work/gowks"
```

`GOPATH`相当于所有Go项目的根目录，我们再看一下具体的目录组成：

  ```text
  ➜  gowks  tree -L 3 .
.
├── bin
│   └── s3cl
├── pkg
│   └── darwin_amd64
│       └── github.com
└── src
    └── github.com
        ├── goamz
        ├── imzjy
        ├── jessevdk
        └── vaughan0
  ```

再Go工作空间主要有三个目录组成：

- `src/` 源代码目录
- `bin/` 编译链接后的可执行文件
- `pkg/` 编译后可以直接用来链接的库文件

### src/ 源代码目录

我们的项目源代码放在`src/`目录下，通过不同的目录来组织不同的项目。通过类似`github.com/imzjy/s3cl`这样的结构来定义项目。在项目定义完成后，我们便可以`import github.com/imzjy/s3cl`来引用这个项目导出的类型，方法等。

我们再来看看`src/github.com/imzjy/s3cl`目录下具体的源代码是怎么组织的：

```text
 gowks  tree src/github.com/imzjy/s3cl 
src/github.com/imzjy/s3cl
├── LICENSE
├── README.md
├── build.sh
├── config.go
└── main.go
```

这个目录是`s3cl`这个Go项目的源代码目录，你还可以在这个目录下创建新的目录来组织模块，但无论怎么样，只是针对于`s3cl`这个项目，如果你想写一个库，那么最好是新建一个目录类似`github.com/imzjy/apkg`来单独将库作为一个Go项目。

当我们设置好`GOPATH`后，我们可以从任意目录，加上项目路径(`github.com/imzjy/s3cl`)来编译项目或者针对项目执行相关命令：

```text
➜  work  go build github.com/imzjy/s3cl
➜  work  go fmt github.com/imzjy/s3cl
gowks/src/github.com/imzjy/s3cl/config.go
gowks/src/github.com/imzjy/s3cl/main.go
```

这样组织的Go项目，可以直接使用`go get`来直接下载编译，链接Go项目。比如这里的`s3cl`是Go得一个命令行工具，别人想使用这个工具的话只需要执行：

```text
➜  work  go get github.com/imzjy/s3cl
```

Go会自动下载s3cl源代码到`src/`目录下，并且会自动下载依赖，编译和链接。这样你`s3cl`这个可执行文件就放在`bin/`目录下。你可以直接使用这个可执行文件。

### 总结

你在GitHub上新建项目，这个项目只放项目相关的源代码。然后你再自己的电脑上设置好自己的Go工作空间，这样你就可以使用`go get`，在Go工作空间目录来统一管理所有的Go项目。对于实际的项目，这个Go Workspace可以单独新建一个项目，其中包含一些项目相关的脚本，文档等常用目录，放到GitHub上，需要加入到项目的人员直接先clone这个项目，跑个脚本设置`GOPATH`，这样所有设置都完成了。类似：

```text
$ git clone https://github.com/imzjy/gowks
$ cd gowks && ./source env.sh
$ go get github.com/imzjy/s3cl
```

`s3cl`已经下载编译好，可以直接使用或者修改调试了。
