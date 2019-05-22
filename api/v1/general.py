
from werkzeug.exceptions import HTTPException  # 这里面各种异常定义了
from common.libs.redprint import Redprint
from common.libs.returns import *

from common.models.models import Major, Category, College, CtyMjRk

import re

api = Redprint('general')

'''
{
    "category" : cat_list,
}

cat_list = [
    {
        "cat_name" : cat_name,
        "cat_id" : cat_id,
        "colleges" : college_list
    },

]

college_list = [
    {
        "col_name" : col_name,
        "majors" : major_list
    }
]

major_list = [
    {
        "m_id" : m_id,
        "m_name" : m_name
    }
]
'''

@api.route('/', methods=['GET'])
def general():
    # 大类{学院{专业}}
    try:
        data = {}
        count = 0
        categories = Category.query.all()  # 一定要all()了才回返回一个list之类可迭代的东西
        # 才能这样判断是否为空
        if not categories:
            return db_not_found()

        cat_list = []
        for cat in categories:
            colleges = College.query.filter_by(category_id=cat.id)

            college_list = []
            for col in colleges:
                # print(col.c_name)
                majors = Major.query.filter_by(college_id=col.id)

                major_list = []             #获得专业list
                for m in majors:
                    major_list.append({
                        "m_id" : m.id,
                        "m_name" : m.m_name
                    })
                
                college_list.append({
                    "col_name" : re.sub('\(.*?\)', '', col.c_name),
                    "majors" : major_list
                })
            cat_list.append({
                "cat_name" : cat.c_name[0] + cat.c_name[2] if cat.id != 1 else cat.c_name[0] + cat.c_name[1],
                "cat_id" : cat.id,
                "colleges" : college_list
            })
        data["category"] = cat_list

        return success_return(data)

    except Exception as e:
        return db_failed_return()




@api.route('/rank/<int:cat_id>', methods=['GET'])
def rank(cat_id):
    # 专业近三年分流排位
    try:
        cty_mj_rk = CtyMjRk.query.filter_by(cty_id=cat_id).all()
        if not cty_mj_rk:
            return db_not_found()
            
        data = []
        for cmr in cty_mj_rk:
            data.append(cmr.get_major_rank_dict())

        return success_return(data)

    except Exception as e:
        # print(e)
        return db_failed_return()

