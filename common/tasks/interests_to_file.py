# import csv
import os
import pandas as pd
from to_db import MyDataBase

from ids import majors

# 专业兴趣对应标签的文件名
file_name = os.path.join(os.getcwd(), 'common/tasks/major2interest.csv')

# 兴趣集合
interests_set = set()


def read_csv(file_name):
    # 读取csv文件
    data = pd.read_csv(file_name)
    return data

def to_set(data):
    # 数据保存到interest_set中
    for row in data.itertuples(index=False):

        # check 
        if row[0].strip() not in majors:
            print(row[0] + "is not in majors")
        interests_set.add(row[1].strip())



print(interests_set)
print("标签数：", len(interests_set))

interests = {}

def to_dict():
    # 写入字典interests
    n = 1
    for i in interests_set:

        interests[i] = n
        n += 1


print(interests)

def to_file():
    # append到ids.py
    with open(os.path.join(os.getcwd(), "common/tasks/ids.py"), 'a') as f:
        f.write('interests = %s' %str(interests))
        f.write('\n')




if __name__ == '__main__':
    # data = read_csv(file_name)
    # to_set(data)
    # to_dict()
    # to_file()
    pass