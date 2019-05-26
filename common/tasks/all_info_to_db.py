import os

from to_db import MyDataBase


db_info = {
        'host' : 'localhost',
        'port' : 3306,
        'user' : 'root',
        'password' : 'lijingwei',
        'database' : 'major_db',
    }


def interest_to_db():
    # interests进mysql表：interest
    from ids import interests
    
    table = 'interest'
    sql = "insert into {table} values({id}, '{i_name}')"
    with MyDataBase(
        host=db_info['host'],
        port=db_info['port'],
        user=db_info['user'],
        password=db_info['password'],
        database=db_info['database'],
    ) as cs:
        # 兴趣写入数据库
        for name, v in interests.items():
            
            cs.execute(sql.format(
                table=table,
                id=v,
                i_name=name
            ))


def man_input_rank():
    # 手动键入百分比.....
    major_rank = {}
    from majors2 import major_dict

    for cat, col in major_dict.items():
        print(cat)
        for coll, majs in col.items():
            print(coll + "学院")
            for m in majs:
                rank = input(m+":").strip()
                if rank is '':
                    major_rank[m] = 'None'
                    print(m + "is None")
                else:
                    major_rank[m] = rank  # 数据库中是字符串类型

            print()
        print()

    print(major_rank)

    with open(os.path.join(os.getcwd(), "common/tasks/ids.py"), 'a') as f:
        f.write("major_rank = %s" % str(major_rank))
        f.write('\n')

# 测控技术与仪器 fix 81.31
# 机械设计及其自动化 fix ??

    # 大类{学院{专业}}
    # with open(os.path.join(os.getcwd(), "common/tasks/info.txt"), 'r') as f:
    #     for row in f:
    #         major = eval(row)
    #         # print(row)
    #         # m_name, brief, course
    #         print(major['m_name'])
    #         print(major['course'])
    #         k = input()

def majors_to_db():
# id           | int(11)       | NO   | PRI | NULL    | auto_increment |
# | m_name       | varchar(20)   | NO   | UNI | NULL    |                |
# | college_id   | int(11)       | NO   | MUL | NULL    |                |
# | category_id  | int(11)       | NO   | MUL | NULL    |                |
# | intro        | varchar(1000) | NO   |     |         |                |
# | course       | varchar(800)  | YES  |     | NULL    |                |
# | salary       | varchar(200)  | YES  |     | NULL    |                |
# | rank_precent
    from majors2 import major_dict

    '''
    ids.py 中 majors 是m_name的list，major_rank是rank_precent,
    college_id是字典  college_id[学院] == college_id
    category_id  category_id[大类] == category_id

    course和intro在info.txt中....
    '''
    from ids import major_rank, college_id, category_id
    
    major_info = {}
    # info文件信息整理
    with open(os.path.join(os.getcwd(), "common/tasks/info.txt"), 'r') as f:
        for row in f:
            major = eval(row)
            # print(row)
            # m_name, brief, course
            # print(major['m_name'])
            # print(major['course'])

            major_info[major['m_name']] = {
                "intro" : major['brief'],
                "course" : major['course']
            }

    # print(major_info)
    
    with MyDataBase(
        host=db_info['host'],
        port=db_info['port'],
        user=db_info['user'],
        password=db_info['password'],
        database=db_info['database'],
    ) as cs:
        table = 'major'
        sql = "insert into major values({m_id}, '{m_name}', {college_id}, {category_id}, '{intro}', '{course}', null, '{rank_precent}')"


        m_id = 1
        for cat, col in major_dict.items():
            # 大类中
            for coll, majs in col.items():
                # 学院里
                for m in majs:
                    cs.execute(sql.format(
                        m_id=m_id,
                        m_name=m,
                        college_id=college_id[coll],
                        category_id=category_id[cat],
                        intro=major_info[m]['intro'],
                        course=major_info[m]['course'],
                        rank_precent=major_rank[m]
                    ))
                    m_id += 1



def interest_rel_major_to_db():
    # 标签-专业关系表入库
    file_name = os.path.join(os.getcwd(), 'common/tasks/major2interest.csv')

    import pandas as pd
    data = pd.read_csv(file_name)
    with MyDataBase(
        host=db_info['host'],
        port=db_info['port'],
        user=db_info['user'],
        password=db_info['password'],
        database=db_info['database'],
    ) as cs:
        select_i_sql = 'select id from interest where i_name="{i_name}"'
        select_m_sql = 'select id from major where m_name="{m_name}"'
        insert_sql = 'insert into interest2major values({id}, ({i_id}), ({m_id}))'
        # 兴趣-专业
        for d in data.itertuples(index=True):
            # d[0]=name ,d[1]=tag
            try:
                print(d)
                cs.execute(insert_sql.format(
                    id=d[0] + 1,
                    i_id=select_i_sql.format(i_name=d[2].strip()),
                    m_id=select_m_sql.format(m_name=d[1].strip())
                ))
            except Exception as e:
                
                print(d[1], d[2], "失败")
                print(str(e))
            # m = cs.fetchone()
            # print(m)

def salary_to_db():
    file_name = os.path.join(os.getcwd(), 'common/tasks/salary.csv')
    import pandas as pd
    data = pd.read_csv(file_name)
    with MyDataBase(
        host=db_info['host'],
        port=db_info['port'],
        user=db_info['user'],
        password=db_info['password'],
        database=db_info['database'],
    ) as cs:
        select_sql = 'select id from major where m_name="{name}"'
        update_sql = 'update major set salary="{salary}" where id={m_id}'
        for row in data.itertuples(index=False):
            cs.execute(select_sql.format(
                name=row[0]
            ))
            m_id = cs.fetchone()
            if not m_id:
                print(row[0], " not in db")
            else:
                # print(m_id)
                cs.execute(update_sql.format(
                    salary=row[1],
                    m_id=m_id[0]
                ))
            # print(row[0], row[1])

    

if __name__ == '__main__':
    # interest_to_db()
    # man_input_rank()
    # majors_to_db()
    # interest_rel_major_to_db()
    salary_to_db()