# 集合，不允許重複，且無順序的，可以修改
my_set = {"aaa","bbb","ccc","aaa","bbb","ccc"}
print(my_set)

# add(元素) 添加新元素
my_set.add('python')
print(my_set)

# remove(元素) 移除元素
my_set.remove('aaa')
print(my_set)

# pop() 隨機取出一個元素
element = my_set.pop()
print(element)

# clear() 清空集合
my_set.clear()
print(my_set)

# difference(集合)取2個集合的差集
set1={1,2,3}
set2={2,5,6}
set3=set1.difference(set2)
print(set3)

# 消除差集，只會改變set1，消除相同的結果
set1={1,2,3}
set2={2,5,6}
set1.difference_update(set2)
print(set1)
print(set2)

# union() 集合合併，注意一樣是沒有重複的
set1={1,2,3}
set2={2,5,6}
set3= set1.union(set2)
print(set3)

# 遍歷，無順序，不能用while
my_set = {"aaa","bbb","ccc","aaa","bbb","ccc"}
for i in my_set:
    print(i)