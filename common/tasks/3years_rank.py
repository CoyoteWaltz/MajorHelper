import os
import pandas as pd

from to_db import MyDataBase


file_name = os.path.join(os.getcwd(), "common/tasks/3years_rank.xlsx")

data = pd.read_excel(file_name, sheet_name=0, usecols=list(range(1, 8)))

db_info = {
        'host' : 'localhost',
        'port' : 3306,
        'user' : 'root',
        'password' : 'lijingwei',
        'database' : 'major_db',
    }

with MyDataBase(
        host=db_info['host'],
        port=db_info['port'],
        user=db_info['user'],
        password=db_info['password'],
        database=db_info['database'],
    ) as cs:
        for row in data.itertuples(index=False):
            m_name = row[0].strip().strip("*").replace("（", "(").replace("）", ")").replace('\n', '')
            # print(m_name)
            cs.execute("select id, category_id from major where m_name = '%s'" %m_name)
            major = cs.fetchone()
            if major is None:
                print(m_name + " is wrong")
            else:
                cs.execute("insert into cty_mj_rk values(null, {cty_id}, {mj_id}, {fp}, {sp}, {tp})".format(
                    cty_id=major[1],
                    mj_id=major[0],
                    fp=str(row[1] * 100) if type(row[1]) is float else 'null',
                    sp=str(row[2] * 100) if type(row[2]) is float else 'null',
                    tp=str(row[3] * 100) if type(row[3]) is float else 'null'
                ))

                # print(major[0], major[1], type(row[1]), type(row[2]), row[3])




# | id             | int(11) | NO   | PRI | NULL    | auto_increment |
# | cty_id         | int(11) | NO   | MUL | NULL    |                |
# | mj_id          | int(11) | NO   | MUL | NULL    |                |
# | first_precent  | float   | YES  |     | NULL    |                |
# | second_precent | float   | YES  |     | NULL    |                |
# | third_precent  