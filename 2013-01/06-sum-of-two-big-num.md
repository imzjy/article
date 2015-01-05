求最大两数之和（SICP 习题1.3）
=======

《Structure and Interpreter of Computer Program》中第1章习题1.3说到：

> 练习1.3 请定义一个过程，它以三个数为参数，返回其中较大两个数之和。

其实这一段的中文版翻译错了，其实原版是说求最大两个数的平方和。但是意思是一样的。

为了这个简单的问题我也思考了挺长时间，就是得不到让我满意的解。三个数如何知道其中的两个较大的？其中的一个办法就是两两比较。但是这样做比较啰嗦，至少要比较三次。特别是用Scheme的写法。而且你最好还要定义变量，去保存中间判断结果。

洗碗时我想到一个解法：先求出最小的那个，然后用(x y z)之和去减去最小的那个值。

代码：

```lisp
(define (min x y)
   (if (< x y)
       x
       y))

(define (sum-of-large-two x y z)
             (- (+ x y z)
                (min (min x y) z)
             ))

;test
(sum-of-large-two 1 2 3)
(sum-of-large-two 3 1 2)
(sum-of-large-two 3 2 1)
```
