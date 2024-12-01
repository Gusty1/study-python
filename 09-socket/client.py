"""
socket客戶端演示
"""

import socket

# 創建socket對象
socket_client = socket.socket()

# 連接到服務器
socket_client.connect(('127.0.0.1', 8888))

# 發消息
socket_client.send('你好，我我我'.encode('UTF-8'))

# 接收返回消息
recv_data = socket_client.recv(1024).decode('UTF-8')
print(f'接收到的回應訊息: {recv_data}')

# 關閉連接
socket_client.close()