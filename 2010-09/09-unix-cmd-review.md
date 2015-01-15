Unix Command Review
=====

### Important UNIX conventions

#### 1, Command Format

> Commands must be typed all on one line, with spaces between the command, options, and arguments.

#### 2,Naming Files

> Filenames consist of alphanumeric characters, underscores, dashes, and periods.  DO NOT use spaces or other punctuation in filenames!

#### 3,Case Sensitivity

> Commands and filenames in UNIX are case sensitive!!

#### 4,Filename Completiom

> After typeing a unique prefix of a filename, pressing the Tab key will cause the Unix shell to complete the filename.

#### 5,Command Editing

> The up arrow key will retrieve a previous command. This command may be edited using the left/right arrow keys and backspace.

#### 6,^C (control-C)

> In UNIX, this terminates a currently running process when typed in the window the process is running in.

#### 7,^Z (control-Z)

> In UNIX, this sends a process to run in the background. The process will still exist; you just won't see it. Type "fg" to bring it back so that you can exit properly. Don't exit Unix with processes running in the background.

### Working with Directories

#### 0,Directory Notes

In UNIX pathnames, slashes (/) separate the directory and filenames 
e.g. /home/mcb/myfile.txt  [ here home and mcb are directories and myfile.txt is a file ]. The current directory is referred to as . (‘dot’) and the parent directory is referred to as .. (‘dot dot’). The home directory is called ~ (‘tilde’).

#### 1,Display present working directory

`pwd`   echo present working directory on screen

#### 2,Change directory

```text
cd dirname     Change current working directory to specific directory.
cd or cd ~    Go to your home directory, i.e. the directory you start in when you login.
cd ..   Go to the parent of the directory you are in now [ move up by 1 directory ]
```

#### 3,Create/Delete directory

```text
mkdir dirname     Creates a directory called dirname in the current directory
rmdir dirname     Delete (remove) empty directory
rm –r dirname     Delete directory and the content inside it(files,subdirectoris)
```

#### 4,Lists directory contents

```text
ls dirname       lists contents within specific directory
ls –l            shows a "long", detailed listing
ls –a            lists all of contents ,including hide directoris,files(starting with “.”)
```

### Working with Files

#### 1,Display file content

```text
cat filename        display entire file
cat –vet            display file including Non-printing characters such as tab,carriage return,linefeed.It’s useful when a file move from windows to unix.
cat filename | less   display and navigate file content
```

#### 2,Rename/Move files

```text
mv file1 file2     rename file1 to file2
mv file dir        move the file to the specific directory
```

#### 3,Copy a file

```text
cp f1 f2     makes a copy of f1,named f2
cp f1 dir    copy f1 to a specific directory
```

#### 4,Delete a file

```text
rm f1       delete a file permanently,Use this command carefully - there is no Undo!!
rm –i f1    ask your confirm before you delete a file. in practice, you can add alias from rm to rm –i in your .bashrc file
```

#### 5,Change file’s mode(who can operate on the file)

`chmod perm f1`  change mode of filename as specified by perm(issions). e.g. chmod  +x file makes file executable,chmod  g-r file removes group read permission on file

### Patterns and Counting

#### 1,Pattern

```text
grep pattern files      find the lines that meet the pattern
grep –r pattern  dir   find the lines recursively in a directory. e.g. grep –r fatal  /var/log
```

#### 2,Counting

```text
wc –l       count by line,usually get input from pipeline. e.g. cat f1 | wc -l
wc –w       count by word
wc –m       count by character
```

### Input/Output and Pipelines

#### 0,Input/output notes

> By default the output of a command goes to STDOUT (standard output or the monitor), and input of a command comes from STDIN (the keyboard).  Input and output can be redirected to/from files with the  < , > and  >> symbols

#### 1,Redirect

```text
cat f1 f2 > f3         concatenate files f1 and f2 and store the result in file f3. Warning: this overwrites file f3
cat f1 >> f2           concatenate file f1 and append to the contents of f2
sort < f1 > f1.sort    sort command reads from f1 and outputs to f1.sort
```

#### 2,Pipelines notes

> Multiple commands can be chained together in a pipeline with the | (‘pipe’) symbol.  When | is used between commands, the output of the first command is piped as input to the second command

#### 3,Pipelines

```text
grep “A” f1 | wc –l   find lines in f1 containing “A” and pipe them to wc  -l Note: this counts the number of lines containing “A” 
grep “>” f1 | wc –l   note that quoting “>” prevents it from acting as output redirection. 
cat f1|sort|head      send the contents of f1 to the sort command, then send the sorted lines to the head command to print the top 10.
```

### Finding help

```text
command –help    a short usage description
man command      manual for a command
```
