'InitializeCulture' is not a member of 'XXXX'解决方法--ASP.NET
===============

今天在部署ASP.NET网页时出现一个奇怪的问题。在开发，调试时访问网页一切正常。但一部署到IIS中时就会出现以下的错误信息：

`'InitializeCulture' is not a member of 'XXXX'. `

**解决方法**：

1. 在publish时，将第一个选项Allows this precompiled site to be updated选项unchecked。
2. 出现该问题的真正原因是两个aspx页面共享了一个源代码文件，找出共享的源代码文件。将其重命名。

例如：

```text
A.aspx
   <%@ Page Language="vb" AutoEventWireup="false" Inherits="SPC.Main" CodeFile="SPC_Main.aspx.vb" %>
B.aspx
   <%@ Page Language="vb" AutoEventWireup="false" Inherits="SPC.Main" CodeFile="SPC_Main.aspx.vb" %>
将B.aspx更新为：
   <%@ Page Language="vb" AutoEventWireup="false" Inherits="SPC.B" CodeFile="SPC_B.aspx.vb" %>
```
即可。
