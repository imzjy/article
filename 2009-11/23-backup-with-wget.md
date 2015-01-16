Backup the blog through wget
==========

I need backup my blog that hosting on chinaunix. opening every page and saving as local file are boring, so I get the copy through Unix tools called wget.

For more information about wget, please click: [wget](http://en.wikipedia.org/wiki/Wget)。

First, export environment variable:

`export ftp_proxy=proxy_ip:proxy:port`

And then create the file containing downloading url line by line:

```text
http://blog.chinaunix.net/u/11680/article_0_1.html
http://blog.chinaunix.net/u/11680/article_0_2.html
http://blog.chinaunix.net/u/11680/article_0_3.html
http://blog.chinaunix.net/u/11680/article_0_4.html
```

Last, execute the command as:

`wget -m -c -k -L -p --proxy-user=username --proxy-passwd=password -i import_url.txt`
