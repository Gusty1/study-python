"""
構造方法
"""

# 構造方法的名稱 __init__

class Student:
    name=None
    age=None
    gender=None
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
        # print('創建了一個student對象')

    # 等於ToString方法，不寫就輸出地址，寫了就輸出這個字串
    def __str__(self):
        return "Student(name={}, age={}, gender={})".format(self.name, self.age, self.gender)

    # 用於小於比較，必須返回true或false
    def __lt__(self, other):
        return self.age < other.age

    # 用於小於等於比較，必須返回true或false
    def __le__(self, other):
        return self.age < other.age

    # 用於相等比較，必須返回true或false
    # 沒有__eq__方法預設會是比較記憶體位址
    def __eq__(self, other):
        return self.age == other.age

# 建立一個 Student 物件
s1=Student("John", 20, "Male")
print(s1.name)
print(s1.age)
print(s1.gender)

s2=Student("Mike", 43, "Female")
print(s1.name)
print(s1.age)
print(s1.gender)

print(s1>s2)
print(s1<s2)

print(s1>=s2)
print(s1<=s2)

print(s1==s2)
print(s1==s2)
