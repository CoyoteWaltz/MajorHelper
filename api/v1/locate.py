
from flask import request, jsonify

from common.libs.redprint import Redprint
'''import models里面的东西进行数据库操作'''

from common.models.models import Interest, Major
from common.libs.returns import *

api = Redprint('locate')


@api.route('/', methods=['GET'])
def locate():
    # 返回所有的兴趣标签
    interests = Interest.query.all()
    i_info = []
    for i in interests:
        i_info.append({
            "i_id" : i.id, "i_content" : i.i_name
        })
    return success_return({
        'interests' : i_info
    })




@api.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        # get 方法的请求会传递三个参数 id1,id2,id3，如果前端是用body里面传raw json可以用
        # request.json或者request.get_json()，好像前者只能接受POST?
        # 用参数传的话用args.get
        d = request.get_json()
        print(type(d))
        return 'get'


    if request.method == 'POST':
        
        return '返回查找结果'

    return '返回搜索结果'