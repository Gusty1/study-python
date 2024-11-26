"""
創建類
"""

# 1. 設計一個類
class Student:
    name = None
    gender=None
    age=None
    def say_hi(self):
        print("Hello, my name is " + self.name)

# 2. 創建一個對象
stu1 = Student()

# 3. 對象屬性進行賦值
stu1.name = "John"
stu1.gender = "Male"
stu1.age = 20

# 4. 獲取對象中紀錄的信息
print(stu1.name)
print(stu1.gender)
print(stu1.age)
stu1.say_hi()