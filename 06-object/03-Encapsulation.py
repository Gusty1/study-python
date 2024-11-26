"""
封裝演示
"""

class Phone:
    __current_name = '12'

    def __run_go(self):
        print("Running...")

    def call(self):
        if self.__current_name != None:
            print('OK')

p1 = Phone()
p1.__current_name = "John"
p1.call()