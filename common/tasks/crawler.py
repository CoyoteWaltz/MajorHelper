import lxml
import re
import requests
from bs4 import BeautifulSoup

'''
爬学院名称，专业名称，专业简介，主要课程，
'''

url = 'http://zyinfo.shu.edu.cn'
after_login = '/Default3.aspx'
form_data = {
    '__VIEWSTATE': '/wEPDwUKMTI1NjE2MTI5OQ9kFgICAQ9kFgICBQ8PFgIeBFRleHQFG+eUqOaIt+WQjeaIluWvhueggemUmeivr++8gWRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBQhidG5Mb2dpbjIhaHB/ryTAnNpbHkJ+HL/His6dLe2bGIGh3b1ChaqT',
    '__VIEWSTATEGENERATOR': 'C2EE9ABB',
    '__EVENTVALIDATION': '/wEWBALNobaICgLEhISFCwKd+7qdDgKC3IeGDCvGV1oIt1JoK9ApEKdL8EqhLqjZn+dafv2yhz0GAfS7',
    'txtName': '17122336',
    'txtPwd': 'Ljw9898',
    'btnLogin.x': '36',
    'btnLogin.y': '19'
}


def college_name():
    # 爬取学院名，登录之后访问默认页从html直接可以获得



