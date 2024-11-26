"""
演示json和python的字典轉換
"""

import json

data = [
    {"name": "小王", "age": 10},
    {"name": "小明", "age": 20},
    {"name": "小張", "age": 30}
]
# 將字典轉換成json字串，有中文的話可以用ensure_ascii=False來正常顯示中文
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)

# 將json字串轉換成字典
new_dict = json.loads(json_str)
print(type(new_dict))
print(new_dict)