# list可以存放不同類型的元素
list_a = ['abc',123,True]

# list索引可以用負的
print(list_a[-3])
print(list_a[-1])

# index(元素) 可以用元素來找位置
print(list_a.index(123))

# insert(位置,元素)指定位置插入指定元素
list_a.insert(2,'aaa')
print(list_a)

# append(元素) 添加到元素到最後
list_a.append(333)
print(list_a)

# extend(list) 將其他數據容器的內容取出，加到list尾部
list_b = [1,2,3]
list_a.extend(list_b)
print(list_a)

# del list[0] list.pop(1) 刪除指定位置元素
del list_a[0]
print(list_a)
list_a.pop(1)
print(list_a)

# list.remove(元素) 根據元素內容刪除
list_a.remove(123)
print(list_a)

# list.clear() 清空列表
list_a.clear()
print(list_a)

# list.count(元素) 指定元素在list的數量
list_a = [123,'aaa',123,'bbb']
print(list_a.count(123))

# len(list) list的元素數量
print(len(list_a))

# 遍歷list
for i in list_a:
    print(i)

index = 0
while index<len(list_a):
    print(list_a[index])
    index += 1
