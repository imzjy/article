自动化构建--使用Ant
==============

Ant是基于Java的自动化构建工具，它依赖于JDK，所以在使用Ant前先要安装JDK，并将JAVA_HOME和PATH环境变量指向JDK，比如在Windows下，环境变量看起来是这个样子的：

```text
JAVA_HOME = C:\Program Files\Java\jdk1.6.0_31
PTAH = %JAVA_HOME%\bin;
```

Ant在使用和概念上很像GNU make，不过是用XML来标记的make，除此之外Ant容许我们用Java来写扩展，这样就可以完成一些比较复杂的构建，甚至是部署的工作了。

### 1，一些概念

类似于make默认在当前目录下寻找Makefile来构建项目一样，Ant会在当前目录下寻找build.xml来构建项目。典型的build.xml看起来是这样样子的：

```xml
<project name="DemoProject" default="dev">
    <!-- build directory -->
    <property name="build.dir" value="./build" />
 
    <!-- default target, it depends the target of clean & makeDirs -->
    <target name="dev" depends="clean, makeDirs">
        <echo message="build folder has been created!" />
    </target>
 
    <!-- target: clean -->
    <target name="clean">
        <delete dir="${build.dir}" />
    </target>
 
    <!-- target: makeDirs -->
    <target name="makeDirs">
        <mkdir dir="${build.dir}" />
    </target>
</project>
```

build.xml构建文件有一个构建项目组成，每个构建项目根据需要可以有若干个Target，每个Target有若干个task组成。类似于这样的结构：

> Project => Target(s) => Task(s)

另外ant也支持属性的，属性类似于make中的变量，上例中我们定义的build.dir这个属性，然后在多处引用。

对于一个构建项目来说必须有一个project来表明当前的构建项目，这个project一般有两个常用的属性，一个是项目的名称：DemoProject，另一个是默认的target，默认的target是指，你若直接在目录下使用ant命令而不加任何参数时，ant会执行的target。类似于make中的第一个target的作用。

Target一般也有两个常用的属性，一个是name用来标明当前target，你可以这样在命令行上指定target name，以此来调用该target，比如我们想调用clean这个target

`$ant clean`

Target另一个重要属性就是depends，Ant通过depends属性来实现依赖管理。比如对于dev这个target来说，他依赖于clean和makeDirs这两个target，在dev这个target被执行之前，Ant会按照depends属性指定的顺序执行相应的target，示例中先执行clean，然后才是makeDirs，最后是dev本身。

Ant中真正做工作是这些task，Ant中配置的繁杂部分也就是各种各样的task，参见[Task Overview](http://ant.apache.org/manual/tasksoverview.html)。

### 2，常用的Task

```text
copy     用来拷贝文件及目录
mkdir    用来创建目录
delete   用来删除文件及文件夹
move     移动文件及目录，文件及目录重命名
replace  变量替换，比如 <replace file="main.js" token="@REVISION@" value="${revision}" /> 这个task会将main.js中的@REVSION@标记替换为${ revision }变量的值
```
 
### 3，扩展Task

如果你觉得Ant自带的task不够用，你可以写Java的jar来扩展task的功能。具体请参考：[Write Your Own Task](http://ant.apache.org/manual/develop.html#writingowntask)。
