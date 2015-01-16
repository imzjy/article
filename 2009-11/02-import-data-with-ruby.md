员工信息导入[Daily works with Ruby]
=========

上周接到一个小的Case，将一些盘点的员工资料导入至数据库。我打开邮件中的Excel，原始资料格式如下：

```text
ID FirstName LastName
123 Jerry Chou
```

我需要做的是将该资料导入数据库。 数据库中的表格列为：

```text
ID Name
```

我的任务也很简单：

1. 将Excel导出成CSV(Comma Separated Value) 。
1. 将 123,Jerry,Chou 的第二个逗号去掉，形成这样的格式： 123,JerryChou。
1. 将 123,JerryChou 导入至数据库。 


任务1很简单，会用Exel都可以做到。

任务2，我写了一个Ruby小脚本,如下：

```ruby
in_file = File.new('pi_user_import.csv')
out_file=File.new("formatted_user.csv","w") 

in_file.each_line do |line|
    v1,v2,v3 = line.split(',')
    puts "#{v1.strip},#{v2.strip}#{v3.strip}\n"
    puts out_file.write("#{v1.strip},#{v2.strip}#{v3.strip}\n")
end
```


任务3，仍然是一个小脚本。

```ruby
require 'OCI8'

conn = OCI8.new('DBUser','UserPass','TNSName')
cursor = conn.parse("INSERT INTO CPI_USER(ID,UNAME) VALUES (:1,:2)")

in_file = File.new('formatted_user.csv')
row_num  = 0
in_file.each_line do |line|
    v1,v2 = line.split(',')
    puts "#{v1},#{v2}"
    
    cursor.bind_param(1, v1.strip)
    cursor.bind_param(2, v2.strip)
    cursor.exec()
    row_num = row_num+1
end
puts row_num.to_s + ' rows were processed.'

cursor.close()
conn.commit
conn.logoff

###############Imported Checking#####################
#num_rows = conn.exec('select * from pi_user') do |r|
#    puts r.join(',')
#end
#puts num_rows.to_s + ' rows were processed.'
###############End Checking##########################
```

注：你可以从：http://rubyforge.org/projects/ruby-oci8/ 获取Ruby-OCI8.

**个人体会**：

- 我很久没有写Ruby的玩具代码了，但遇到具体任务，用Ruby写个小脚本来完成任务还是很简单的。
- Ruby脚本对Oracle的支持也还不错。
- 记得听说过类似“不行就迭代”的话，但不记得是谁说的了。对于一些日常琐事来说确实如此。提醒自己写项目代码时可不能这样想。

