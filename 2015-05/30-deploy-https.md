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
MIIEpQIBAAKCAQEA6gkOZps1FDvfA9L7C4axPj+CgFmAV70qprVievLizaZ5QbNT
78ehKgFwBAC48dsWuyC8tNEVghm5Xrs4TXwkOOX7Q3Rm39VsAj1WQSE2Y/Jrd+61
SgABhiKGxaLNPwbJYc1R5Hj1/qEz061xcXl0iGMRdFC8VvxKM3Tn9w5UZN3qSRF2
1emAsq9puLpyEQfskjalLJx2iZyR31q7P0V1e7htRWs4wjswqe4oUTyxcxMqv/w4
--省略了一些--
t0PP0u/G3/a6WyKdCYUZWXmYqdqbn9FEDl2/8qvSOH7V2DuVCrHL46Qlc1BG95a2
IrXo3+eADmH2XH00zvJHU8CjytD7IV2oOQECdO8BV64jfAObK0+W2/psTP7xwISP
1hy21+XL0f60r59/c5lbtBO1F7Iu8EBHWhPNbvOqW8GzkcI3g08FNzLw/D44d/s3
MddNRq+vXOg/VhalL+v5MpUSDTX2/n0KxWVTsgJU4gWZzCPT+MY9Vnl+Tj/f1ajq
-----END RSA PRIVATE KEY-----
```

有了私钥以后，我们就可以申请让CA给我们颁发证书，我们需要提供的就是CSR文件。

#### 1.2, 生成CSR文件

我们需要提供给CA的只有一个CSR的文件，我们可以通过刚才生成的私钥(private key)生成对应的CSR，这里的意思其实是说，我们现在有了私钥，我要CA给我颁发一个证书，证明这个私钥是授信的，CA不要知道我们的私钥，他只是证明我们的私钥是可信的。可以通过下面的命令来生成CSR即可：

```shell
$openssl req -new -key imzjy.key -out imzjy.csr
```

这里的命令是使用私钥生成CA需要的CSR。这其中我们需要填写我们的一些信息，[信息规范](https://www.sslshopper.com/what-is-a-csr-certificate-signing-request.html)中*最重要*的部分就是CN(common name)，也就是你网站的域名，通常分为两类：一种是类似于`*.imzjy.com`的泛域名，这种认证比较贵，好处是你可以让你的子域名`blog.imzjy.com`都可以使用HTTPS。另一种就是制定单个域名比如`www.imzjy.com`，所有这个域名下得内容都可以使用HTTPS。

生成的CSR文件格式如下：

```text
-----BEGIN CERTIFICATE REQUEST-----
5hATLyo6uCwKjP3Hh/Kb+BTYfhw+mJsaPEONFFaLK0zFcMLnD6eLczMFwy04K2I8
sQmm/feCTxykn/+FK0ZvM97Fpp4Pp3U5py+lXtsJrJ4XENbcKv8JEKftu3xWS7EV
joqm48oiB9iljiF/xwVoQT/MCaz2JhG0BeCJ7QsRQ774Mw1XxHhobRioIfUnCicb
--省略了一些内容--
DyKSssyHuRMkkdfJGUn003lvUynfHxkgM4PPtC/vAgMBAAGgADANBgkqhkiG9w0B
AQUFAAOCAQEAM7ZLo8LjABvYY/+YCGx0JYq9DSPK18Q8w4htVqNx97QvvDSs9N6X
-----END CERTIFICATE REQUEST-----
```

在提交CSR给我们的CA之前，我们可以确认一下我们提交的内容填写是否正确，使用下面的命令可以从CSR中显示我们刚才填写的内容。

```shell
$openssl req -in imzjy.csr -noout -text
```
至此我们的申请准备工作已经做完，接下来可以把CSR发给CA要求CA给我们颁发证书。


