import pandas as pd
import numpy as np


'''
R = average for the movie (mean) = (Rating)
v = number of votes for the movie = (votes)
m = minimum votes required to be listed in the Top Movies list
C = the mean rating across the whole report

ðð=(ð£Ã·(ð£+ð))Ãð+(ðÃ·(ð£+ð))Ãð¶

WR = è©è«çäººæ¸ / (è©è«çäººæ¸ï¼æå°éè¦è©è«çäººæ¸) x è©è«çå¹³åå + (æå°éè¦è©è«çäººæ¸ (è©è«çäººæ¸ + æå°éè¦æç¥¨çäººæ¸) )

'''

for i in range(0,256):
    file_test = str(f'{i}.csv')
    print(file_test)
#     data = pd.read_csv(file_test)
#     print(data)

# r = round(data['è©ç­'].mean(),3)
# v = data['è©ç­'].count()
# m = 20.0
# c = 4.5

# wr = v / ( v + m ) * r + (m/(v+m))
# emo_score = data['emo_score']
# final_score = emo_score * 0.5 + wr *0.5
# print(f'æ¯é»{file_test}Gooleå¹³åå¾åçº{r}')
# print(f'æ¯é»{file_test}æç¥¨çç¸½äººæ¸çº{v}äºº')
# print(f'WR score æ¨è¦åæ¸çº{wr}')

