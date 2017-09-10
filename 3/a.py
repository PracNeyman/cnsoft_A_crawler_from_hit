import jieba
from wordcloud import WordCloud
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from PIL import Image,ImageTk


def wordCloud():
    file = open("cloud.txt")
    line = file.readline()
    space_split = ""
    while line:
        wordlist_after_jieba = jieba.cut(line, cut_all=True)
        wl_space_split = " ".join(wordlist_after_jieba)
        space_split += " "
        space_split += wl_space_split
        line = file.readline()
    my_wordcloud = WordCloud(background_color='white',font_path = "/System/Library/Fonts/PingFang.ttc").generate(
        space_split)
    plt.figure(figsize=(10, 8), dpi=600)
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.savefig("./src/5.png", dpi=800)
    file.close()
    plt.close('all')


wordCloud()