import os
import re
import time
# 将中文转码为url编码 urllib.parse.quote

import lxml
from urllib.request import urlopen
from urllib.parse import quote, urlencode

import requests     # ??
from bs4 import BeautifulSoup

from ids import majors
'''
爬专业简介，主要课程，
from 百度百科
'''
url = "https://baike.baidu.com/item/"

cookie = {
    "Cookie" : "BAIDUID=A3FC6077BEE92CF7B9795A60304E0A59:FG=1; BIDUPSID=A3FC6077BEE92CF7B9795A60304E0A59; PSTM=1545920931; BDUSS=JIYnZ3WVBzWHp2VDk1UlVhVThFT0k4S2lLSEZVdzJXQS1uZVBLYjMyUE1ia3hjQVFBQUFBJCQAAAAAAAAAAAEAAADL8uJPQWxiYWxvbmXYvAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMzhJFzM4SRcY1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1557494707,1557494761,1557501025,1557501062; delPer=0; PSINO=1; H_PS_PSSID=26523_1425_28777_21125_28518_28722_28964_28838_28585_22157; pgv_pvi=2590939136; pgv_si=s2680053760; BK_SEARCHLOG=%7B%22key%22%3A%5B%22%E6%B1%89%E8%AF%AD%E5%9B%BD%E9%99%85%E6%95%99%E8%82%B2%E4%B8%93%E4%B8%9A%22%2C%22%E6%B1%89%E8%AF%AD%E5%9B%BD%E9%99%85%E6%95%99%E8%82%B2%22%2C%22%E6%99%BA%E8%83%BD%E6%9C%BA%E5%99%A8%E4%BA%BA%22%5D%7D; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1557568948"
}
cookie = bytes(urlencode(cookie), encoding='utf8')

file_name = os.path.join(os.getcwd(), "common/tasks/info.txt")
# # <div class="lemma-summary" label-module="lemmaSummary">

def strip_char(string):
    s = re.sub('\[[0-9]\]', '', string)      # 将文段里的[0],[1]都去掉
    return re.sub('[\n\xa0]', '', s)      # 将文段里的换行都去掉

def open_url_get_info(major):
    '''
    打开每个专业的百科详细页，返回简介，课程信息（字符串处理）
    '''
    info = {'m_name' : major}
    #处理放在item后面的url字符
    major = major.split('(')[0].rstrip('专业')
    item = quote(major + '专业')
    html = urlopen(url + item, cookie).read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('h1').get_text()
    if "百度百科错误页" in h1:
        print("%s error page" %major)
        return
    elif major not in h1:
        print("wrong page %s"%h1)
        return
    
    brief = soup.find('div', {"class" : "lemma-summary"}).get_text().strip('\n')
    
    brief = strip_char(brief)
    info['brief'] = brief
    print(major)
    # print(brief)
    # print()

    # class="para-title level-2" 是个大的div
    all_div = soup.find_all('div')
    title_div = soup.find_all('div', {"class" : "para-title level-2"})
    start = -1
    c_info = ''
    for c in title_div:
        # 主干课程，主要课程
        if "主干课程" in c.get_text() or "主要课程" in c.get_text() or  "课程设置" in c.get_text():
            start = all_div.index(c)
            course_div = c
            # print(c)
    # print(start)
    if start > 0:
        # end = title_div[title_div.index(all_div[start]) + 1] 
        next_title = title_div[title_div.index(course_div) + 1]
        end = all_div.index(next_title)
        # print(end)
        # for d in all_div[start + 1 : end - 1]:
        #     print(d.get_text())
        c_info = ''.join([d.get_text() for d in  all_div[start + 1 : end - 1]])
        # print(all_div[start + 1 : end - 1])
    


    info['course'] = strip_char(c_info)
    print(info)


    return info

def to_file(filename):
    for m in majors:
        info = open_url_get_info(m)
        with open(file_name, 'a') as f:
            f.write(str(info))
            f.write('\n')
        time.sleep(.7)

def main():
    to_file(file_name)

def test():
    # for m in majors[-5:]:
#     print(m, end=' ')
#     item = quote(m.split("(")[0]+'专业') if not m.endswith('专业') else quote(m.split("(")[0])
#     html = urlopen(url + item, data=data).read().decode("utf-8")
#     soup = BeautifulSoup(html, 'lxml')
#     h1 = soup.find('h1').get_text()
#     if "百度百科错误页" in h1:
#         print('ops..')
#     elif m in h1:
#         print('ok')
#     else:
#         print(h1)
#     time.sleep(.7)
    pass

if __name__ == '__main__':
    main()
    # test()





# print(soup)