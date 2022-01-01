def inv(num):
    out = 0

    while num:
        out = out * 10 + num % 10

        num /= 10
        num = int(num)

    return out
print(inv(90000))
def fat(n):

    if n == 1:
        return 0
    elif n == 2:
       return 1
    else:
        return fat(n - 1) + fat(n - 2)
print(fat(4))