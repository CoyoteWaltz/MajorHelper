# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy

from application import db


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(20), nullable=False, unique=True)


class College(db.Model):
    __tablename__ = 'college'

    id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(30), nullable=False, unique=True)
    category_id = db.Column(db.ForeignKey('category.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    category = db.relationship('Category', primaryjoin='College.category_id == Category.id', backref='colleges')


class CtyMjRk(db.Model):
    __tablename__ = 'cty_mj_rk'

    id = db.Column(db.Integer, primary_key=True)
    cty_id = db.Column(db.ForeignKey('category.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    mj_id = db.Column(db.ForeignKey('major.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    first_precent = db.Column(db.Float)
    second_precent = db.Column(db.Float)
    third_precent = db.Column(db.Float)

    cty = db.relationship('Category', primaryjoin='CtyMjRk.cty_id == Category.id', backref='cty_mj_rks')
    mj = db.relationship('Major', primaryjoin='CtyMjRk.mj_id == Major.id', backref='cty_mj_rks')


class Interest(db.Model):
    __tablename__ = 'interest'

    id = db.Column(db.Integer, primary_key=True)
    i_name = db.Column(db.String(20), nullable=False, unique=True)


class Interest2major(db.Model):
    __tablename__ = 'interest2major'

    id = db.Column(db.Integer, primary_key=True)
    interest_id = db.Column(db.ForeignKey('interest.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    major_id = db.Column(db.ForeignKey('major.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    interest = db.relationship('Interest', primaryjoin='Interest2major.interest_id == Interest.id', backref='interest2majors')
    major = db.relationship('Major', primaryjoin='Interest2major.major_id == Major.id', backref='interest2majors')


class Major(db.Model):
    __tablename__ = 'major'

    id = db.Column(db.Integer, primary_key=True)
    m_name = db.Column(db.String(20), nullable=False, unique=True)
    college_id = db.Column(db.ForeignKey('college.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    category_id = db.Column(db.ForeignKey('category.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    intro = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue())
    course = db.Column(db.String(800))
    salary = db.Column(db.String(200))
    rank_precent = db.Column(db.String(50))

    category = db.relationship('Category', primaryjoin='Major.category_id == Category.id', backref='majors')
    college = db.relationship('College', primaryjoin='Major.college_id == College.id', backref='majors')
