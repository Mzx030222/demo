def inv(num):
    out = 0
    if num == 0:
        out = 0
    else:
        while num:
            out = out * 10 + num % 10
            num /= 10
            num = int(num)
    return out
print(inv(123))

def inv(num):


    while num:
        print(num % 10)

        num /= 10
        num = int(num)
    return 1

print(inv(12345))
c = inv(12345)
print(c)
