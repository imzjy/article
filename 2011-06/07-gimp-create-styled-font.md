GIMP 创建不同风格文字
========

### 1，GIMP文字操作

#### 1.1 怎么样在GIMP中添加文字？

File->New新创建一个画布，然后点击工具箱中的“A”样式的工具(或菜单Tools->Text)。

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106071353085667.png)

在画布中需要添加文字的地方点击，此时会出现一个GIMP Text Editor对话框，在些写入你想添加的文字，我这里写入“GIMP 文字”。

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/20110607135309585.png)

此时，在工具箱的下方，你可以更改文字的字体，大小，颜色等属性，如图：

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106071353091664.png)

#### 1.2 怎么样修改已经添加的文字？

在你添加字体时，会自动添加一个字体的图层(Layer)，你可以右击这个图层然后选择Text Tool来修改文字。

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106071353096092.png)


### 2，使用GIMP创建发光文字

#### 2.1 按上面所教方法，创建“GIMP 文字”，并将字体的颜色设置为红色。

之后将文字作为选区，即在文字图层上右击Text to Selection.

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106071353105469.png)

#### 2.2 将选区扩大3px。

点击Select->Grow，之后在Grow Selection中设置为3px。

#### 2.3 复制这个图层，并将填充为黄色(光线的颜色)。

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106071353108501.png)

#### 2.4 在选区上使用高斯模糊

在`GIMP文字#1`这个图层上点击一下，选中这个图层，然后Select->None。然后对图层使用高斯模糊Filters->Blur->Gaussian Blur，

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106071353109896.png)

将模糊值设置为10px将模糊值设置为，

#### 2.5 将`GIMP文字#1`复制一份，再次使用高斯模糊

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106071353114814.png)

#### 2.6 复制[GIMP文字]图层，并使用高斯模糊

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106071353125238.png)

#### 2.7 调整图层顺序

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106071353124682.png)

#### 2.8 新建一个黑色图层，并放图层最下方

为了让发光效果更加明显，我们换个黑色的底色。最终效果

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106071353137680.png)


### 3，创建五彩斑斓的文字

#### 3.1 在新画布上添加文字，文字内容为[GIMP文字]

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106071353141726.png)

#### 3.2 创建文字选区

使用2.1所教的方法创建文字选区


#### 3.3 使用Blend Tool工具创建渐变色

在工具箱点击渐变填充工具(Tools->Paint Tools->Blend)

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106071353143088.png)

#### 3.4 选择填充的Gradient

在填充工具下方的属性Gradient中选择一个多色相的填充色，比如Full saturation spec

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106071353146120.png)

#### 3.5 填充文字选区

按住Ctrl键(Ctrl键可以保证一条水平线)，在文字选区上从左至右填充。

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106071353149151.png)

填充完成后如下：

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106071353145007.png)

#### 3.6 创建一个黑色图层来衬托一下

最终效果如下：

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106071353146087.png)
