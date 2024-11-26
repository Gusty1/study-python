# 元組一旦定義完成就不能修改

my_tuple = ('abc',123,True,'abc')
print(my_tuple)

# 如果元組只有單個元素，後面必須接,不然就不是元組
#my_tuple_a = ('abc')
my_tuple_a = ('abc',)
print(f"類型:{type(my_tuple_a)}，印出來:{my_tuple_a}")

# index(元素) 查找指定算元素出現的位置
print(my_tuple.index('abc'))

# count(元素) 查找指定元素出現的數量
print(my_tuple.count('abc'))

# len(tuple) 當前元組的元素數量
print(len(my_tuple))

# 元組遍歷
for i in my_tuple:
    print(i)

index = 0
while index<len(my_tuple):
    print(my_tuple[index])
    index+=1

# 元組不能修改，但如果元組裡面嵌套一個list可以修改
tuple_a = ([1,2,3],)
print(tuple_a)
tuple_a[0][1] = 9
print(tuple_a)