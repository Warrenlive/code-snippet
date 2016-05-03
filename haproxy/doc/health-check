在haproxy中创建一个健康检查，至少需要在server配置行添加一个check关键字。下面来介绍常用的一些参数

	inter <time>：设置两个健康检查的间隔频率，如果没有设置，默认是2s
	rise <count>：连续检查成功的次数视为UP，默认2s
	fall <count>：连续检查失败的次数视为DOWN，默认3s

	timeout check <timeout>：让服务器接收检查的时间；如果inter和timeout check都设置了，小则优
![](http://www.haproxy.com/doc/aloha/8.0/_images/haproxy_checks_timeouts.png)


### TCP检查

1.默认检测端口使用server端口检查，也可以自定义。
2.option tcp-check：检查有效如果服务器回答了SYN / ACK包。

	backend abc
	 option tcp-check
	 server srv1 10.0.0.1:443 check port 80
	 
### SSL端口检查

1.option ssl-hello-chk：发送一个sslv3客户端的hello消息
2.每10s发送一次hello消息，两次无回复则认为失败

	backend abc
	 option ssl-hello-chk
	 option log-health-checks
	 default-server inter 10s fall 2
	 server srv1 10.0.0.1:443 check
	 
### http检查

1.使用一个简单的http检查

	backend abc
	 option httpchk
	 server srv1 10.0.0.1:80 check
 
 2.使用OPTIONS请求 / ，返回状态200-399正常

	backend abc
	 option httpchk OPTIONS / HTTP/1.0
	 http-check expect rstatus (2|3)[0-9][0-9]
	 server srv1 10.0.0.1:80 check
	 
3.使用GET请求 /check ，返回200正常

	backend abc
	 option httpchk get /check
	 http-check expect status 200
	 server srv1 10.0.0.1:80 check
	 
4.检查一个20k大小的返回值包含关键字OK则正常

	global
	 tune.chksize 32768

	backend abc
	 option httpchk get /check
	 http-check expect string OK
	 server srv1 10.0.0.1:80 check
	 
5.带主机名的检查

	backend abc
	 option httpchk get /check HTTP/1.0\r\nHost:\ www.xwarren.com
	 server srv1 10.0.0.1:80 check
	 
6.如果状态返回404则认为是维护模式，则快速关闭

	backend abc
	 option httpchk get /check HTTP/1.0\r\nHost:\ www.xwarren.com
	 http-check disable-on-404
	 server srv1 10.0.0.1:80 check
	 

### 检查MySQL服务

可选参数：

	user <username>：检查MySQL的用户名
	post-41：兼容MySQL 4.1和最新版本
	
准备工作：

	USE mysql;
	INSERT INTO user (Host,User) values ('<ip_of_haproxy>','<username>');
	FLUSH PRIVILEGES;

examples：

	backend abc
	 option mysql-check user haproxy post-41
	 server srv1 10.0.0.1:3306 check
	 
### 自定义TCP检查规则

1.comment：注释
2.tcp连接110端口
3.如果返回字符串包含+OK则正常

	backend be_pop
	 option tcp-check
	 tcp-check comment pop
	 tcp-check connect 110
	 tcp-check expect string +OK
	 server srv1 10.0.0.1:110 check
	 