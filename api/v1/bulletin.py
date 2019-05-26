from flask import request

from common.libs.redprint import Redprint
from common.models.models import Article, Board
from common.libs.returns import *

api = Redprint('bulletin')


@api.route('/', methods=['GET', 'POST'])
def bulletin():

    return '发布'

@api.route('/article_list/<string:b_name>', methods=['GET', 'POST'])
def article_list(b_name):
    b_id = Board.query.filer_by(b_name=b_name).first()
    if not b_id:
        return failed_return("数据库中未找到")
    all_article  = Article.query.filter_by(board_id=b_id).all()
    a_list = []
    for at in all_article:
        a_list.append({
            "a_id" : at.id,
            "title" : at.title,
            "pub_time" : at.publish_time.strftime("%Y-%m-%d")
        })
    return success_return(a_list)



@api.route('/article/<int:a_id>', methods=['GET', 'POST'])
def article(a_id):
    article = Article.query.filter_by(id=a_id).first()
    if not article:
        return failed_return("数据库中未找到")
    return success_return(article.get_article_info())
