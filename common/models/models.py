# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy

from application import db


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True) #, nullable=False, default=1)
    c_name = db.Column(db.String(20), nullable=False, unique=True)


class College(db.Model):
    __tablename__ = 'college'

    id = db.Column(db.Integer, primary_key=True) #, nullable=False, default=1)
    c_name = db.Column(db.String(30), nullable=False, unique=True)
    category_id = db.Column(db.ForeignKey('category.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    category = db.relationship('Category', primaryjoin='College.category_id == Category.id', backref='colleges')


class CtyMjRk(db.Model):
    __tablename__ = 'cty_mj_rk'

    id = db.Column(db.Integer, primary_key=True) #, nullable=False, default=1)
    cty_id = db.Column(db.ForeignKey('category.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    mj_id = db.Column(db.ForeignKey('major.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    first_precent = db.Column(db.Float)
    second_precent = db.Column(db.Float)
    third_precent = db.Column(db.Float)

    cty = db.relationship('Category', primaryjoin='CtyMjRk.cty_id == Category.id', backref='cty_mj_rks')
    mj = db.relationship('Major', primaryjoin='CtyMjRk.mj_id == Major.id', backref='cty_mj_rks')


    def get_major_rank_dict(self):

        return {
            "m_name" : self.mj.m_name,
            "f_rank" : self.first_precent,
            "s_rank" : self.second_precent,
            "t_rank" : self.third_precent
        }



class Interest(db.Model):
    __tablename__ = 'interest'

    id = db.Column(db.Integer, primary_key=True) #, nullable=False, default=1)
    i_name = db.Column(db.String(20), nullable=False, unique=True)


class Interest2major(db.Model):
    __tablename__ = 'interest2major'

    id = db.Column(db.Integer, primary_key=True) #, nullable=False, default=1)
    interest_id = db.Column(db.ForeignKey('interest.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    major_id = db.Column(db.ForeignKey('major.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    interest = db.relationship('Interest', primaryjoin='Interest2major.interest_id == Interest.id', backref='interest2majors')
    major = db.relationship('Major', primaryjoin='Interest2major.major_id == Major.id', backref='interest2majors')


class Major(db.Model):
    __tablename__ = 'major'

    id = db.Column(db.Integer, primary_key=True) #, nullable=False, default=1)
    m_name = db.Column(db.String(20), nullable=False, unique=True)
    college_id = db.Column(db.ForeignKey('college.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    category_id = db.Column(db.ForeignKey('category.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    intro = db.Column(db.String(1000))#, server_default=db.FetchedValue())
    course = db.Column(db.String(800))
    salary = db.Column(db.String(200))
    rank_precent = db.Column(db.String(50))
    enroll_num = db.Column(db.Integer)      # 招收人数

    category = db.relationship('Category', primaryjoin='Major.category_id == Category.id', backref='majors')
    college = db.relationship('College', primaryjoin='Major.college_id == College.id', backref='majors')


    

    def get_dict_info(self):

        return {
            "m_name" : self.m_name,
            "intro" : self.intro,
            "course" : self.course,
            "salary" : self.salary,
            "rank_precent" : self.rank_precent,
            "enroll_num" : self.enroll_num
        }
        

class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    publish_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    content = db.Column(db.Text)
    author = db.Column(db.String(30))
    board_id = db.Column(db.ForeignKey('board.id'), index=True)
    img_link = db.Column(db.String(1000))
    file_link = db.Column(db.String(1000))

    board = db.relationship('Board', primaryjoin='Article.board_id == Board.id', backref='articles')

    def get_article_info(self):
        # 获取格式化信息
        separate_links = []
        separate_links.append
        return {
            "title" : self.title,
            "pub_time" : self.publish_time.strftime("%Y-%m-%d"),
            "author" : self.author,
            "img_link" : self.img_link if self.img_link is None else self.img_link.split(","),
            "file_link" : self.file_link if self.file_link is None else self.file_link.split(","),
            "content" : self.content
        }

# 专业辅修 转专业 学院活动 海外实习
class Board(db.Model):
    __tablename__ = 'board'

    id = db.Column(db.Integer, primary_key=True)
    b_name = db.Column(db.String(80), nullable=False, unique=True)
    publish_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    intro = db.Column(db.String(200))

    
