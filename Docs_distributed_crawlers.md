#分布式爬虫系统

> 哈尔滨工业大学：武德浩，万丁，李博


> 题目要求：
> 
> 爬虫系统，是对海量的分散的互联网数据进行采集的系统，是搜索引擎系统的基础。大数据近年来快速发展，炙手可热，不仅是数据的容量大，更是强调对全样本的数据的分析。互联网数据中包含了大量有价值信息，是大数据的重要数据来源。
而互联网上的数据内容丰富，组织形式也灵活多样。传统的爬虫系统，对所有的网页采用同样的办法处理，利用深度优先或广度优先的办法获取网页链接，下载网页，对网页中的所有的文本数据建立倒排索引。这种方式没有对网页数据的信息进行组织、归类。
应大数据的需求，分布式爬虫系统是解决这一问题的方案。分布式爬虫，对同一个网站的同类数据，进行结构化。同时，能利用分布式的软件设计方法，实现爬虫的高效采集。

本次我们主要实现了两个爬虫系统，分别用于电商网站和博客网站的爬取，具体信息如下。

##基于redis实现分布式爬虫的淘宝网站信息爬取及词云展示

###前言

本次我们首先开始的是针对于淘宝（天猫）网站的关于商品Url，商品价格，商品评论，店铺Url，店铺信息，店铺地址，店铺信用排名等各种数据的爬取，然后通过我们后期处理，组织，对商品进行数据的管理，可视化，以及对评论进行词云生成，以方便使用者在庞大的数据下能够有效的提取出有用的信息。

> 电商网站中的数据具有极大的价值，而同样也正是如此，各大电商网站对于爬虫都有较为完善的反爬虫机制，且网站结构变化快，时效性极高，不同网站数据组织不同，分类标签不同，需要人工针对不同的网站定制不同的爬虫，而且由于淘宝，京东等网站体量极大，我们在爬取的过程中，如果仅仅使用传统爬虫，除开被封禁 IP 的危险，更会受限于效率，让我们无法在所需要的时间内爬取到相应的信息，此外关于Url去重，爬取过程中时间与空间的博弈等等需求，都让电商类网站爬虫的制作困难重重。

在这样的任务要求上，我们基于传统的爬虫进行了改进，经过广泛的学习与思考之后，我们采用了 redis 数据库实现了一个分布式结构化的爬虫，可以对于淘宝（天猫）网站进行多个线程的同时爬取，其效率和效果都远远的高于我们最开始的传统爬虫。

###前提环境、架构

开发语言：Python 3.6

开发环境: Windows 10、8G内存，Core I5 处理器

数据库：Redis

###实现方式说明

我们利用 redis 实现了 master + slaver 的分布式爬虫思想。

主要策略如下图：
![pic 1](https://ooo.0o0.ooo/2017/06/28/595397f34e61e.jpg)

我们设置了一个 master.py 文件用于管理 request ，发送给 slaver.py 需要爬取的页面请求，由 slaver.py 完成页面信息的提取，中间对于 url 的处理我们使用 redis 进行管理，以便于处理多线程之间的通信。

[武德浩补充]

此外我们的爬虫中还有一个 getIP 文件，此文件的作用主要是用于实现 IP 池的管理，我们通过从一个专门的代理网站去爬取当下可用的热门 IP ，实时对 slaver 更换 IP 去进行爬取，以防止单一 IP 遭到淘宝的反爬虫策略的封禁。

![pic 2](https://ooo.0o0.ooo/2017/06/28/5953997a8ff47.png)

###爬虫的运行与测试

##基于scrapy + mongodb实现的CSDN博客文章爬取

> 互联网是企业进行发布信息的渠道，是个人共享和获取信息的工具，同时也为政府提供了大量有价值的信息，用于监管企业和个人。政府有效的利用互联网的信息，能发现舆论倾向，建立征信体系，发现犯罪行为等。

###前言

对于这个题目，我们选取了国内著名的技术类型博客网站CSDN进行相应的爬取，我们通过scrapy框架进行爬虫的构建，实现网站结构的自动化分析（提取下一页url，提取当前文章的title，info，author，content等），生成对应的.md文件（如下图），方便用户简略查看，然后将主体的数据存入mongoDB作为储备。


###前提环境、架构

开发语言：Python 3.6

开发环境: OS X、8G内存，Core I5 处理器

框架：Scrapy + MongoDB

### 实现方式说明

####Scrapy框架
我们注意到题目中提到爬虫的通用化，在我们目前了解的知识背景中，Scrapy正是这样的是一个为了爬取网站数据，提取结构性数据而编写的应用框架。 
<div><center>![pic 6](http://opmza2br0.bkt.clouddn.com/17-6-29/88493134.jpg)</center></div>


可以应用在包括数据挖掘，信息处理或存储历史数据等一系列的程序中。

Scrapy 使用 Twisted这个异步网络库来处理网络通讯，架构清晰，并且包含了各种中间件接口，可以灵活的完成各种需求。

其项目组成大致如下

```
scrapy.cfg
csdn/
    __init__.py
    items.py
    pipelines.py
    settings.py
    spiders/
        __init__.py
        csdn.py
        ...
```

通过为各个组件编写相应的爬虫程序，分析网站之后编写xpath选择方式，再利用scrapy已有的现成接口，我们可以很快捷的开发出对应网站所需求的爬虫。

当然这个框架还有许多比如利用middleware实现的功能更丰富的如代理等，将在下面介绍。

###MongoDB

在scrapy，我们可以通过在settings里面增加 MongoDB 的IP以及端口，来使得我们可以通过使用pymongo这个模块与MongoDB通信，把爬虫爬取的数据写到数据库中的collection中。

设置好了之后我们只需要再修改存储的管道pipeline的信息：原本用于.json或者是其他方式输出的信息，我们现在将其打包成为一个item，然后存放到数据库里。

![pic 7](http://opmza2br0.bkt.clouddn.com/17-6-29/65535613.jpg)

注意到的是，我们将除了正文之外的其他信息，以.md文档的方式存入了文件当中，可以方便用户的第一次选取，而更详细的完整信息，为了存储效率的需要，我们将其存入了MongoDB当中。

![pic 3](http://opmza2br0.bkt.clouddn.com/17-6-29/46060909.jpg)

![pic 4](http://opmza2br0.bkt.clouddn.com/17-6-29/40031375.jpg)

###IP池以及代理的选取

通过Scrapy定义的中间件的方式，我们可以实现IP及代理的变换，首先我们在运行爬虫之前，先去IP网站上利用一个小型爬虫爬取出当前可用的IP，作为我们的IP池来选取。

![pic 8](http://opmza2br0.bkt.clouddn.com/17-6-29/36283606.jpg)

![pic 7](http://opmza2br0.bkt.clouddn.com/17-6-29/87549374.jpg)

然后在爬取好了之后我们在scrapy框架中导入这些代理。

```
def get_random_proxy(self):   
    while 1:  
        with open('/Users/luodian/Desktop/csdn/proxies.txt', 'r') as f:
            proxies = f.readlines()
        if proxies:
            break
        else:
            time.sleep(1)
    proxy = random.choice(proxies).strip()
    return proxy
```

然后在处理每次request请求时，使用我们下载的这些IP。

```
def process_request(self,request, spider):  
    '''对request对象加上proxy'''  
    proxy = self.get_random_proxy()  
    print("this is request ip:"+proxy)  
    request.meta['proxy'] = proxy   


def process_response(self, request, response, spider):  
    '''对返回的response处理'''  
    # 如果返回的response状态不是200，重新生成当前request对象  
    if response.status != 200:  
        proxy = self.get_random_proxy()  
        print("this is response ip:"+proxy)  
        # 对当前reque加上代理  
        request.meta['proxy'] = proxy   
        return request  
    return response  
```

如上，这样就实现了动态更新IP，远远地降低了被目标网站封禁的风险。


###爬虫的运行及测试

首先我们在命令行下进入到爬虫的文件夹，执行如下的命令。

```
scrapy crawl csdnblog
```

在命令行中自动开始爬取我们所需求的信息，并且在每次保存成.md文件的同时都输出一次，便于我们管理爬虫的运行状态。

这里把LOG_LEVEL的级别调为了INFO，可以省略一些不必要的信息，可以让我们只关注主要呈现出来的那部分内容。

![pic](http://opmza2br0.bkt.clouddn.com/17-6-29/80054343.jpg)

爬下来的文件同时存储到了本地以及数据库。

![pic](http://opmza2br0.bkt.clouddn.com/17-6-29/48614044.jpg)

![pic](http://opmza2br0.bkt.clouddn.com/17-6-29/48301273.jpg)

在实时更换IP以及代理的情况下理论上我们可以无限制的爬下CSDN上所有的文章，但是我们的带宽有限，我们并没有进行全局爬取的测试。

在演示视频中的几十秒的爬取之中，我们成功爬取了将近6000个页面，得到了几十兆的数据。

![pic](http://opmza2br0.bkt.clouddn.com/17-6-29/90713477.jpg)







