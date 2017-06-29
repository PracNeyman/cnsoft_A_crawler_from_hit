#coding:utf-8
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import jieba
import numpy as np
from PIL import Image

#读入背景图片
#abel_mask = np.array(Image.open('color.jpg'))

#读取要生成词云的文件
text_from_file_with_apath = open('alice.txt').read()

#通过jieba分词进行分词并通过空格分隔
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
#my_wordcloud = WordCloud().generate(wl_space_split) 默认构造函数
my_wordcloud = WordCloud(background_color='white',font_path='/System/Library/Fonts/STHeiti Light.ttc').generate(wl_space_split)

# 根据图片生成词云颜色
# image_colors = ImageColorGenerator(abel_mask)
#my_wordcloud.recolor(color_func=image_colors)

# 以下代码显示图片
plt.figure(figsize = (10,8),dpi = 600)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.savefig("a.png",dpi = 600)
plt.show()
