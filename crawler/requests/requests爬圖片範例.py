"""
BS4+圖片下載練習
"""

import requests
from bs4 import BeautifulSoup
import os
import time


def get_img_list():
    url = 'https://www.wallpaperflare.com/'
    # 這個網站沒有任何限制，只是我想記錄一下
    headers = {
        # 有些會限制user-agent要是瀏覽器的才會允許
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        # 有些圖片會有防盜練限制，要加上referer才行
        'Referer': 'https://www.pixiv.net/'
    }
    resp = requests.get(url, headers=headers)
    html_text = resp.text
    resp.close()
    bs4 = BeautifulSoup(html_text, 'html.parser')

    pic_li_list = bs4.findAll('li', class_='item shadow')
    img_list = []
    for picItem in pic_li_list:
        if picItem.find('figure'):
            img_url = picItem.find('a', itemprop='url').find('img').get('data-src')
            filename_with_extension = os.path.basename(img_url)
            img_list.append({
                'name': filename_with_extension,
                'url': img_url,
            })
    print(f'共取得{img_list.count}張圖片')

    return img_list


def write_pic(img_list):
    # 用enumerate可以取得index
    for index, value in enumerate(img_list):
         # 圖片太多了，10張就好
        if index > 10:
            print('下載結束')
            break

        print(f'第{index + 1}張圖片 下載中...')
        with open('./test_pic/' + value['name'], 'wb') as f:
            resp = requests.get(value['url'])
            f.write(resp.content)
            resp.close()
        print(f'第{index + 1}張圖片 下載完成')
        # 怕一直發請求會被鎖，停個1秒
        time.sleep(1)

if __name__ == '__main__':
    write_pic(get_img_list())
