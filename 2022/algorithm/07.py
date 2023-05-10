from re import T
import numpy as np
K1 = [[2, 4], [1, 9], [1, 8], [4, 9], [3, 12]]
K = [[334, 1000], [334, 1000], [334, 1000]]


X1 = [[2, 0, 0], [3, 1, 0], (1, 3, 0)]
X2 = [[4, 2, 0], [0, 4, 0], [5, 5, 0]]


def function_question_7_3(K):
    K = sorted(K, key=lambda x: x[1])
    time_K = 0
    for x in K:
        time_K += x[0]
        if time_K > x[1]:
            return False
    return True


def function_question_7_2(X1, X2):
    X1 = sorted(X1, key=lambda x: (x[0]+x[1]))
    X2 = sorted(X2, key=lambda x: (x[0]+x[1]))
    print(X1, X2)
    cnt = 0
    for x1 in X1:
        for x2 in X2:
            if x1[0] < x2[0] and x1[1] < x2[1] and x2[2] == 0:
                print(x1[0:2], x2[0:2])
                x2[2] = 1
                cnt += 1
                break
    return cnt


if __name__ == '__main__':
    print(function_question_7_2(X1, X2))
