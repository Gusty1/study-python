"""
用 requests 爬取 Google 翻譯 API 翻譯文字
"""

import requests

text = input('輸入要翻譯的文字: ')
# text = 'dog'
url = f"https://translate.googleapis.com/translate_a/single"
params = {
    "client": "gtx",
    "sl": 'auto',
    "tl": 'zh-TW',
    "dt": "t",
    "q": text,
}

response = requests.get(url, params=params)
result = response.json()
# 翻譯結果在 [0][0][0]
translated_text = result[0][0][0]
print(translated_text)

response.close()
