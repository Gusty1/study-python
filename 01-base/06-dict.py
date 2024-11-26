# 字典
my_dict1 = {
    "naturo":99,
    "sasuke":60,
    "sakura":8
}

print(my_dict1)

# 透過key值取得value
print(my_dict1["naturo"])

# 新增、修改 key不存在就是新增
my_dict1["sasuke"] = 100
my_dict1["kakashi"] = 0
print(my_dict1)

# pop(元素)刪除元素
my_dict1.pop("kakashi")
print(my_dict1)

# clear()清空
my_dict1.clear()
print(my_dict1)

# keys()獲取字典全部的key
my_dict1 = {
    "naturo":99,
    "sasuke":60,
    "sakura":8
}
print(my_dict1.keys())

# 遍歷字典
for i in my_dict1.keys():
    print(f"name: {i}，score: {my_dict1[i]}")
