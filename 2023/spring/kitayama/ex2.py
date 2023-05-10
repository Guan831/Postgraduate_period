import random

def before(seed_num):
    random.seed(seed_num)
    a = []
    for a1 in range(10):
        a.append(random.random())
    for a2 in range(len(a)):
        for a3 in range(len(a) - a2 -1):
            if a[a3] > a[a3+1]:
                a4 = a[a3]
                a[a3] = a[a3+1] 
                a[a3+1] = a4
    a5 = 0
    a5 += a[0]
    a5 += a[1]
    a5 += a[2]
    return a5

def after(seed_num):
    random.seed(seed_num)
    a = []
    for a1 in range(10):
        a.append(random.random())
    for a2 in range(len(a)):
        for a3 in range(len(a) - a2 -1):
            if a[a3] > a[a3+1]:
                a4 = a[a3]
                a[a3] = a[a3+1] 
                a[a3+1] = a4
    a5 = 0
    a5 += a[0]
    a5 += a[1]
    a5 += a[2]
    return a5

if __name__ == "__main__":
    # before関数は少なくとも3つの意味のある処理に分けることができる
    # before関数と同じ動作をし，なおかつコードを読むだけで意味が読み取りやすくなるようにafter関数を書き換えよ
    # なおrandom.seed(seed_num)は乱数を固定するために書いてあるので，意味には含めないものとする
    res_before = before(123)
    res_after = after(123)
    if res_before == res_after:
        print("同じだよ")
    else:
        print("違うよ")
