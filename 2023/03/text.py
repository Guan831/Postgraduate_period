def text() -> str:
    return "Hello, World!"

# 声明一个输出质数的函数，输入n，输出n以内质数


def prime_number(n: int) -> list:
    """
    输入一个数字，输出该数字以内的质数
    """
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result


if __name__ == "__main__":
    print(prime_number(100))
