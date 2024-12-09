"""
用requests模組爬取Google搜尋台積電結果
"""


import requests

#https://www.google.com/search?q=%E5%8F%B0%E7%A9%8D%E9%9B%BB

url = 'https://www.google.com/search?q=%E5%8F%B0%E7%A9%8D%E9%9B%BB'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
response = requests.get(url, headers=headers)

print(response)

# 取得源代碼
print(response.text)

response.close()