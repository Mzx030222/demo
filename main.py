
def my_sumB(n):
    sum = 0
    if n == 1:
        sum = 0
    elif    n == 2:
        sum = 1
    else:
        sum = my_sumB(n - 1) + my_sumB(n - 2)
    return sum


print(my_sumB(1))


def inv(num):
    out = 0
    if num == 0:
        out = 0
    else:
            out = out * 10 + num % 10
            num /= 10
            num = int(num)
    return out
print(inv(5))



