# volatile型变量自增操作的隐患
作者：bruce128
日期：2016-11-23 13:50
浏览量：2426
> 简介：用FindBugs跑自己的项目，爆出两处An increment to a volatile field isn’t atomic。相应报错的代码如下：volatile int num = 0;
nu...

 链接：http://blog.csdn.net/bruce128/article/details/53302958
