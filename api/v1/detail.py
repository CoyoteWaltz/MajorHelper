from flask import request
from common.libs.redprint import Redprint
from application import db

from common.models.models import Major
from common.libs.returns import *

api = Redprint('/detail')


@api.route('/<int:m_id>', methods=['GET', 'POST'])  # 如果不用指定的方法会405直接错误
def detail(m_id):
    # 返回查询到的专业的信息
    # if m_id < 1000:
    #     c_number = '0' * (4 - len(str(m_id))) + str(m_id)
    #     try:
    #         c = Clas(number=c_number, size=50)
    #         db.session.add(c)
    #         db.session.commit()
    #     except Exception:
    #         db.session.rollback()
    # else:
    #     t_name = 'flask%d' %(m_id % 100)
    #     try:
    #         t = Teacher(name=t_name)
    #         db.session.add(t)
    #         db.session.commit()
    #     except Exception:
    #         db.session.rollback()

    # t = Teacher.query.all()
    # s = [i.name for i in t]
    if request.method == 'GET':
        major = Major.query.filter_by(id=m_id).first()

        if major is None:
            return failed_return("not in database")
        
        m_info = {
            "m_name" : major.m_name,
            "intro" : major.intro,
            "course" : major.course,
            "salary" : major.salary,
            "rank_precent" : major.rank_precent
        }
        return success_return(m_info)
    

    # return request_disallow_return('GET')


# @api.route('/add_chief', methods=['GET', 'POST'])
# def add_chief():
#     # 用GET的方式发起请求，参数为c_id , t_id
#     # if request.method == 'GET':
#     #     # c_id = request.get_json()
#     #     ids = request.args  # 获得以params转过来的参数，等价于在url之后加?c_id= & t_id=
#     #     print(ids['c_id'])
#     #     c_id = ids['c_id']
#     #     print(ids['t_id'])
#     #     t_id = ids['t_id']

#     #     # c = Clas.query.filter_by(id=c_id).first()
#     #     # # t = Teacher.query.filter_by(id=t_id).first()
#     #     # c = Clas.query.get(c_id)#id=c_id)
#     #     # t = Teacher.query.get(t_id)#id=t_id)
#     #     # 错误检查
#     #     if c is None:
#     #         return 'No such a class'
#     #     if c.chief_id is not None:
#     #         return 'Already has a chief'

#     #     if t is None:
#     #         return 'No such a teacher'
#     #     if t.class_id is not None:
#     #         return 'Already has a class'
#     #     t.class_id = c_id
#     #     c.chief_id = t_id
#     #     db.session.commit()
#     #     # 建立班主任关系
#         return None
