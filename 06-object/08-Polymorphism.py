"""
多型的演示
"""

class Animal:
    def speak(self):
        pass

class Dog:
    def speak(self):
        print('Woof!')

class Cat:
    def speak(self):
        print('Meow!')

def make_noise(animal:Animal):
    animal.speak()

# 演示多型
dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)

# 抽象類別，以冷氣為例
class AC:
    def cool_wind(self):
        #製冷
        pass
    def hot_wind(self):
        #製熱
        pass
    def swing_l_r(self):
        #左右擺動
        pass

class Midea_AC(AC):

    def cool_wind(self):
        print('現在吹冷風')

    def hot_wind(self):
        print('現在吹熱風')

    def swing_l_r(self):
        print('現在左右搖擺')

def make_cool(ac:AC):
    ac.cool_wind()

midea_ac = Midea_AC()
make_cool(midea_ac)
