'''
更新近一年招收人数
'''

import os
import pandas as pd
from to_db import MyDataBase



file_name = os.path.join(os.getcwd(), "common/tasks/enroll_num.xlsx")

db_info = {
        'host' : 'localhost',
        'port' : 3306,
        'user' : 'root',
        'password' : 'lijingwei',
        'database' : 'major_db',
    }

def read_data():
    data = pd.read_excel(file_name, sheet_name=0, usecols=[2, 3])

    print(data)
    return data


def to_db(data):
    with MyDataBase(
        host=db_info['host'],
        port=db_info['port'],
        user=db_info['user'],
        password=db_info['password'],
        database=db_info['database'],
    ) as cs:
        select_sql = "select id from major where m_name='{name}'"
        update_sql = "update major set enroll_num={num} where id={m_id}"

        for row in data.itertuples(index=False):
            cs.execute(select_sql.format(name=row[0]))
            m_id = cs.fetchone()
            # fetch到的都是个元组....
            if not m_id:
                print(row[0] + " is not in db...")
            else:
                if row[1] != -1:
                    print(int(row[1]))
                    cs.execute(update_sql.format(
                        num=int(row[1]),
                        m_id=m_id[0]
                    ))        
                    print(row[0] + " done")


if __name__ == "__main__":
    data = read_data()
    to_db(data)
    