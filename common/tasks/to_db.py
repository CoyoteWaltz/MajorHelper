import MySQLdb



class MyDataBase():
    # 封装一个数据库类，可以实现用with来操作
    def __init__(self, host, port, user, password, database, charset='utf8'):
        self._conn = MySQLdb.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset=charset
        )
        self.cs = self._conn.cursor()
    def __enter__(self):
        # 上下文属性
        # print('进入上下文')
        # with 上下文as的对象就是这里返回的值
        return self.cs
    
    def __exit__(self, exc_t, exc_v, traceback):
        # print('exc_t:', exc_t)  None
        # print('exc_v:', exc_v)
        # print('traceback:', traceback)
        # print('结束上下文')
        self._conn.commit()
        self.cs.close()
        self._conn.close()


# db = MySQLdb.connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     password='lijingwei',
#     database='testsss',
#     charset='utf8'
#     )



# sql = [
#     'SELECT * FROM class',
#     'INSERT INTO class values(null, {})'
#     ]

# with MyDataBase('localhost', 3306, 'root', 'lijingwei', 'testsss') as cs:
#     cla = ['1022', '1023', '1222']
#     for c in cla:
#         cs.execute(sql[1].format(c))
#     cs.execute(sql[0])
#     cont = cs.fetchall()
#     print(cont)
