Base64,DES,RSA,SHA1,MD5 笔记
======

### 1，Base64

场景：你想把一组二进制数据表示为一组可见字符，这样在某些场合更加利于传输，比如在邮件中传输。

算法：http://zh.wikipedia.org/wiki/Base64

### 2，DES和RSA

场景：你想对一组二进制数据进行加密。比如你想保护你的数据不被别人窃取，即使别人有你加密后的二进制数据，但如果没有密码，他仍旧不能解开。

算法：

DES：http://zh.wikipedia.org/wiki/DES 
RSA：http://zh.wikipedia.org/wiki/RSA%E5%8A%A0%E5%AF%86%E6%BC%94%E7%AE%97%E6%B3%95

区别：DES是对称的加密，也就是说加密和解密的用的是同一个密钥。RSA用的是非对称加密，加密用public key，解密用private key。

讨论：

DES现在可以被暴力破解，现在一般用AES来替代DES加密。

由于RSA是非对称加密，换个说法就是可以用私钥加密，用唯一对应的公钥解密。但这不是公钥加密(public cryptography)的工作方式。具体参见：

http://stackoverflow.com/questions/1181421/is-possible-to-encrypt-with-private-key-using-net-rsacryptoserviceprovider

所谓的用私钥加密的真正方式是数字签名。也就是你对一个二进制流用私钥进行签名。在接受端会用公钥来验证你的签名。从而可以知道来源的真实性和抗抵赖。具体的C#实例可以参考：https://gist.github.com/3991414

### 3，SHA1和MD5

场景：你有一组二进制数据，你为了保证这组二进制数据的完整性，你想为这组二进制数据生成唯一的数字签名。

算法：

- SHA1：http://zh.wikipedia.org/wiki/SHA1 
- MD5： http://zh.wikipedia.org/wiki/MD5
