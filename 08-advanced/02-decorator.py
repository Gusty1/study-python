"""
裝飾器演示
"""

# 裝飾器的一般寫法
# def outer(func):
#     def inner():
#         print('我睡覺了')
#         func()
#         print('我起床了')
#     return inner
#
# def sleep():
#     import random
#     import time
#     print('睡眠中...')
#     time.sleep(random.randint(1, 5))
#
# # sleep()
# fn = outer(sleep)
# fn()

# 裝飾器的快捷寫法(語法糖)
def outer2(func):
    def inner2():
        print('我睡覺了')
        func()
        print('我起床了')
    return inner2

@outer2
def sleep2():
    import random
    import time
    print('睡眠中...')
    time.sleep(random.randint(1, 5))

sleep2()