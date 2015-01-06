.net快速写个录像程序
=========

基本在Windows下的录像程序在底层都是使用了Microsoft的[DirectShow](http://msdn.microsoft.com/en-us/library/windows/desktop/dd375454(v=vs.85).aspx)接口，对于DirectShow有一个.net的wrapper，称作[DirectShowLib](http://directshownet.sourceforge.net/)。但是封装地并不充分，换个角度说你还是需要知道DirectShow的API然后才能编写摄像头程序，有没有封装地更好地呢，当然有的:).我们可以使用[AForge](http://www.aforgenet.com/)的封装在30分钟左右写出一个摄像程序。

下面是关键代码：

```csharp
VideoFileWriter writer = new VideoFileWriter();
VideoCaptureDevice videoSource = null;
System.Diagnostics.Stopwatch timer = null;
 
private void video_NewFrame(object sender,NewFrameEventArgs eventArgs)
{
    // get new frame
    Bitmap bitmap = eventArgs.Frame;
    //image.SetPixel(i % width, i % height, Color.Red);
    writer.WriteVideoFrame(bitmap, timer.Elapsed);
 
}
 
private void btnStart_Click(object sender, EventArgs e)
{
    VideoCaptureDeviceForm videoSettings = new VideoCaptureDeviceForm();
    var result =  videoSettings.ShowDialog(this);
    if (result == System.Windows.Forms.DialogResult.Cancel)
    {
        return;
    }
 
    // create video source
    videoSource = videoSettings.VideoDevice;
    // set NewFrame event handler
    videoSource.NewFrame += new NewFrameEventHandler(video_NewFrame);
    // start the video source
    videoSource.Start();
 
 
    var fileName = string.Format(@"C:\temp\capv\{0}.flv", Guid.NewGuid().ToString());
    FileInfo fInfo = new FileInfo(fileName);
    if (!Directory.Exists(fInfo.DirectoryName))
    {
        Directory.CreateDirectory(fInfo.DirectoryName);
    }
 
    // create new video file
    writer.Open(fileName, 640, 480, 30, VideoCodec.FLV1);
 
    //start a timer to sync the video timeline
    timer = System.Diagnostics.Stopwatch.StartNew();
 
    ShowCurrentStatus("running");
}
 
private void btnStop_Click(object sender, EventArgs e)
{
    videoSource.SignalToStop();
    videoSource.WaitForStop();
    writer.Close();
    ShowCurrentStatus("stop");
}
```

AForge不仅对DirectShow进行了封装，还提供了图片处理的函数，可以用来处理图片，比如一些滤镜。其[介绍在这里](http://www.aforgenet.com/framework/features/)，[文档在这里](http://www.aforgenet.com/framework/documentation.html)。

[源码下载](http://files.cnblogs.com/Jerry-Chou/DirectShowDemo.7z)

NOTE:需要注意的是源码中我使用了`AForge.Video.FFMPEG`的命名空间，用来保存视频编码，其在底层用了ffmpeg的类库，所以运行程序时需要`avcodec-53.dll`等类库在场。你可以从[AForge的类库包](http://www.aforgenet.com/framework/downloads.html)的`Externals\ffmpeg\bin`中找到这些文件。
