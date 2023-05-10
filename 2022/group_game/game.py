# coding:utf-8

import random
​
# 11人,9人
​if __name__ == '__main__':

    position = ['人狼', '人狼', '狂人', '占い師', '霊媒師', '市民', '市民', '市民', '市民']
    random.shuffle(position)
    ​
    hito = ['kitayama', 'horikawa', 'kotake', 'oooka',
            'koyanagi', 'makonya', 'mizuno', 'a1', 'a2']
    ​
    for position, hito in zip(position, hito):
        print(hito, position)
