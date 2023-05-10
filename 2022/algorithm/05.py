# 5.3
import random
N = 7
W = 10
a = []
for i in range(10, 20):
    a.append(random.randint(1, 10))


def function_question_5_3(W):
    for i, n in enumerate(a):
        list_a = []
        list_a.append(n)
        cntN = n
        for b in range(i+1, len(a)):
            list_b = list_a
            while cntN <= W:
                cntN += a[b]
                if cntN > W:
                    break
                list_b.append(a[n])
            if len(list_b) > 1:
                print(list_b)


if __name__ == '__main__':
    print(a)
    print('上の中から和'+(str(W))+'とその以下の仕組みは')
    function_question_5_3(W)
