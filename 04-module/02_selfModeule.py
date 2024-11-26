# 自定義模塊: my_module

# import my_module
# my_module.test(1,2)

from my_module import test

# __name__ 是 Python 內建的變數，用來判斷當前模塊是否為主模塊 (main module)
# 當 __name__ 等於 '__main__' 時，表示當前模塊為主模塊，可以執行程式的主要功能。
# 不然被引用的模塊程式回全部執行。
if __name__ == '__main__':
    test(2, 2)

from my_module2 import *

test_a(1, 2)
# 由於在my_module2__all__只有設定test_a，所以test_b會報錯
# __all__，只有在import *時才有作用，如果要使用test_b，還是可以手動去import
# test_b()
