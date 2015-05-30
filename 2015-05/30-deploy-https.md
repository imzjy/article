部署HTTPS
=========

因为要用到HTTPS，为了测试我在自己的站点上部署了[HTTPS](https://www.imzjy.com)，对于部署来说还是比较简单的，网上也有大把教程可以参考，但是这些教程大多只给出了命令并没有解释命令和原理，我开一篇Blog来介绍下命令和部署HTTPS流程和原理。

### 网站管理员怎么部署HTTPS

大致流程是这样的:

1. 生成RSA密钥
2. 使用RSA密钥生成CSR(Certificate Sign Request)
3. 将CSR发给CA(Certificate Authority)
4. CA会发给你4张Ce
