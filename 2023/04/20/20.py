import numpy as np

# 定义一个大小是100的全1数组
x = np.ones(100)

# 一个for循环，i从2到100
for i in range(2, 100):
    # 如果x[i]是1，那么就把x[i]开始的i的倍数都变成0
    if x[i] == 1:
        x[i::i] = 0
    print(i)
