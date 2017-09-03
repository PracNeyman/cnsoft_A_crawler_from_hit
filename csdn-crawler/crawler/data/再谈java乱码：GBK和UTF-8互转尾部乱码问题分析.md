# 再谈java乱码：GBK和UTF-8互转尾部乱码问题分析
作者：54powerman
日期：2017-08-25 16:08
浏览量：2003
> 简介：一直以为，java中任意unicode字符串，可以使用任意字符集转为byte[]再转回来，只要不抛出异常就不会丢失数据，事实证明这是错的。经过这个实例，也明白了为什么 getBytes()需要捕获异常...

 链接：http://blog.csdn.net/54powerman/article/details/77575656
