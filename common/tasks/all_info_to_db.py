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







if __name__ == '__main__':
    # interest_to_db()
    # man_input_rank()
    majors_to_db()