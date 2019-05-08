# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

from application import db

'''
数据库的增删改查
'''

class Clas(db.Model):
    __tablename__ = 'class'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(10), nullable=False, unique=True)
    size = db.Column(db.Integer, server_default=db.FetchedValue())
    chief_id = db.Column(db.ForeignKey('teacher.id'), index=True)

    chief = db.relationship('Teacher', primaryjoin='Clas.chief_id == Teacher.id', backref='class')
    def __str__(self):
        return 'class no.{} size:{} chief:{}'.format(self.number, self.size, self.chief_id)

class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    class_id = db.Column(db.ForeignKey('class.id'), index=True)
    
    nick_name = db.Column(db.String(20), unique=True)

    _class = db.relationship('Clas', primaryjoin='Student.class_id == Clas.id', backref='students')


class Teacher(db.Model):
    __tablename__ = 'teacher'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    class_id = db.Column(db.ForeignKey('class.id'), index=True)

    _class = db.relationship('Clas', primaryjoin='Teacher.class_id == Clas.id', backref='teachers')
