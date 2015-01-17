Functional Programming 的思考
====

最近Functional Programing似乎很热，7月份的《程序员杂志》也两天篇文章是专门讲述FP的。 

Funtional Programming(函式程编)是一种写传统的Imperative(命令式编程）有着不一样的思考方式。通过对FP的学习可以更好是从[怎么样解决问题这个角度]去分析问题。就我最近的了解，可以给FP打下以下几个tag： 

1. FP的特征，以及功能是体现是通过High-Order Function以及Lazy evaluation来实现的。通过FP可以更好的抽象算法——程序的目标。我们写的很多程序其实都是要实现一些算法。将一些输入，经过处理后，变为输出。 
2. 以数据为中心，在OO中我们常会讲到数据常用来保持对象的状态(data used for holding state）。面象对象的主要功能还是将算法与数据进行封装。而FP(函式编程)中的一等公民(first -class)解决的就是算法的问题。将算法拆为无状态，可复用的单元——即是函式(函数)。 
3. 编程思想的变化，由于我们长时间生活在Imperative式的编程环境中，可能对FP并不觉得友好，但FP所强调的模块化(Modularizatioin)，将状态与算法的分离，构建简洁，可复用的算法，等一些思想还是不谋而合的。其中C++对这方面的研究很近几年一直不断，对，我说的是C++中的Generic Programming，以及一些优秀的泛型库。泛型(Generizing）在一定程序上就是将算法写数据(状态,state)分离开，并重用其算法部分。 

OO进行了这么多年，但结构化编程依然存在，还活的很好，说明了OO也不是万能的。同样，如今FP双来了，但OO肯定会存在并发展而且会活的更好。我一直是喜欢看C++的代码，特别是写的好的C++的代码，可以结合多种编程模型，以最直接，简洁的方式完成任务。而关于这一些Bjarne多次提及。前几年C++有些朝向“奇技淫巧”上发展，结果让C++自己吃了苦头。 

FP给我们带来了新的思想，更高级的抽象方式，还不快些吸收！ 

----

Reference: 

http://www.md.chalmers.se/~rjmh/Papers/whyfp.html 

http://www.stanford.edu/class/cs242/readings/backus.pdf 
