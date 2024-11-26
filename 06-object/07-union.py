"""
聯合類型註釋
"""

from typing import Union

# 聯合類型可以用來表示一個變數可以是多種型別的其中一個，沒有強制性

my_list:list[Union[int,str]] = [1,2,'a','b',True]

print(my_list)

def func(data:Union[int,str])->Union[int,str]:
    print(data)
    return data

func(True)