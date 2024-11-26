"""
lambda匿名函數，沒有名稱，只能臨時使用一次，只能寫一行
lambda 參數:返回值
"""

def test_func(compute):
    result = compute(1,2)
    print(result)

# 是把lambda這個函式當參數傳入test_func
test_func(lambda x,y:x+y)

