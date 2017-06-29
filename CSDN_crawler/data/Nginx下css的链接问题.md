# Nginx下css的链接问题
作者：lzhlzz
日期：2016-11-20 14:13
浏览量：855
> 简介：放在 Nginx 下的网页代码，在链接外部 css 文件时，可能出现没有链接成功的问题。需要在 nginx.conf 里的 http 下添加一行。http {
include mime.types;

 链接：http://blog.csdn.net/lzhlzz/article/details/53240674
