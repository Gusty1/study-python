"""
多線程演示
"""
import time
import threading


def sing(msg):
    while True:
        print(msg)
        #睡眠1秒
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    # sing()
    # dance()

    #創建一個唱歌的線程，args傳入tuple參數
    sing_thread = threading.Thread(target=sing,args=('唱歌中...',))
    # 創建一個跳舞的線程，kwargs傳入字典參數
    dance_thread = threading.Thread(target=dance,kwargs={'msg':'跳舞中...'})

    # 執行線程
    sing_thread.start()
    dance_thread.start()


