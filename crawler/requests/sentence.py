import requests
from bs4 import BeautifulSoup
import json

def get_sentence():
    # url = 'https://www.chinesewords.org/wisdom/show-317.html'
    # url = 'https://www.chinesewords.org/wisdom/show-11535.html'
    url = 'https://www.chinesewords.org/wisdom/show-11498.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    sentence = soup.find('div', id='txt').text
    sentence_ary = sentence.split('\n')
    sentence_list = []
    for i in sentence_ary:
        if i.strip() and i.find('、') != -1 and i.find('——') != -1:
            i = i.strip()
            sentence_start = i.find('、')
            sentence_end = i.find('——')
            sentence = i[sentence_start + 1:sentence_end]
            name_start = i.find('——')
            name = i[name_start + 2:]
            sentence_list.append({
                "sentence":sentence,
                "name":name,
            })
    return sentence_list

def write_sentence_to_json(sentence_list):
    try:
        with open('sentence.json', "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except Exception as e:
        existing_data = []
    with open('sentence.json', 'w', encoding='utf-8') as f:
        existing_data.extend(sentence_list)
        json.dump(existing_data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    print('獲取句子開始')
    get_sentence_list = get_sentence()
    print(f'獲取句子結束，共獲得{len(get_sentence_list)}筆資料')
    print('開始寫入json檔案')
    write_sentence_to_json(get_sentence_list)
    print('寫入json檔案完成')