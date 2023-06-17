#Os 5 primeiros valores de forma sequêncial, dado:
# 1. T(1) = 1
# 2. T(2) = T(n - 1) + 3 para n >= 2


def recursivo(num):
    
    if num < 2:
        num = 1
        print(num)
    else:
        while num <= 15:
            num = (num - 1) + 3
            print(num)
            num += 1

recursivo(2)