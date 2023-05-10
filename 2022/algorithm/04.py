

def function_question_4_1(n):
    if (n == 0) or (n == 1):
        return 0
    elif (n == 2):
        return 1
    else:
        return (function_question_4_1(n-1)+function_question_4_1(n-2)+function_question_4_1(n-3))


if __name__ == '__main__':
    print(function_question_4_1(8))
