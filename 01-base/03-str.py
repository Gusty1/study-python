# 字符串

str_a = 'today'
for i in str_a:
    print(i)
print(str_a[1])
print(str_a[4])

# 字符串是不可修改的
#str_a[0]='b'

# strip(字符串) 字符串不寫會去掉前後空格和換行，有字符串則去除指定的字符串
str_1 = ' abaabbbcccba    '
print(str_1.strip())

# 不知道為什麼字串前後空白會影響strip，所以用strip記得先去空白
str_2 = 'abaabbbcccba'
# strip(字符串) 並不是去掉指定的字串，而是將字串拆成字元，然後把相符的都去掉
print(str_2.strip('ab')) # 輸出ccc
