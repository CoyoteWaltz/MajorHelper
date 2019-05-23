
from flask import request

from common.libs.redprint import Redprint
'''import models里面的东西进行数据库操作'''

from common.models.models import Interest, Major, Interest2major
from common.libs.returns import *

import random

api = Redprint('locate')


@api.route('/', methods=['GET'])
def locate():
    # 返回所有的兴趣标签
    try:
        interests = Interest.query.all()
        if not interests:
            return db_not_found()
            
        i_info = []
        for i in interests:
            i_info.append({
                "i_id" : i.id, "i_content" : i.i_name
            })

        return success_return({
            'interests' : i_info
        })

        return failed_return("数据库中无内容")

    except Exception as e:
        return db_failed_return()


@api.route('/search/', methods=['GET', 'POST'])
def search():
    # 接受前端三个标签id，返回相关专业的信息 m_id, m_name
    if request.method == 'GET':
        # f_id = request.values.get('f_id')
        # s_id = request.values.get('s_id')
        # t_id = request.values.get('t_id')
        # print(request.headers)
        id_list = eval(str(request.values.get('tags')))
        # id_list = eval(str(request.values.get('tags')).decode('utf8'))
        # d = request.values.get('tags')
        # print(d)
        # id_list = random.sample(range(1, 26), 3)
        # print("id_list", id_list)
        # print(type(f_id))
        # id_list = []
        # if f_id is not None:
        #     id_list.append(f_id)            
        # if s_id is not None:
        #     id_list.append(s_id)            
        # if t_id is not None:
        #     id_list.append(t_id)            

        major = []
        # 专业集合的list
        major_sets = []
        for i in id_list:
            # print("id==>>", i)
            major_set = set()
            # 获取这个id对应的关系
            in_m = Interest2major.query.filter_by(interest_id=i).all()
            # print("in_m", in_m)
            # 放进集合中

            for fim in in_m:
                # print("add=>>", fim.major.m_name)
                major_set.add((fim.major.id, fim.major.m_name))
            # print(222, major_set)
            if major_set:
                major_sets.append(major_set)
            # print("append===>", i)
        # print("for循环结束")
        # print("major_sets+++>>>", major_sets)
        # print("len--->", len(major_sets))
        # 处理集合的list
        intersection = major_sets[0].copy()     # 这里一定要copy不然会被覆盖，或者换一个方法
        for m_set in major_sets[1:]:
            intersection &= m_set
        # 处理交集
        # print("交集====", intersection)
        if not intersection:
            # 交集为空,集合列表按长度大小排序

            sorted_set = sorted(major_sets, key=lambda x:len(x), reverse=True)
            # print("sorted===>>", sorted_set)
            # print("len===>", len(sorted_set))
            # 按照长度降序
            if not sorted_set:
                # 什么都没搜到
                return failed_return("数据库中未找到")

            set_len = len(sorted_set)
            for i in range(5):
                # print(1111)
                rand_m = random.choice(list(sorted_set[i % set_len]))
                # print(rand_m)
                # if list(sorted_set[i % set_len]):
                #     rand_m = list(sorted_set[i % set_len])
                # else:
                #     return failed_return("dsfsdf")
                m_dict = {"m_id" : rand_m[0], "m_name" : rand_m[1]}
                if m_dict not in major:
                    major.append(m_dict)

            return success_return(major)

        # 纠结选择专业返回 上限5个
        if len(intersection) >= 5:
            major = random.sample(intersection, 5)
        elif len(intersection) >= 3:
            major = list(intersection)
        else:
            # 不足3个就随机抽取两个差集中的 从major_sets中随机抽一个集合
            # 然后和intersection做差集，从差集中随机选一个
            m_id = -1
            for _ in range(2):

                sub_set = random.choice(major_sets) - intersection
                if sub_set:
                #可能出现差集为空的情况
                    rand_m = random.choice(list(sub_set))
                    if m_id != rand_m[0]:
                        major.append(rand_m)
                        m_id = rand_m[0]

        return success_return(major)


    if request.method == 'POST':
        # 通过 get_json() 接受字典
        # data = request.get_json()
        data = request.form.get('content')
        if not data:
            return failed_return("未接收到数据")
        
        # 先实现简单的数据库模糊查找吧，以后再考虑结合分词之后的关键字搜索

        major_set = set()
        if len(data) <= 6:
            # 搜索内容长度小于5就用名字包含关键字     %关键字% 包含关键字
            major_like = Major.query.filter(Major.m_name.like("%%%s%%"%data)).all()
            for m in major_like:
                major_set.add((m.id, m.m_name))
        else:
            ms = Major.query.all()
            for m in ms:
                if m.m_name in data:
                    major_set.add((m.id, m.m_name))
        
        interests = Interest2major.query.all()
        for i in interests:
            if str(i.interest.i_name) in data:
                major_set.add((i.major.id, i.major.m_name))
        
        if not major_set:
            return failed_return("未能匹配")
        major_list = []
        for m_id, m_name in major_set:
            major_list.append({
                "m_id" : m_id,
                "m_name" : m_name
            })

        return success_return(major_list)
