以下是haproxy的一些常见参数提取，帮助更好的配置维护。

### 数据样本的类型：

* boolean
* integer
* ip
* string
* binary



### 内部状态信息

* avg_queue(backend):队列总数
* be_conn(backend):当前连接数
* be_sess_rate(backend):每秒会话创建速率
* fe_conn(frontend):当前连接数
* fe_sess_rate(frontend):每秒会话创建速率
* nbsrv(backend):返回可用的服务器数量
* srv_conn(backend/server):当前连接数
* srv_is_up(backend/server):server状态 true/false
* srv_sess_rate(backend/server):server每秒会话创建速率
* date():返回时间 从1970/01/01到现在的秒数
* env(name):返回一个环境变量
* rand(range):返回一个随机数,0-range可选参数


### 4层状态信息

* be_id:返回当前backend id
* dst:目的地址
* dst_port:目的端口
* dst_conn:当前连接数
* fe_id:返回当前frontend id
* so_id:返回当前listen id
* src:源地址
* src_port:源端口
* srv_id:返回当前server id


### 7层状态信息

* capture.req.hdr(idx):获取一个捕获请求头
* capture.req.method:获取http请求方法
* capture.req.uri:获取请求的url
* capture.req.ver:获取http请求版本
* req.body:获取http请求的body块数据
* req.body_len:获取body长度
* req.body_size:获取body大小
* req.body_param(name):获取body参数，一般为post参数
* req.cook(name):从cookie中获取一个值
* req.cook_cnt(name):该cookie出现的次数
* req.cook_val(name):获取一个cookie的值并转化为整形
* req.hdr(name):从头部中获取一个值
* req.hdr_cnt(name):该头部出现的次数
* req.hdr_val(name)获取一个头部的值并转化为整形
* status:返回http请求状态
* path:请求路径，没有主机名和get参数
* url:完整的请求路径
* urlp(name):获取url的参数
* urlp_val(name):获取url的参数并转换为整形