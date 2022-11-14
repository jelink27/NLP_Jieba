import jieba
import pandas as pd
import imageio.v2 as imageio
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

# data = pd.read_csv('122.csv',engine='python',skiprows =1,
#                        names=['temp','tourist_id','comment_user','comment_star','comment'])
#print(data.comment)

stopfile = "stop_words.txt"  # stopwords

with open(stopfile,'r',encoding="utf-8") as f:stop_words = f.readlines()
stop_words = [stop_word.rstrip() for stop_word in stop_words]
print(stop_words)
new_list = []


#檔案讀取
for i in range(10):
    pass


for i in range(392,394):
    file_name = str(f'{i}.csv')
    print(file_name)
    data = pd.read_csv(f'{file_name}',engine='python',skiprows =1,
                    names=['temp','tourist_id','comment_user','comment_star','comment']) 
    # print(data.head())
    for j in range(len(data['comment'])): 
        print(data.comment[j])
        seg_list = jieba.lcut(data.comment[j], cut_all=False)
        for seg in seg_list:
            if seg not in stop_words:
                new_list.append(seg)
        jieba_list=' '.join(new_list)
        #print(jieba_list)
        #產生文字雲
    mask = imageio.imread('taipei.jpg')
    image_colors = ImageColorGenerator(mask)
    wc = WordCloud(
        background_color='black',
        mask=mask,
        random_state=10,
        font_path='Iansui094-Regular.ttf',
        prefer_horizontal = 1,
        repeat=False,
        min_font_size = 35, #35~50
        max_font_size=450 #原本300
        )

    wc.generate(jieba_list)
    image_colors = ImageColorGenerator(mask)
    wc.recolor(color_func=image_colors) 
    wc.to_file(f'{i}.png')
        

'''
    #使用jieba斷詞後存成list使用
for j in range(len(data['comment'])): 
    print(data.comment[j])
    seg_list = jieba.lcut(data.comment[j], cut_all=False)
    for seg in seg_list:
        if seg not in stop_words:
            new_list.append(seg)
    jieba_list=' '.join(new_list)
    #print(jieba_list)
    #產生文字雲
'''

# mask = imageio.imread('taipei.jpg')
# image_colors = ImageColorGenerator(mask)
# wc = WordCloud(
#     background_color='black',
#     mask=mask,
#     random_state=10,
#     font_path='Iansui094-Regular.ttf',
#     prefer_horizontal = 2,
#     repeat=False
#     )

# wc.generate(jieba_list)
# image_colors = ImageColorGenerator(mask)
# wc.recolor(color_func=image_colors) 
# wc.to_file(f'{i}.png')
        

# data = pd.read_csv('122.csv',engine='python',skiprows =1,
#                        names=['temp','tourist_id','comment_user','comment_star','comment'])
#print(data.comment)    

# for j in range(len(data['comment'])): 
#         print(data.comment[j])
#         seg_list = jieba.lcut(data.comment[j], cut_all=False)
#         for seg in seg_list:
#             if seg not in stop_words:
#                 new_list.append(seg)
#         jieba_list=' '.join(new_list)
#         #print(jieba_list)

# mask = imageio.imread('taipei.jpg')
#         image_colors = ImageColorGenerator(mask)
#         wc = WordCloud(
#             background_color='black',
#             mask=mask,
#             random_state=10,
#             font_path='Iansui094-Regular.ttf',
#             prefer_horizontal = 2,
#             repeat=False
#             )

#         wc.generate(jieba_list)
#         image_colors = ImageColorGenerator(mask)
#         wc.recolor(color_func=image_colors) 
#         wc.to_file(f'{i}.png')










