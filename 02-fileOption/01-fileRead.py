# 檔案讀取

# 打開文件 open(路徑,模式,編碼)
f = open('./test.txt','r',encoding='UTF-8')
print(type(f))

# 讀取文件 read(數字) 數字表示要讀取的字節，不寫讀取全部內容，輸出是字串
# 注意: 讀取文件會紀錄上一次使用的位置，然後從該位置繼續讀取
content = f.read()
print(type(content))

# readline() 讀取一行，輸出是str
# content2 = f.readline()
# print(content2)

# readlines() 一行一行讀取，輸出是list，元素是字串
# content3 = f.readlines()
# print(content3)

# for 遍歷文件
# contents = f.readlines()
# for i in contents:
#     print(i)

# 關閉文件
# f.close()

# with open 操作，執行完以後會自動關閉
with open('./test.txt', 'r', encoding='UTF-8') as f:
    for i in f.readlines():
        print(i)
