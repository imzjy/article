Run exe in background on .NET platform
===========

前两天写了个[Bash脚本](http://www.cnblogs.com/Jerry-Chou/archive/2010/12/14/1905415.html)，用来将Flv格式转换为Avi格式。可是，并不是每个人的电脑上都有Linux/Unix环境，在将这些小工具拿给别的使用的时候，我还要提供一个Windows可以执行的工具。本来我是想将Bash转换为Windows批处理的，弄了一会也没有搞好，后来想了一下，干脆写个Console Application去后台调用ffmpeg工具来执行转换工作。

工具写好了，当我调用ffmpeg.exe这个小工具的时候，老是出现一个cmd窗口，非常不美观。后来网上找了一下，将执行ffmpeg的窗口隐藏起来，这个效果好多了。最近狂迷Command-Line和一些开源简洁的小工具，用这个方法，我就可以在我的应用程序中利用一些简洁实用的小工具了 :)

```csharp
using System;
using System.Diagnostics;
using System.IO;
using System.Threading;
 
namespace convert_flv_2_avi
{
    class Program
    {
        static void Main(string[] args)
        {
            CheckFfmpegToolExist(Ffmpeg);
            MakeDestinationFolderExist(AviFolder);
 
            Console.WriteLine("Starting convert, please ensure flv files placed in folder of flv-folder\n");
            ConvertFlv2Avi(FlvFolder);
 
            Console.WriteLine("\nCompleted,Press any key to exit.");
            Console.ReadKey();
        }
 
        private static void ConvertFlv2Avi(string flvFolder)
        {
            string[] flvFiles = Directory.GetFiles(flvFolder);
            foreach (string flv in flvFiles)
            {
                Console.WriteLine("Converting file of {0}", flv);
                RunFfmpeg(flv,
                    string.Format("{0}.avi", flv.Substring(0, flv.Length - 4)));
            }
        }
 
        private static void MakeDestinationFolderExist(string aviFolder)
        {
            if (!Directory.Exists(aviFolder))
            {
                Directory.CreateDirectory(aviFolder);
            }
        }
 
        private static void CheckFfmpegToolExist(string Ffmpeg)
        {
            if (!File.Exists(Ffmpeg))
            {
                Console.WriteLine("Can not find {0}", Ffmpeg);
                Console.ReadKey();
                Environment.Exit(1);
            }
        }
 
        static void RunFfmpeg(string flvFile, string aviFile)
        {
 
            Process ffmpeg = new Process();
            ffmpeg.StartInfo.FileName = Ffmpeg;
            ffmpeg.StartInfo.Arguments = 
                string.Format(@"-i {0} -r 25 -b 750k -y {1}", flvFile, aviFile.Replace(FlvFolder, AviFolder));
            ffmpeg.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;  //Run ffmpeg.exe in background
            try
            {
                ffmpeg.Start();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
 
        }
 
 
        private const string Ffmpeg = @"ffmpeg\ffmpeg.exe";
        private const string FlvFolder = @"flv-folder";
        private const string AviFolder = @"out-avi-folder";
    }
}
```
