import pandas as pd
import numpy as np


'''
R = average for the movie (mean) = (Rating)
v = number of votes for the movie = (votes)
m = minimum votes required to be listed in the Top Movies list
C = the mean rating across the whole report

𝑊𝑅=(𝑣÷(𝑣+𝑚))×𝑅+(𝑚÷(𝑣+𝑚))×𝐶

WR = 評論的人數 / (評論的人數＋最少需要評論的人數) x 評論的平均分 + (最少需要評論的人數 (評論的人數 + 最少需要投票的人數) )

'''

for i in range(0,256):
    file_test = str(f'{i}.csv')
    print(file_test)
#     data = pd.read_csv(file_test)
#     print(data)

# r = round(data['評等'].mean(),3)
# v = data['評等'].count()
# m = 20.0
# c = 4.5

# wr = v / ( v + m ) * r + (m/(v+m))
# emo_score = data['emo_score']
# final_score = emo_score * 0.5 + wr *0.5
# print(f'景點{file_test}Goole平均得分為{r}')
# print(f'景點{file_test}投票的總人數為{v}人')
# print(f'WR score 推薦分數為{wr}')

