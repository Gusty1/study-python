import mysql.connector
from mysql.connector import Error
import pandas

# 操作資料庫
def connect_to_mysql(data_list):
    connection = None
    cursor = None
    try:
        # 建立連線
        connection = mysql.connector.connect(
            host='127.0.0.1',  # MySQL 伺服器地址
            database='pet_you',  # 資料庫名稱
            user='root',  # 使用者名稱
            password='root'  # 密碼
        )

        if connection.is_connected():
            print("connected success")

            # 建立 Cursor 物件以執行 SQL 語句
            cursor = connection.cursor()

            # 執行其他 SQL 查詢
            for  i  in data_list:
                print(i)
                sql = "INSERT INTO Test VALUES (null,%s, %s, %s)"
                cursor.execute(sql, (i['customer'], i['type'], i['rate']))

            # 提交變更
            connection.commit()
    except Error as e:
        print("連接資料庫時出現錯誤：", e)

    finally:
        # 確保關閉連線
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("資料庫連線已關閉")

# 讀取excel檔案
def read_excel():
    try:
        print('read excel file')

        """
        讀取 Excel 檔案(
            檔案,
            sheet_name名稱，不寫預設就是第一個sheet,
            header= 不寫預設會是1，會把第一列當作key值
            如果是0，則會把第一列當作數據，取值要用index，1、2、3)
        """
        df = pandas.read_excel('./test.xlsx', sheet_name='工作表1')
        data_list=[]
        # 顯示數據
        print(df)
        for row in df.itertuples():
            print(row)
            cur_data = ({
                'customer': row.客戶,
                'type': row.單位,
                'rate': row.比例
            })
            data_list.append(cur_data)
        print(data_list)
        return data_list
    except Exception as e:
        print("讀取 Excel 檔案時出現錯誤：", e)
        return ''

"""
記得要先裝 
pip install mysql-connector-python
pip install pandas openpyxl
"""
if __name__ == "__main__":
    my_data_list = read_excel()
    connect_to_mysql(my_data_list)
