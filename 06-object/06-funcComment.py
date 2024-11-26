"""
函數類型註釋
"""


# 對參數進行類型註釋
def add(a: int, b: int):
    return a + b


print(add(1, 2))


# 對函數返回值進行類型註釋
def func(data: str) -> str:
    return data


print(func('hello world'))
