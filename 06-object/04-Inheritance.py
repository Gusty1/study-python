"""
繼承演示
"""


class Phone:
    # 序號
    id = None
    # 廠牌
    producer = 'XX'

    def call_by_4g(self):
        print('4G通話')


# 單繼承演示
class Phone2024(Phone):
    # 面部識別id
    face_id = 111

    def call_by_5g(self):
        print('2024新功能 5G通話')


phone2024 = Phone2024()
print(phone2024.id)
print(phone2024.producer)


# 多繼承演示
class NFCReader:
    nfc_type = '第五代'

    def read_card(self):
        print('讀取卡片')


class MyPhone(Phone, NFCReader):
    # 如果裡面不想寫裡面可以寫個pass就好
    pass


my_phone = MyPhone()
print(my_phone.id)
my_phone.call_by_4g()
print(my_phone.nfc_type)


# 覆寫父類成員方法
class MyPhone2(Phone):
    id = 123

    def call_by_4g(self):
        print('我是 新 4G通話')
        # print('老id: ' + super().id)
        print('老id: ' + str(super(MyPhone2, self).id))

phone2 = MyPhone2()
print(phone2.id)
phone2.call_by_4g()
