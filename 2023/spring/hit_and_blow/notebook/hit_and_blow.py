# In[]

"""
・人が合っていれば1blow、人と位置が合っていれば1hit       
・少ないturn数で3hitを目指す     
・1回答で1trun経過する     
・1回hintを使用したら1turn経過する     
・変な入力によるValueErrorは考慮していない     
・出力画面が足りない場合、「in a text editor」
"""


# In[]
import pandas as pd
import numpy as np
import random
import os
import time
import readline

INPUT = '../input'
SEED = 0

ans = pd.read_csv(os.path.join(
    INPUT, '/Users/aite/Public/2021Guan/2021_Guan/2023/spring/hit_and_blow/input/kaitou.csv'))

question = ['Q1.あなたの性別は？->「0.男, 1.女」',
            'Q2.あなたの年次は？->「0.B3, 1.それ以外」',
            'Q3.好きなスポーツは？->「0.野球, 1.サッカー」',
            'Q4.好きな食べ物は->「0.焼肉, 1.寿司」',
            'Q5.夏と言えば？->「0.海, 1.花火」',
            'Q6.北山先生は？->「0.かっこいい, 1.かわいい」',
            'Q7.生まれ変わるなら？->「0.きゅうりが食べられない河童, 1.鼻が短い天狗」',
            'Q8.現在、付き合っている（結婚）している人が？->「0.いる, 1.いない」',
            'Q9.もち運びやすそうなひらがなは？->「0.へ, 1.つ」',
            'Q10.旅行にいくなら？->「0.群馬県, 1.滋賀県」',
            'Q11.なくなったら困るのは？->「0.shiftキー, 1.Enterキー」',
            'Q12.なくなったら困るのは？（パート2）->「0.slack, 1.Dropbox」',
            'Q13.好きなテレビのジャンルは？->「0.ドラマ, 1.バラエティー」',
            'Q14.好きなお菓子は->「0.きのこの山, 1.たけのこの里」',
            'Q15.春メニューと言えば->「0.研究MTG, 1.勉強会」']

people = {1: "北山", 2: "小竹", 3: "関", 4: "堀川", 5: "大岡",
          6: "小柳", 7: "斉藤", 8: "笹本", 9: "水野", 10: "星", 11: "吉倉"}


def get_key(d, val_search):
    keys = [key for key, value in d.items() if value == val_search]
    if keys:
        return keys
    else:
        return None

# 答え生成


def rand_ints_nodup(a, b, k):
    ns = []
    while len(ns) < k:
        n = random.randint(a, b)
        if not n in ns:
            ns.append(n)
    return ns


def hit_blow(x, ans):
    hit = 0
    blow = 0
    for i in range(3):  # len(x)
        if x[i] == ans[i]:
            hit += 1
        else:
            if x[i] in ans:
                blow += 1

    return [hit, blow]


def hit_blow_a(q, a):
    x1, x2, x3 = q.split(',')
    x = [get_key(people, x1)[0],
         get_key(people, x2)[0],
         get_key(people, x3)[0]]
    h, b = hit_blow(x, a)
    if h == 3:
        print(' ')
        print('<<<<< Game Clear >>>>>')
        print(' Turn Score: '+str(turn)+'turn')
    else:
        """
        print(' --------- ')
        print('|hit :' +str(h)+ '|')
        print('|blow:' +str(b)+ '|')
        print(' --------- ')
        """
        print('hit  : ' + str(h))
        print('blow : ' + str(b))
    return h


# In[]
a = rand_ints_nodup(1, 11, 3)

hint = 0
hit = 0
turn = 0

print('答え入力例「水野,堀川,大岡」')

# ターンごとにループ
while True:
    turn += 1
    print(' ')
    print('-------------------- turn' + str(turn)+' --------------------')
    time.sleep(1)
    q = input('              答えを入力してください（hintが欲しいなら「hint」と入力してね）')

    if 'hint' in q:
        if hint != 0:
            print('              hintは2回連続では使えません。回答してね。')
            q = input('              答えを入力してください')
            print('「'+q+'」')
            time.sleep(1)
            hit = hit_blow_a(q, a)
            hint = 0
            if hit == 3:
                break
        else:
            hint += 1
            random_q = random.randint(1, 15)
            help_list = [ans.iloc[:, random_q-1][i] for i in range(3)]

            print('<< hint >>')
            print(question[random_q-1])
            print('正解アンケート結果: ' + str(help_list[0]) + ',' +
                  str(help_list[1]) + ',' + str(help_list[2]))
    else:
        hint = 0
        print('「'+q+'」')
        hit = hit_blow_a(q, a)
        if hit == 3:
            break

# %%
