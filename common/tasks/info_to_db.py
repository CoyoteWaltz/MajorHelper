
import os
import MySQLdb
import pandas as pd

# from . import to_db
from to_db import MyDataBase


file_name = os.path.join(os.getcwd(), 'docs/majors.xlsx')
n = 66
data = pd.read_excel(file_name, sheet_name=1, usecols=[
                     1, 2, 3], nrows=n)  # 'Sheet1')
# print(data.at[4, '专业'])       # at 行 列
# print(data.shape[0])

# print(type(next(data.iterrows())))  # dataframe有一个行迭代器 每一行作为元组返回
# print(next(data.iterrows()))

# i, d = next(data.iterrows())
# major_dict = {}
from majors2 import major_dict

majors = []
"""发现学院冲突"""
for row in data.itertuples(index=False, name='这个是每个row的名字'):  # 这个也更好，比iterrows快
    # 三元组依次是 学院 专业 大类
    # if row[2] not in major_dict.keys():
    #     major_dict[row[2]] = {}
    # if row[0] not in major_dict[row[2]].keys():
    #     major_dict[row[2]][row[0]] = []
    # college = major_dict[row[2]][row[0]]
    # if row[1] not in college:
    #     college.append(row[1])
    majors.append(row[1])

# print(major_dict)

db_info = {
        'host' : 'localhost',
        'port' : 3306,
        'user' : 'root',
        'password' : 'lijingwei',
        'database' : 'major_db',
    }

table = ['category', 'college']
select_sql = 'select {sth} from {table} {condition}'
insert_sql = 'insert into {table} values({values})'

category_id = {}
college_id = {}
# 在数据库中写入表
with MyDataBase(
        host=db_info['host'],
        port=db_info['port'],
        user=db_info['user'],
        password=db_info['password'],
        database=db_info['database'],
    ) as cs:

    count = 1
    for cate in major_dict.keys():
        # print(cate)
        cs.execute(select_sql.format(
            sth="id",
            table=table[0],
            condition="where c_name = '{}'".format(cate)
        ))
        # cs.execute('select * from %s where c_name = ' %(table[0],))
        c_id = cs.fetchone()
        category_id[cate] = c_id[0]

    # MySQLdb._exceptions.IntegrityError: (1062, "Duplicate entry '法学院' for key 'c_name'")

        # try:
        for col in major_dict[cate].keys():
            try:
                cs.execute(insert_sql.format(
                    table=table[1],
                    values="{id}, '{c_name}', {category_id}".format(
                        id=count,
                        c_name=col,
                        category_id=category_id[cate]
                    )
                ))
            except Exception:
                pass
            # cs.execute(select_sql.format(
            #     sth="id",
            #     table=table[1],
            #     condition="where c_name='%s'" %col
            # ))
            # col_id = cs.fetchone()
            college_id[col] = count  # col_id[0]
            count += 1

        # except MySQLdb.Error as e:
        #     if "Duplicate" in str(e):
        #         print('数据库中已经有学院了')
            

print(category_id)
print(college_id)
print(majors)
# print(len(majors))
with open(os.path.join(os.getcwd(), 'common/tasks/ids.py'), 'w') as f:
    f.write('category_id = %s\n'% str(category_id))
    f.write('college_id = %s\n' % str(college_id))
    f.write('majors = %s\n' % str(majors))
    

        
    # d = cs.fetchall()
    # print(d[0][0])



#  id          | int(11)     | NO   | PRI | NULL    | auto_increment |
# | c_name      | varchar(30) | NO   | UNI | NULL    |                |
# | category_id | int(11)     | N



# 专业(学院='材料科学与工程学院', 专业='电子科学与技术', 大类='理学工学类')

# print(i)
# print(d)

# for r in data.iterrows():
#     print(r)

# for c in data['大类']:
#     major_dict[c] = []

# for college in data['学院', '大类']:
#     print(college)

# print(major_dict)

# 将组成的字典写入文件
# with open('majors2.py', 'w') as f:
#     f.write(str(major_dict))
