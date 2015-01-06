C#画图
====

在.NET下面画图需要用到System.Drawing命名空间，这个命名空间基本上是对GDI+(Graphic Devices Inteface plus)的封装。我们来看看怎么使用.NET画图。

### 1，先创建一个画布(Graphics)

GDI+是对显示器/打印机的图形输出设备的包装，通过GDI+我可以使用抽象语言输出图形，而不考虑硬件的驱动等细节。要画图先要有画布（其实是个输出设备），在.NET中我们用Graphics来表示这个画布。MSDN对Graphics类的解释是：Encapsulates a GDI+ drawing surface.

我们一般有两种方法创建画布(Graphics):

#### 1.1,使用Graphics的静态方法，从Image，窗口来创建Graphics。

```csharp
//create graphics over window
var frmGraphics = new frmGraphics();
Graphics g = Graphics.FromHwnd(frmGraphics.Handle);
 
//create graphics over image
var img = Image.FromFile(@"C:\Users\a.png");
Graphics g2 = Graphics.FromImage(img);
```

#### 1.2,使用.NET控件的CreateGraphics方法

```csharp
Graphics g = pictureBox1.CreateGraphics();
```

### 2，画出图形

我们可以用两种方式表示一个图形，用笔(Pen)勾画出形状。我们还可以用刷子(Brush)填充出这个形状，由些绘画API有分为两类，一类是勾画，这类API特点是都以Draw开头：

```csharp
g.DrawArc(redPen, rect, 125, 40);                 //弧
g.DrawBezier(redPen, p1, p2, p3, p5);             //Bezier曲线
g.DrawClosedCurve(redPen, points);                //闭合曲线
g.DrawCurve(redPen, points);                      //曲线
g.DrawEllipse(redPen, rect);                      //椭圆，当长宽比为1:1时即为圆
g.DrawLine(redPen, p1, p4);                       //线段
g.DrawLines(redPen, points);                      //点连成的线段
g.DrawPath(redPen, new GraphicsPath());           //由直线和曲线连成的路径
g.DrawPie(redPen, rect, 90, 45);                  //饼状图
g.DrawPolygon(redPen, points);                    //多边形
g.DrawRectangle(redPen, rect);                    //方形
g.DrawString("Cicle", new Font("Arial", 15), brush, p4);
```

填充的API都是以Fill开头，基本用法跟上面类似，唯中的区别就是以Brush来代替Pen

```csharp
g.FillClosedCurve(brush, points);
g.FillEllipse(brush, rect);
g.FillRegion(brush, new Region(rect));
g.FillPie(brush, rect, 90, 100);
```

### 3，处理图像

Graphics有两类方法用来处理图像：

```csharp
g.DrawIcon(icon, rect);
g.DrawImage(image, p1);
g.DrawImageUnscaledAndClipped(image, p2);
DrawIcon, DrawImage将图标或图像显示在输出设备(Graphics)上。
```
 
### 4，截屏

Graphics类还提供了一个截图的方法CopyFromScreen，我们可以利用这个方法来截取屏幕：

```csharp
g.CopyFromScreen(new Point(0, 0), new Point(100, 100), sz);
```

### 5，其它

#### 5.1，抗锯齿

```csharp
g.SmoothingMode = SmoothingMode.AntiAlias;
```

#### 5.2,画布的大小

```csharp
g.VisibleClipBounds.Width;
g.VisibleClipBounds.Height;
```

#### 5.3，画布的变换(Transform)

```csharp
var img = Image.FromFile(@"C:\Users\message.png");
g.RotateTransform(45);
g.ScaleTransform(0.5F, 0.5F);
g.DrawImage(img, p1);
```
