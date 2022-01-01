
def div():
    try:
        a = 10
        b = 0
        c = a / b
        print(c)
    except BaseException as e:
        print(10000)
        raise RuntimeError('testError')
    finally:
        print(10000)
#div()
import os
fp = open("test.txt",'a+')
fp.write('Hello')
