部署HTTPS
=========

因为要用到HTTPS，为了测试我在自己的站点上部署了[HTTPS](https://www.imzjy.com)，对于部署来说还是比较简单的，网上也有大把教程可以参考，但是这些教程大多只给出了命令并没有解释命令和原理，我开一篇Blog来介绍下命令和部署HTTPS流程和原理。

### 1, 网站管理员怎么部署HTTPS

在介绍细节之前先介绍一下大致流程:

1. 生成RSA密钥
2. 使用RSA密钥生成CSR(Certificate Sign Request)
3. 将CSR发给CA(Certificate Authority)
4. CA会发给你4张Certificate
5. 将CA给你的证书合并成一张证书
6. 使用RSA密钥和合并后的证书部署Web Server

接下来，我们看看每一步我具体要做什么，怎么做，为什么这么做。

#### 1.1, 生成RSA密钥

HTTPS是基于PKI(Publick Key Infrastructure)，是使用非对称的加密来防止防止篡改和抵赖，在使用HTTPS之前我们需要生成自己的密钥，这个密钥用来加密和身份识别。我们可以使用[openssl](https://www.openssl.org/)工具来生成RSA密钥：

```shell
$openssl genrsa -out imzjy.key 2048 
```

生成2048为的密钥，这里说得密钥其实是私钥，有一点需要注意所有的私钥都是包含公钥的，你可以从私钥中导出公钥--如果你需要的话，[参考](http://stackoverflow.com/questions/5244129/use-rsa-private-key-to-generate-public-key)。我们这这里不需要公钥，所以我们不关心这部分。

生成的私钥内容形式如下：

```text
-----BEGIN RSA PRIVATE KEY-----
KaTPkW8avFQKx4gtWGNJvxsq+gArY7zDtglkcb1NnR0pb5ZFkr5SuLZvCU2sX+YQ
Ey8qOrgsCoz9x4fym/gU2H4cPpibGjxDjRRWiytMxXDC5w+ni3MzBcMtOCtiPLEJ
--省略了一些--
MIIEogIBAAKCAQEAxKSYkUAqwzpLvgAzvPjyvp1MFGWk/8EnWkWc60QCs7IzqhEF
-----END RSA PRIVATE KEY-----
```

