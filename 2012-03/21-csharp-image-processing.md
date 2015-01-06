C#图片处理
=======

通常对一幅图片的处理包括：格式变换，缩放(Scale)，翻转(Rotate)，截取(Clip)，滤镜(Filter,如高斯模糊)等。

### 1,图片格式转换
.NET中的Image类是对图片对象的封装，我们可以通过操作Image类的实例来处理图片。通常我们有两种式可以得到Image实例：

```csharp
var imgPng = Image.FromFile(@"C:\temp\img\pp.png");
 
byte[] raw = ReadFromFileOrNetwork();
var imgBmp = Image.FromStream(new MemoryStream(raw));
``` 

#### 1.1判断图片格式

```csharp
var imgJpg = Image.FromFile(@"C:\temp\img\jj.jpg");
if (imgJpg.RawFormat.Equals(ImageFormat.Jpeg))
{
    MessageBox.Show("Jpeg");
}
```

注意这里使用`ImageFormat.Equals`方法，而不能使用`==`，如果非要使用等号，可以：

```csharp
if (imgPng.RawFormat.Guid == ImageFormat.Png.Guid)
{
    MessageBox.Show("Png");
}
```

#### 1.2,图片格式转换

```csharp
imgPng.Save(@"c:\temp\img\newBmp.bmp", ImageFormat.Jpeg);
```

### 2,图片的缩放(Scale)

图片的放大，缩小，拉伸可以通过Image实例的·GetThumbnailImage·来实现

```csharp
//缩小
var newPng = imgPng.GetThumbnailImage(imgPng.Width / 2, imgPng.Height / 2, () => { return false; }, IntPtr.Zero);
newPng.Save(@"c:\temp\img\newPng.png");
//放大
var newJpg = newPng.GetThumbnailImage(imgPng.Width * 2, imgPng.Height * 2, () => { return false; }, IntPtr.Zero);
newJpg.Save(@"c:\temp\img\newJpg.jpg", ImageFormat.Jpeg);
//拉伸(Stretch)
var newGif = newPng.GetThumbnailImage(imgPng.Width * 2, imgPng.Height  /2, () => { return false; }, IntPtr.Zero);
newGif.Save(@"c:\temp\img\newGif.gif", ImageFormat.Gif);
```

### 3,图片的翻转(Rotate)

图片的翻转通过Image.RotateFlip方法来实现

```csharp
//翻转
imgPng.RotateFlip(RotateFlipType.Rotate180FlipX);
imgPng.Save(@"c:\temp\img\newPng.png");
```

可以通过`RotateFlipType`调整翻转的角度

### 4,图片的截取(Clip)

有时我们只想要图片的一部分，比如左边100个像素，而不是整个图片。我们可以通过两种方式来实现。

#### 4.1，拷贝原图片的部分像素

```csharp
Rectangle rect = new Rectangle(0, 0, imgPng.Width / 2, imgPng.Height);
Bitmap clipPng = new Bitmap(imgPng).Clone(rect, imgPng.PixelFormat);
clipPng.Save(@"c:\temp\img\clipPng.png");
```

#### 4.2，画出部分图片

```csharp
Rectangle rect = new Rectangle(0, 0, imgPng.Width / 3, imgPng.Height);  //target size
Bitmap canvas = new Bitmap(rect.Width,rect.Height);                     //create canvas(width&heigh same as target)
 
using (Graphics g = Graphics.FromImage(canvas))
{
    g.DrawImageUnscaledAndClipped(imgPng, rect);
}
canvas.Save(@"c:\temp\img\canvas.png");
```

### 5,滤镜(Filter)

通常我们对图片使用滤镜，就是对图片的像素点进行矩阵变换(Matrix)。我们先从单个像素点的处理开始：

#### 5.1，颜色反转(Color Invert)

Color Invert是指对位图的每个像素取其反色，Jpg和Bmp格式的颜色是以RGB(Red Green Blue)来表示的，也就是每个像素点由RGB三种颜色来组成。Png由于可以设置为透明，所以加了一个Alpha通道，也就是说Png是用RGBA来表示的。

有一点需要注意的是，我们使用Image来获取的颜色表示并不是RGB而是BGR，准确地说这是GD+在底层返回的就不是RGB，而是BGR这点需要特别注意。对于Png文件我们还可以通过Alpha通道来设置图片的透明度。

```csharp
/* Usage:
    InvertColor(@"C:\temp\img\colorInvert.png", @"C:\temp\img\colorInvert-1.png");
*/
private static void InvertColor(string srcFileName,string destFileName)
{
    var bitPic = new Bitmap(srcFileName);
    if (!(bitPic.RawFormat.Equals(ImageFormat.Bmp) || 
        bitPic.RawFormat.Equals(ImageFormat.Jpeg) || 
        bitPic.RawFormat.Equals(ImageFormat.Png)))
    {
        MessageBox.Show("Unsuported format,only support for bmp,jpg or png");
        return;
    }
 
 
    Rectangle rect = new Rectangle(0, 0, bitPic.Width, bitPic.Height);
    var bmpData = bitPic.LockBits(rect, ImageLockMode.ReadWrite, bitPic.PixelFormat); // GDI+ still lies to us - the return format is BGR, NOT RGB. 
 
    IntPtr ptr = bmpData.Scan0;
    // Declare an array to hold the bytes of the bitmap.
    int totalPixels = Math.Abs(bmpData.Stride) * bitPic.Height; //Stride tells us how wide a single line is,width*heith come up with total pixel
    byte[] rgbValues = new byte[totalPixels];
 
    // Copy the RGB values into the array.
    Marshal.Copy(ptr, rgbValues, 0, totalPixels); //RGB=>rgbValus
 
    if (bitPic.RawFormat.Equals(ImageFormat.Bmp) || bitPic.RawFormat.Equals(ImageFormat.Jpeg))
    {
        int b = 0, g = 1, r = 2;  //BGR
        for (int i = 0; i < totalPixels; i += 3)
        {
            rgbValues[r + i] = (byte)(255 - rgbValues[r + i]);
            rgbValues[g + i] = (byte)(255 - rgbValues[g + i]);
            rgbValues[b + i] = (byte)(255 - rgbValues[b + i]);
        }
    }
    else if (bitPic.RawFormat.Equals(ImageFormat.Png))
    {
        int b = 0, g = 1, r = 2, a = 3;  //BGRA
        for (int i = 0; i < totalPixels; i += 4)
        {
            rgbValues[r + i] = (byte)(255 - rgbValues[r + i]);
            rgbValues[g + i] = (byte)(255 - rgbValues[g + i]);
            rgbValues[b + i] = (byte)(255 - rgbValues[b + i]);
            rgbValues[a + i] = 255;  //NOTE:you can set (255*threshold) for transparency.
        }
    }
 
    Marshal.Copy(rgbValues, 0, ptr, totalPixels);
    bitPic.UnlockBits(bmpData);
 
    bitPic.Save(destFileName);
}
```

对于GIF，由于他并不是按RGB的颜色来编码，而是用另一种256色的颜色编码，我稍后再研究:)

#### 5.2，灰度图(Grayscale)

Grayscale就是将每像素点的RGB值作平均，即第个像素的RGB分量值都是一样的。这样做的目的就因为等值的RGB(R=G=B)就是从黑到白的颜色区间，我们可以通过GIMP看下：

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201203/201203221349088128.png)

当每个像素点的组成RGB相等时，该点必定是灰色调的。

我们的代码也有调整，这次使用`Bitmap.GetPixel来`得到图片的RGB值，这样就不需要对图片的格式进行特别处理了。不过还是不可以处理Gif等使用Indexed Color的图片。

```csharp
private void Grayscale(string srcFileName, string destFileName)
{
    var bitPic = new Bitmap(srcFileName);
    if (!(bitPic.RawFormat.Equals(ImageFormat.Bmp) ||
        bitPic.RawFormat.Equals(ImageFormat.Jpeg) ||
        bitPic.RawFormat.Equals(ImageFormat.Png)))
    {
        MessageBox.Show("Unsuported format,only support for bmp,jpg or png");
        return;
    }
 
    int rgb;
    Color c;
    for (int y = 0; y < bitPic.Height; y++)
    {
        for (int x = 0; x < bitPic.Width; x++)
        {
            c = bitPic.GetPixel(x, y);
            rgb = (int)((c.R + c.G + c.B) / 3);  //We can adjust this calc as needed, such as Max(r,g,b),Min(r,g,b),(.299*r +.587*g.+ .114*b)
            bitPic.SetPixel(x, y, Color.FromArgb(rgb, rgb, rgb));
        }
    }
 
    bitPic.Save(destFileName);
}
```

#### 5.3，明亮度(Brightness)

计算机中颜色(Color)是用RGB来表示的，但我们人眼对色彩的认识的模式是HSV(纯度Hue,饱和度Saturation,亮度Value或Luminance)。我们可以使得RGB的每个分量的值增大来让图片变亮，也可以使每个分量变小来让图片变暗。而HSV模式的明暗设置就更简单了，只需改V分量值即可以改变图片的明暗。关于RGB到HSL/HSV的转换算法可以看Wikipedia。有一点需要注意的就是.net中Color类的GetHue,GetSaturation,GetBrightness获取的是HSL值而不是HSV值。

##### 通过RGB来改变明暗度

```csharp
private void Brightness(string srcFileName, string destFileName, float grain)
{
    var bitPic = new Bitmap(srcFileName);
    if (!(bitPic.RawFormat.Equals(ImageFormat.Bmp) ||
        bitPic.RawFormat.Equals(ImageFormat.Jpeg) ||
        bitPic.RawFormat.Equals(ImageFormat.Png)))
    {
        MessageBox.Show("Unsuported format,only support for bmp,jpg or png");
        return;
    }
 
 
    Color c;
    Func<int, int> notOver255 = (x) => { return x > 255 ? 255 : x; };
    for (int y = 0; y < bitPic.Height; y++)
    {
        for (int x = 0; x < bitPic.Width; x++)
        {
            c = bitPic.GetPixel(x, y);
            Color brightColor = Color.FromArgb(
                notOver255((int)(c.R * grain)), 
                notOver255((int)(c.G * grain)), 
                notOver255((int)(c.B * grain)));
            bitPic.SetPixel(x, y, brightColor);
        }
    }
 
 
 
    bitPic.Save(destFileName);
}
```csharp

##### 通过HSV中V分量来改变图片明暗度

稍后研究，还有个问题就是改变图片的明暗度后，Png和Jpg图片的大小产生了变化，换个说法就是RGB分量值会影响Png和Jpg压缩。


-----
Reference:

1,http://www.codeproject.com/Articles/1989/Image-Processing-for-Dummies-with-C-and-GDI-Part-1

2,http://en.wikipedia.org/wiki/HSL_and_HSV

3,http://stackoverflow.com/questions/359612/how-to-change-rgb-color-to-hsv

4,http://www.cnblogs.com/sndnnlfhvk/archive/2012/02/27/2370643.html
