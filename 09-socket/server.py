"""
socket 服務端演示
"""

import socket

# 建立socket對象
socket_server = socket.socket()

# 綁定IP位置和端口
socket_server.bind(('127.0.0.1',8888))

# 監聽端口(允許連接的數量)
socket_server.listen(1)

# 等待客戶端連接
# result = socket_server.accept()
# conn = result[0] #客戶端和服務端的連接對象
# address = result[1] #客路端的地址訊息
conn,address = socket_server.accept()
# accept方法返回的是二元元組(連接對象，客戶地址信息)
# 可以通過變量1，變量2 = socket_server.accept()的形式，直接接收二元元組內的2個返回信息
# accept()方法式阻塞的方法，如果沒有連接就會卡住，不會向下執行

print(f'接收到了客戶端的連接，客戶端的信息是: {address}')

# 接收客戶端信息
data = conn.recv(1024).decode('UTF-8')
# recv(緩衝區大小)，一般給1024即可
# 返回的值是byte，需要用decode('UTF-8')轉換成字串
print(f'客戶端發來的消息是: {data}')

# 發送回應消息
msg =input('請輸入回應消息: ').encode('UTF-8')
conn.send(msg)

# 關閉連接
conn.close() # 關閉當前連接
socket_server.close()