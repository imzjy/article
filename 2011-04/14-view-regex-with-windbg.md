View Regex pattern string using windbg
============

```text
0:004> !threads 
********************************************************************* 
* Symbols can not be loaded because symbol path is not initialized. * 
*                                                                   * 
* The Symbol Path can be set by:                                    * 
*   using the _NT_SYMBOL_PATH environment variable.                 * 
*   using the -y <symbol_path> argument when starting the debugger. * 
*   using .sympath and .sympath+                                    * 
********************************************************************* 
PDB symbol for clr.dll not loaded 
ThreadCount:      2 
UnstartedThread:  0 
BackgroundThread: 1 
PendingThread:    0 
DeadThread:       0 
Hosted Runtime:   no 
                                   PreEmptive   GC Alloc                Lock 
       ID  OSID ThreadOBJ    State GC           Context       Domain   Count APT Exception 
   0    1  1774 0066c328      a020 Enabled  021e5614:021e5fe8 00665b58     0 MTA 
   2    2  17bc 00678150      b220 Enabled  00000000:00000000 00665b58     0 MTA (Finalizer) 
0:004> ~0s 
*** WARNING: Unable to verify checksum for C:\Windows\assembly\NativeImages_v4.0.30319_32\mscorlib\b79870f56fb884856832833fe760f671\mscorlib.ni.dll 
*** ERROR: Module load completed but symbols could not be loaded for C:\Windows\assembly\NativeImages_v4.0.30319_32\mscorlib\b79870f56fb884856832833fe760f671\mscorlib.ni.dll 
eax=00000001 ebx=00000000 ecx=00000000 edx=00000000 esi=0015ec0c edi=0015eb88 
eip=75947468 esp=0015eafc ebp=0015eb1c iopl=0         nv up ei pl nz na po nc 
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00000202 
KERNEL32!VDMConsoleOperation+0x246: 
75947468 83c404          add     esp,4 
0:000> !DumpHeap -type Regex 
….

Statistics: 
      MT    Count    TotalSize Class Name 
62b361b4        3           36 System.Text.RegularExpressions.RegexCharClass+SingleRangeComparer 
62b36188        3           36 System.Text.RegularExpressions.RegexCharClass+SingleRange 
62b362f8        3           48 System.Text.RegularExpressions.RegexFC 
62b3611c        3           72 System.Collections.Generic.List`1[[System.Text.RegularExpressions.RegexCharClass+SingleRange, System]] 
62b35e4c        3           72 System.Collections.Generic.List`1[[System.Text.RegularExpressions.RegexOptions, System]] 
62b35cf8        3           72 System.Text.RegularExpressions.RegexCharClass 
62b362bc        3           84 System.Text.RegularExpressions.RegexFCD 
62b364fc        6           96 System.Text.RegularExpressions.RegexPrefix 
62b35ff4        4           96 System.Text.RegularExpressions.RegexOptions[] 
62b36210        3          108 System.Text.RegularExpressions.RegexTree 
62b35a0c        3          120 System.Text.RegularExpressions.RegexBoyerMoore 
62b36284        3          132 System.Text.RegularExpressions.RegexCode 
62b36248        3          144 System.Text.RegularExpressions.RegexWriter 
62b1e5b4        3          156 System.Text.RegularExpressions.Regex 
62b35e10        3          252 System.Text.RegularExpressions.RegexParser 
62b36540        3          312 System.Text.RegularExpressions.RegexInterpreter 
62b360a4       18          432 System.Collections.Generic.List`1[[System.Text.RegularExpressions.RegexNode, System]] 
62b35d30        1         1140 System.Text.RegularExpressions.RegexCharClass+LowerCaseMapping[] 
62b36040       29         1160 System.Text.RegularExpressions.RegexNode 
Total 100 objects 
0:000> !DumpHeap -mt 62b1e5b4 
Address       MT     Size 
021db2fc 62b1e5b4       52     
021e1390 62b1e5b4       52     
021e2248 62b1e5b4       52     
total 0 objects 
Statistics: 
      MT    Count    TotalSize Class Name 
62b1e5b4        3          156 System.Text.RegularExpressions.Regex 
Total 3 objects 
0:000> !DumpObj 021db2fc 
Name:        System.Text.RegularExpressions.Regex 
MethodTable: 62b1e5b4 
EEClass:     6295bb8c 
Size:        52(0x34) bytes 
File:        C:\Windows\Microsoft.Net\assembly\GAC_MSIL\System\v4.0_4.0.0.0__b77a5c561934e089\System.dll 
Fields: 
      MT    Field   Offset                 Type VT     Attr    Value Name 
6356f9ac  4000001        4        System.String  0 instance 021db210 pattern 
62b3489c  4000002        8 ...egexRunnerFactory  0 instance 00000000 factory 
62b2dd68  4000003       24         System.Int32  1 instance        0 roptions 
6357537c  4000004        c ...ections.Hashtable  0 instance 00000000 caps 
6357537c  4000005       10 ...ections.Hashtable  0 instance 021e0344 capnames 
63526c28  4000006       14      System.Object[]  0 instance 021e0b70 capslist 
63572978  4000007       28         System.Int32  1 instance        2 capsize 
62b35c0c  4000008       18 ...xclusiveReference  0 instance 021e135c runnerref 
62b35c48  4000009       1c ...s.SharedReference  0 instance 021e1370 replref 
62b36284  400000a       20 ...essions.RegexCode  0 instance 021e131c code 
6357662c  400000b       2c       System.Boolean  1 instance        1 refsInitialized 
62b35da8  400000c        4 ...deEntry, System]]  0   static 021db8a0 livecode 
63572978  400000d      864         System.Int32  1   static       15 cacheSize 
0:000> !DumpObj 021db210 
Name:        System.String 
MethodTable: 6356f9ac 
EEClass:     632a8bb0 
Size:        50(0x32) bytes 
File:        C:\Windows\Microsoft.Net\assembly\GAC_32\mscorlib\v4.0_4.0.0.0__b77a5c561934e089\mscorlib.dll 
String:      (?<url>href=".+?") 
Fields: 
      MT    Field   Offset                 Type VT     Attr    Value Name 
63572978  40000ed        4         System.Int32  1 instance       18 m_stringLength 
63571dc8  40000ee        8          System.Char  1 instance       28 m_firstChar 
6356f9ac  40000ef        8        System.String  0   shared   static Empty 
    >> Domain:Value  00665b58:021d1228 << 
```text

命令的备注：

```text
0:004> !threads               #列出所有托管的线程
0:004> ~0s                    #转到0号托管进程(~0s)，其中0:004中的4表示当前线程ID为4
0:000> !DumpHeap -type Regex  #使用!DumpHeap –type 查看Regex的Method Table。
!DumpHeap -mt 62b1e5b4        #查看Method Table所关联的Object
!DumpObj 021db2fc             #查看Regex对象的内容
!DumpObj 021db210             #由于String是引用类型，Value显示的是其引用值，再次查看该引用对象(String)的内容
```
