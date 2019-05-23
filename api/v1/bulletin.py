from flask import request

from common.libs.redprint import Redprint

from common.libs.returns import *

api = Redprint('bulletin')


@api.route('/', methods=['GET', 'POST'])
def bulletin():

    return '发布'

@api.route('/article_list/<int:b_id>', methods=['GET', 'POST'])
def article_list(b_id):

    return b_id



@api.route('/article/<int:a_id>', methods=['GET', 'POST'])
def article_list(a_id):

    return a_id