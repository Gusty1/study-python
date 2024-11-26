# list切片
my_list = [1,2,3,4,5,6]

# 對list進行切片，從1開始，4結束，步長為1
result1 = my_list[1:4]
print(result1)

# 只寫個:跟一般遍歷一樣
result2 = my_list[:]
print(result2)

# 從頭開始，步長為2
result3 = my_list[::2]
print(result3)