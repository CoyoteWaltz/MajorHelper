'''
发布文章的接口

先写python命令行版本的，以后转为web的
'''

from to_db import MyDataBase


db_info = {
        'host' : 'localhost',
        'port' : 3306,
        'user' : 'root',
        'password' : 'lijingwei',
        'database' : 'major_db',
    }

def save_to_db(info):
    for key, val in info.items():
            print(key, val)
    
    with MyDataBase(
        host=db_info['host'],
        port=db_info['port'],
        user=db_info['user'],
        password=db_info['password'],
        database=db_info['database'],
    ) as cs:
        insert_sql = "insert into article values(null, '{title}',\
             null, '{content}', '{author}', {b_id}, {i_link}, {f_link}"
        select_b_sql = "select id from board where b_name='{b_name}'"
        cs.execute(select_b_sql.format(b_name=info['a_board']))
        b_id = cs.fetchone()
        if b_id is None:
            print("板块无效")
            return
        else:
            print(b_id)
        cs.execute(insert_sql.format(
            title=info['a_title'],
            content=info['a_content'],
            author=info['a_author'],
            b_id=b_id[0],
            i_link="'%s'"%info['img_name'] if info['img_name'] != '' else 'null',
            f_link="'%s'"%info['file_name'] if info['file_name'] != '' else 'null'
        ))
        
    print("成功存入数据库")
    

def main():
    print("hello, 按提示输入文章内容")
    a_info = {}
    count = 0
    while (True):
        count += 1
        print("第%d篇"%count)
        a_info["a_title"] = input("文章标题\n>>>").strip()
        a_info["a_board"] = input("文章板块\n>>>").strip()
        a_info["a_author"] = input("文章作者\n>>>").strip()
        a_info["a_content"] = input("文章内容\n>>>").strip()
        # a_info["img_name"] = input("图片名(用英文逗号分隔)").split(',')
        a_info["img_name"] = input("图片名(用英文逗号分隔)")
        # a_info["file_name"] = input("文件名(用英文逗号分隔)").split(',')
        a_info["file_name"] = input("文件名(用英文逗号分隔)")
        
        submit = input("以上，确认吗？(y/n)").strip()
        if submit.lower() == 'y':
            save_to_db(a_info)

            submit = input("还要继续吗?(y/n)").strip()
            if submit.lower() == 'n':
                break
        else:
            print("重来")
            count -= 1

        
    print("完成了%d篇文章 bye~"%count)

if __name__ == "__main__":
    main()