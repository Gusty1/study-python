# 導入urllib

from urllib.request import urlopen

url = 'https://www.google.com.tw/'

# 開啟網址
response = urlopen(url)

# 返回的是byte編碼，要依據網頁編碼解碼才能得到網頁內容
# 某些網站，特別是 Google，返回的內容可能不是 UTF-8 編碼的，所以要手動取得編碼
# 獲取內容的編碼，默認為 utf-8
encoding = response.info().get_content_charset() or 'utf-8'
# big5
# print(encoding)

# 取得網頁內容
print(response.read().decode('big5'))
