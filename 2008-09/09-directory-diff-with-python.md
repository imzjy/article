Python--文件比较脚本
===============

时常爱收集一些电子书,而且为了不让自己这些电子书丢失,我不仅在公司的电脑中有一份,家里的移动硬盘中也保留了一份.

但电子书通常都是慢慢收集来的,今天一书,明天一本.时间久了.公司电脑里的保存的电子书跟移动硬盘上的电子书不一致了,公司里的电子书在慢慢增长,而且分布在不同的目录之下,很难知道哪些是新增的,哪些是原来就有的.为了检查在两个目录中,有哪些文件是不一致的,我写了该脚本.

```python
#Platform: WinXp + Python2.5.2
#File compare
#Author Jerry Chou
#Date Aug-9-2008
#Revison: 0.1
"""
    This program compare the source directory file with the destination directory file
    and print the different file to screen.

    ----------------Module Variable Introduction-----------------
    [SrcDic], Source dicrectory, default is 'D:\Jeffrey\ebook'
    [DestDir], Destination directory, default is 'I:\ebook'
    [ExtList], which file extensions shoud be checked.
        default is ['.doc','.chm','.pdf','.zip','.7z']
    -------------------------------------------------------------
"""
import os

SrcDir = r'D:\Jeffrey\ebook'
DestDir = r'I:\ebook'
ExtList = ['.doc','.chm','.pdf','.zip','.7z']
_outlist=[]

def _getfilelist(dir):
    filelist = [os.path.join(dir,fname) for fname in os.listdir(dir)]
    basefilelist = [file for file in filelist if os.path.isfile(file) and str.lower(os.path.splitext(file)[1]) in ExtList]
    global _outlist
    _outlist = _outlist + basefilelist
    dirlist = [file for file in filelist if os.path.isdir(file)]
    for file_dir in dirlist:
        _getfilelist(file_dir)

def main():
    _getfilelist(SrcDir)
    global _outlist
    srclist = _outlist
    _outlist = []
    #
    _getfilelist(DestDir)
    #global _outlist
    destlist = _outlist
    _outlist = []
    #base file
    srcfilelist = [os.path.split(file)[1] for file in srclist]
    destfilelist = [os.path.split(file)[1] for file in destlist]
    #
    difflist = [file for file in srcfilelist if file not in destfilelist] + \
               [file for file in destfilelist if file not in srcfilelist]
    #query dict
    dictSrc = dict(zip(srcfilelist,srclist))
    dictDest = dict(zip(destfilelist,destlist))
    for item in difflist:
        if dictSrc.has_key(item):
            print r'[Source]' + dictSrc[item]
        elif dictDest.has_key(item):
            print r'[Destination]' + dictDest[item]
        else:
            print '-'*20 + 'Key Not Found' + '_'*20

if __name__ == '__main__':
    main()
```

用法示例:

```text
>>> import comparefile as cfile
>>> print cfile.__doc__
    This program compare the source directory file with the destination directory file
    and print the different file to screen.

    ----------------Module Variable Introduction-----------------
    [SrcDic], Source dicrectory, default is 'D:\Jeffrey\ebook'
    [DestDir], Destination directory, default is 'I:\ebook'
    [ExtList], which file extensions shoud be checked.
        default is ['.doc','.chm','.pdf','.zip','.7z']
    -------------------------------------------------------------

>>> cfile.SrcDir = r'D:\Backup\ELM\ELM_Project0219'
>>> cfile.DestDir =r'D:\Backup\ELM\ELM_Project'
>>> cfile.ExtList = ['.config','.cs','.vb']
>>> cfile.main()
[Source]D:\Backup\ELM\ELM_Project0219\ELM_Uploader\FrmUploader.Designer.vb
[Source]D:\Backup\ELM\ELM_Project0219\ELM_Uploader\FrmUploader.vb
[Destination]D:\Backup\ELM\ELM_Project\ELMS\ProjectInstaller.cs
[Destination]D:\Backup\ELM\ELM_Project\ELMS\ProjectInstaller.Designer.cs
[Destination]D:\Backup\ELM\ELM_Project\ELMSServer\Common.vb
[Destination]D:\Backup\ELM\ELM_Project\ELMSServer\Program.vb
[Destination]D:\Backup\ELM\ELM_Project\ELMSServer\bin\Debug\ELMSServer.exe.config
[Destination]D:\Backup\ELM\ELM_Project\ELMSServer\bin\Debug\ELMSServer.vshost.exe.config
[Destination]D:\Backup\ELM\ELM_Project\ELM_FERT\ELM_COMMON.vb
[Destination]D:\Backup\ELM\ELM_Project\ELM_FERT\ELM_FERT_1.vb
[Destination]D:\Backup\ELM\ELM_Project\ELM_FERT\ELM_ROH.vb
[Destination]D:\Backup\ELM\ELM_Project\ELM_FERT\bin\Debug\ELM.dll.config
```

调用`cfile.main()`给出了两个目录`D:\Backup\ELM\ELM_Project0219`和`D:\Backup\ELM\ELM_Project]`下面的vb及cs源文件有哪里异同.
