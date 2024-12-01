"""
正則表達式演示
"""

import re

s = 'python gusty python'

# match實現匹配
result = re.match('python', s)
print(result)
print(result.span())
print(result.group())
print('--------------------------------')

# search實現搜尋
result2 = re.search('python', s)
print(result2)
print(result2.span())
print(result2.group())
print('--------------------------------')

# findall實現找到所有匹配的字串

result3 = re.findall('python', s)
print(result3)
print('--------------------------------')
# 正則應用

ss = 'python gusty python 2'
# match實現匹配
# 帶上r標記，代表轉譯字符無效
result = re.findall(r'[a-z]', ss)
print(type(result))
print(result)

