# C# 性能优化最佳实践
作者：xunzaosiyecao
日期：2016-11-20 19:49
浏览量：1768
> 简介：1、使用泛型来避免装箱、拆箱操作。
        装箱操作会造成GC压力；如果发生在集合中，应该使用泛型集合避免。
        对于值类型的集合，使用List来代替ArrayList，使用Dic...

 链接：http://blog.csdn.net/jiankunking/article/details/18664043
