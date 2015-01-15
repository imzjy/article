Why Object doesn't support this property or method in Javascript?
===========

Recently, I developed the web camera application using Flex 3.

But, a bug from IE browser’s cache wasted me about 4 hours.the short description of bug are:

`Object doesn't support this property or method`

I have developed the swf application embeded in my page of SamplePage.aspx.  then I updated swf file in the web server directory.

When those job done, I reopen SamplePage.aspx and access swf property using Javascript code.there is exception popup `Object doesn't support this property or method`.

To fixed the problem, I make correct, recompile, check syntax both in ActionScript and Javascript,bla…bla…bla…..the exception still exist.

What’s happened ?

An idea be came up with after I had went home, it may be caused by browser’s cache.

Yes, I deleted the browser’s cache, then all thing go right.

In the case, I sumarize the following check list.

1. Check spelling.
2. Clean the browser’s cache before you testing a page.
2. Relax yourself when you have no idea on a bug.
