# 寫入文件

# 打開文件
f= open('./test2.txt','w',encoding='UTF-8')

# 文件不存在會創建文件，文件存在會把寫入內容清空後再重寫入
# write 寫入內容
f.write('12345')

# 刷新文件
f.flush()

# 關閉 close有內置flush功能
f.close()

