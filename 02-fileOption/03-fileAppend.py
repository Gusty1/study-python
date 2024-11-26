# 文件追加

# 打開文件
f=open('./test3.txt','a',encoding='UTF-8')

#寫入內容
f.write('\nhello world')

# 關閉文件
f.close()