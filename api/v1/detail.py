from flask import request
from common.libs.redprint import Redprint
from application import db

from common.models.models import Major
from common.libs.returns import *

api = Redprint('/detail')


@api.route('/<int:m_id>', methods=['GET'])  # 如果不用指定的方法会405直接错误
def detail(m_id):
    # 返回查询到的专业的信息
# if request.method == 'GET':
    try:
        major = Major.query.filter_by(id=m_id).first()

        if major is None:
            return db_not_found()
        
        return success_return(major.get_dict_info())
    except Exception as e:

        return db_failed_return()

    # return request_disallow_return('GET')
