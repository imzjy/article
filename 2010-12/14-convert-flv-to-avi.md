Convert video format from flv to avi
==============

最近由于需要将一些视频由flv格式转化为avi格式，为了自动化转换，我写了如下脚本：

```shell
#!/bin/bash
 
FFCMD='/cygdrive/c/work-dir/ffmpeg/ffmpeg.exe'  # path to ffmpe tools
 
#check output directory exist
if ! test -d $2;
then
  mkdir $2
fi
 
#convert flv to avi
for f in $(ls $1/*.flv);
do
  if test -f $f
  then
    echo -e "\nConverting $f"
    FILENAME=$(basename $f | cut -d '.' -f 1)
    #echo $FILENAME
    $FFCMD -i $f -r 25 -b 750k -y $FILENAME.avi 2>> log.txt
    mv -f $FILENAME.avi $2
  else
      echo -e "\nSkipping $f - not a regular file";
  fi
done 
 
#Usage#
#You can convert the all of flv files in flv-folder/ to avi file located in out-avi-folder/ by following command
#$./convert-flv-2-avi.sh flv-folder/  out-avi-folder/
```

对于视频/音频的转换，一般都会用到ffmpeg这个工具，详情可以参考：http://www.ffmpeg.org/
