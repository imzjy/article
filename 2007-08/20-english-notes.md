《Inside the C++ Object Model》E文整理之二
========

**41，if any  如果有的话(一般放在句尾)**

Exp：Use overloading new operator to allocate the memory of the array, if any.

M1：使用重载的operator new 去分配数组的内存(如果有的话)。

M2：如果有重载的operator new，则用它分配数组的内存。

**42，with that   接着就...   然后就…**

Exp：As before, the additional 1 byte for the empty instance of class X is removed and, with that, the additional 3 bytes of padding.

M：像上节说的那样，为空的类实例而附加的1 byte被移除，接着是那3个字节的扩展(被移除)。

**43，at times 有时**

Exp：This size may at times surprise you as being larger than necessary.

M：这个大小有时会让你吃惊，因为它大于其需要的(内存大小)。

J：有时候其值可能令你吃惊，因为它可能比你想象的还大。

**44，come about  发生**

Exp：The growth comes about in two ways.

M：扩展以两种方式出现。

**45，as a whole  作为一个整体，整体来看**

Exp：Alignment requirements on the data members and data structures as a whole.

M：data member和作为一个整体的data struct的对齐需要。

**46，take up  占用，花去**

Exp：The concrete1 class contains the two members? The val and bit1 that together take up 5 bytes.

M：类concrete包含两个成员？val和bit1共占用了5个字节。

**47，so far  到目前为止**

Exp：Nothing necessarily to complain about so far.

M：到目前为止还没有什么需要抱怨的。

**48, fit 适合,**

词组  [fit of]

Exp：It’s the layout of derived class that typically drives the unwary programmer into fits of either perplexity or angry indignation.

M：典型的，这个派生类的layout将驱使粗心的程序员要么困惑，要么生气。

**49，pack into  塞进，挤进**

Exp：Our unwary programmer expects it to be packed into the base concrete1 representation.

M：我们那些粗心的程序员希望它(新增的bit2)被塞进基类concrete1中来表示。
