# ss-libev 源码解析udp篇 (4)
作者：n5
日期：昨天 17:31
浏览量：475
> 简介：本篇分析remote_recv_cb，这是整个udp转发的反方向，即读取从后端发送过来的数据再发送给前端。对于ss-server，读取到的数据是目标地址的udp服务器发送回来的响应数据，ss-serv...

 链接：http://blog.csdn.net/n5/article/details/73743541
