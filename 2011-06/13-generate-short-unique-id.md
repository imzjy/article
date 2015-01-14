How to generate the short unique id using C#
=========

It’s very common to create unique id in our application, like as order identifier,user identifier.etc. There are also many ways to generate the unique id in C#. The simplest approach is generating GUID by GUID struct built in .net framework. like as:

`string id = Guid.NewGuid().ToString().ToLower()`

But, the length of id that created by this approach is 36 digits. It’s long, we want to make short version of unique id instead of long version of unique id.

It’s hard to create global unique id less than 36 digits. In reality, we also do not need the global unique id. sometimes, unique in machine level just enough for us.There is a easy way to generate unique id that do not global unique and with a slight performance overhead.

This approach utilize DateTime.Ticks property to generating unique id.The Ticks property for DateTime represents how number of 100-nanosecond intervals that have elapsed since 12:00:00 midnight, January 1, 0001. The step of generating unique id are:

1. hold on 1 minisecond for unique.
1. get how 100-nanoseconds have elapsed since specific time point.
1. convert the value of time ticks from decimal to alphabet.
 
Here is source code of [unique id generator](http://code.google.com/p/code-gallery/source/browse/trunk/dotnet/common-lib/common-lib/IdGenerator.cs).

```csharp
public class IdGenerator
{
    private static object instance = new object();
 
    public static string NewId()
    {
        lock (instance)
        {
            Thread.Sleep(1);
            long ticks = DateTime.Now.Ticks;
            return ConvertToBase(ticks, 36);
        }
    }
 
    private static String ConvertToBase(long num, int nbase)
    {
        String chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
 
        // check if we can convert to another base
        if (nbase < 2 || nbase > chars.Length)
            return "";
 
        long r;
        String newNumber = "";
 
        // in r we have the offset of the char that was converted to the new base
        while (num >= nbase)
        {
            r = num % nbase;
            newNumber = chars[(int)r] + newNumber;
            num = num / nbase;
        }
        // the last number to convert
        newNumber = chars[(int)num] + newNumber;
 
        return newNumber.ToLower();
    }
}
```
