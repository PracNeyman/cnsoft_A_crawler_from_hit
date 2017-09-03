# FFmpeg任意文件读取漏洞分析
作者：yaofeiNO1
日期：2017-07-31 15:41
浏览量：1241
> 简介：1. 漏洞描述
漏洞简述： 漏洞利用了FFmpeg可以处理HLS播放列表的特性，而播放列表可以引用外部文件。通过在AVI文件中添加自定义的包含本地文件引用的HLS播放列表，可以触发该漏洞并在该文件播放...

 链接：http://blog.csdn.net/yaofeino1/article/details/76422817
