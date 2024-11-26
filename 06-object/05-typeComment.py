"""
演示變量的類型註釋
"""
import json
import random

# 基礎數據類型註釋
var_1: int = 10
var_2: str = 'hello world'
var_3: bool = True

# 對象類型註釋
class Student:
    pass
stu:Student = Student()

# 基礎容器類型註釋
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {'name': 'Alice', 'age': 20}

# 容器類型註釋
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int,str,bool] = (1, 'aaa', True)
my_dict: dict[str,int] = {'age': 20}

# 在註釋中進行註釋
var_1 = random.randint(1,10) # type:int
var_2 = json.loads('{"name": "Alice"}') # type:dict[str,str]
def func():
    return 10
    pass
var_3 = func() # type:int

# 類型註釋的錯誤
# 類型註釋沒有強制性，只能建議你不要寫錯
var_4:int = '123'
var_5:str = 123

