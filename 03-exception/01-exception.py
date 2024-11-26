# 異常處理

# 基本使用
try:
    a = '123'
    b= 123
    c = a+b
    print(c)
except Exception  as e:
    print(e)
finally:
    print('end')

# 捕獲指定異常
# try:
#     a = '123'
#     b= 123
#     c = a+b
#     print(c)
# except TypeError as a:
#     print(a)