"""
閉包演示
"""


# 簡單閉包

def outer(logo):
    def inner(msg):
        print(f"<{logo}>{msg}</{logo}>")

    return inner


fn1 = outer("Python")
fn1("Hello, world!")
# 另一種寫法
outer("Python")("Hello World")


# 使用nonlocal修改外部變數的值

def outer2(num1):
    def inner2(num2):
        nonlocal num1
        num1 += num2
        print(num1)

    return inner2


fn2 = outer2(10)
fn2(20)

