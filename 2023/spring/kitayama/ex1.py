def before():
    a = list(range(30))
    result = []
    temp = []
    temp.append(a[0])
    temp.append(a[1])
    temp.append(a[2])
    result.append(temp)
    temp = []
    temp.append(a[3])
    temp.append(a[4])
    temp.append(a[5])
    result.append(temp)
    temp = []
    temp.append(a[6])
    temp.append(a[7])
    temp.append(a[8])
    result.append(temp)
    temp = []
    temp.append(a[9])
    temp.append(a[10])
    temp.append(a[11])
    result.append(temp)
    temp = []
    temp.append(a[12])
    temp.append(a[13])
    temp.append(a[14])
    result.append(temp)
    temp = []
    temp.append(a[15])
    temp.append(a[16])
    temp.append(a[17])
    result.append(temp)
    temp = []
    temp.append(a[18])
    temp.append(a[19])
    temp.append(a[20])
    result.append(temp)
    temp = []
    temp.append(a[21])
    temp.append(a[22])
    temp.append(a[23])
    result.append(temp)
    temp = []
    temp.append(a[24])
    temp.append(a[25])
    temp.append(a[26])
    result.append(temp)
    temp = []
    temp.append(a[27])
    temp.append(a[28])
    temp.append(a[29])
    result.append(temp)
    return result


def after_for(n, m):
    a = list(range(n))
    result = []
    cnt = n//m
    for i in range(cnt):
        temp = []
        for j in range(m):
            temp.append(a[i*m+j])
        result.append(temp)
    return result


def after(n, m):
    return after_for(n, m)


if __name__ == "__main__":
    # after関数の中身をなるべく行数が少なくなるように書き換え，before関数と同じ結果を得よ
    # なお，任意の長さのリストを任意の長さに分割して格納できるようにするとなおよい
    res_before = before()
    res_after = after(30, 3)
    if res_before == res_after:
        print("同じだよ")
    else:
        print("違うよ")
