Windows下安装,设置PHP,Apache和MySQL
===============

最近在看PHP的书,为了感受一下PHP的Dirty and Quick,我想在Windows下安装Apache以及PHP和MySQL.从网上找了半天也配置不成功,主要是太分散了.不知道开源的世界因为易用性的缘故吓走了多少人.不过仔细想一下也不怪,在我配置好了之后再去看看网上的那些配置方法,好像都对,只是版本不同导致了很多不同的配置方式.现给出我的配置方法,希望不会很快就失效!

### Platform:

WinXp + php-5.2.5-Win32.zip + apache_2.2.8-win32-x86-openssl-0.9.8g.msi

### Installation:

1. unzip `php-5.2.5-Win32.zip`, and copy contents to `C:\PHP`;
1. install MySQL;
1. install Apache; In my computer, I prefer to `C:\Apache` as default installation directory

### Configuration:

**Appache**

1. open the folder of [conf] within apache install directory, then edit [httpd.conf] file within the folder of [conf].
	1. add the DSO support: `LoadModule php5_module "C:/PHP/php5apache2_2.dll"`
	2. b,add parsing support: `AddType application/x-httpd-php .php`
2. test the apache configuration;

**PHP and MySQL**

1. rename `php.ini-dist` to `php.ini` and copy it to the directory of `C:\Windows\`;
2. edit `php.ini` in directory of `C:\Windows`
	1. change `extension_dir='./'`  to `extension_dir='C:/PHP/ext'`;
	2. find section of `[Dynamic Extensions]`, uncomment the `extension=php_gd2.dll`,`extension=php_mbstring.dll`,`extension=php_mysql.dll`
3. copy `libmysql.dll` from `C:\PHP` to `C:\windows\system32`(PHP5 doesn't support MySQL by default,so must copy `libmysql.dll` by hand)
4. restart apache;
