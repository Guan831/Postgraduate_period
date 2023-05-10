import turtle
import math

#         0  1  2  3  4  5  6
list_A = [2, 9, 6, 1, 7, 8, 5]
list_B = [8, 7, 1, 2, 3, 6, 4]
list_C = [0, 2, 4, 5, 0, 1, 7, 8, 0]
# code 3.1線形探索法


def function3_1(n, k=[]):
    for i in k:
        if i is n:
            return True
    return False

# code 3.2特定の要素の存在する添字も取得


def function3_2(n, k=[]):
    for j, i in enumerate(k):
        if i is n:
            return j
    return -1

# code 3.3最小値を求める


def function3_3(k=[]):
    min = k[1]
    for i in k:
        if i < min:
            min = i
    return min

# code 3.4ペアの全探索


def function3_4(k1=[], k2=[]):
    # 1

    min = k1[0]+k2[0]
    for i in k1:
        for j in k2:
            if min > i+j:
                min = i+j

    # 2
    #min = function3_3(k1)+function3_3(k2)
    return min

# code 3.6　部分和問題に対するビットを用いる全探索解法
# ???


def function3_6(N, W, a=[]):
    return False

# code 問題3.1


def function_question_3_1(n, k=[]):
    found_id = -1
    for j, i in enumerate(k):
        if i is n:
            found_id = j
    return found_id

# code 問題3.2


def function_question_3_2(n, k=[]):
    cnt = 0
    for i in k:
        if i is n:
            cnt += 1
    return cnt

# code 問題3.3


def function_question_3_3(k=[]):
    if k[0] < k[1]:
        min = k[0]
        sec_min = k[1]
    else:
        min = k[1]
        sec_min = k[0]
    for i in k:
        if i < min:
            sec_min = min
            min = i
    return sec_min

# code 問題3.4


def function_question_3_4(k=[]):
    min = k[0]
    max = k[0]
    for i in k:
        if i < min:
            min = i
        if i > max:
            max = i
    return max-min

# code 問題3.5


def function_question_3_5(k=[]):
    while(1):
        cont = 0
        for j, i in enumerate(k):
            if i % 2 == 0:
                k[j] = i/2
                cont = 1
        if cont == 0:
            return k

# code 問題3.6


def function_question_3_6(K, N):
    x = 0
    cnt = 0
    while x <= K:
        y = 0
        while y <= K:
            z = N-x-y
            if z <= K and z >= 0:
                cnt += 1
                print(x, y, z)
            y += 1
        x += 1
    return cnt

# code 問題3.6


def function_question_3_7(K=[]):
    sum = 0
    return sum


if __name__ == '__main__':
    # 3.1 特定の数字を探索
    #print(function3_1(7, list_A))

    # 3.2 特定の要素の存在する添字も取得
    # print(function3_2(0, list_A))

    # 3.3最小値を求める
    # print(function3_3(list_A))

    # 3.4ペアの全探索
    #print(function3_4(list_A, list_B))

    # 3.5組み合わせの全探索
    # 3.6部分和問題に対するビットを用いる全探索

    # 問題3.1
    #print(function_question_3_1(8, list_A))

    # 問題3.2
    #print(function_question_3_2(0, list_C))

    # 問題3.3
    # print(function_question_3_3(list_A))

    # 問題3.4
    # print(function_question_3_4(list_A))

    # 問題3.5
    # print(function_question_3_5(list_A))

    # 問題3.6
    print(function_question_3_6(3, 5))

    # 問題3.7
    # print("")
