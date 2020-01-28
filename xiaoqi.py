import requests
from bs4 import BeautifulSoup
import re

url = "https://baike.baidu.com/item/"
str = "我爱我家控股集团股份有限公司"


def get_html(url, str):
    a = url + str
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'}
    html = requests.get(a, headers=headers, verify=False)
    if html.status_code == 200:
        html.encoding = 'utf-8'
        return html.text
    return None


def get_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_jianjie(soup):
    title = soup.find('div', class_='lemma-summary')
    text = title.find('div', attrs = {'class':'para'}).get_text()
    return text


def get_shuxing(soup):
    content = soup.find('div', class_='basic-info cmn-clearfix')
    left = content.find('dl', attrs = {'class':'basicInfo-block basicInfo-left'}).get_text()
    right = content.find('dl', class_='basicInfo-block basicInfo-right').get_text()
    return left + right


def qiepian(str):
    list = str.strip().split('\n')
    for i in list:
        if i == '':
            list.remove(i)
        if "\xa0" in i:
            list.remove(i)
        if i == '':
            list.remove(i)
    return list


def func1(str1, str2):
    d = {'predicate': str1, 'object': str2}
    return d


def func2(dict):
    l = [dict]
    return l


def main():
    html = get_html(url, str)
    soup = get_soup(html)
    text = get_jianjie(soup)
    shuxing = get_shuxing(soup)

    print(text)
    print(shuxing)
    print(qiepian(shuxing))


if __name__ == '__main__':
    main()
    '''
    d = func1('摘要', '随着时间的推移，陈翔、齐秦、吴宗宪、蔡琴、青鸟飞鱼等歌手都曾翻唱过。')
    l = func2(d)
    print(l)
    '''
    '''
    tuplex = ((2, "w"), (3, "r"))
    print(dict((y, x) for x, y in tuplex))
    '''
