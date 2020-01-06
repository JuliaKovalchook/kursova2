from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://xhtqtijplvyyav:2296695fe193f9e4ceb5e22ff8fb10b3bc0a685dcb4e086b01014cf55e8dadb8@ec2-54-225-119-13.compute-1.amazonaws.com:5432/d3g2tl81l22kh4'

db = SQLAlchemy(app)


class Groups(db.Model):

    __tablename__ = 'groups'
    code = db.Column('code', db.String(64), primary_key=True)
    students = db.relationship('Students', backref='groups', lazy='dynamic')
    group_subject = db.relationship('GroupSubject', backref='groups', lazy='dynamic')

    def __init__(self, code):
        self.code = code
    def __repr__(self):
        return '<Group: code=%r>' % self.code

class Subjects(db.Model):

    __tablename__ = 'subjects'
    name = db.Column('name', db.String(64), primary_key=True)
    def __init__(self, name):

        self.name = name

    def __repr__(self):

        return 'Subject: name=%r' % self.name


class Subjects2(db.Model):

    __tablename__ = 'subjects2'
    predmet = db.Column('predmet', db.String(64), primary_key=True)
    def __init__(self, predmet):

        self.predmet = predmet

    def __repr__(self):

        return 'Subject: predmet=%r' % self.predmet

class StudentStatus(db.Model):

    __tablename__ = 'studentstatus'
    group_code = db.Column('group_code', db.String(64), db.ForeignKey('students.group_code'), primary_key=True)
    study_book = db.Column('study_book', db.String(64), db.ForeignKey('students.study_book'), primary_key=True)
    actual_date = db.Column('actual_date', db.String(64), primary_key=True)
    status = db.Column('status', db.String(64))
    destiny = db.Column('destiny', db.String(64))
    student_group = db.relationship('Students', backref='status_group', lazy=True,
                              foreign_keys=[group_code])
    student_spook = db.relationship('Students', backref='status_spook', lazy=True,
                              foreign_keys=[study_book])

    def __init__(self, study_book, group_code, actual_date, status, destiny):

        self.study_book = study_book
        self.group_code = group_code
        self.actual_date = actual_date
        self.status = status
        self.destiny = destiny

    def __repr__(self):

        return '<StudentStatus: study_book=%r; group_code=%r; actual_date=%r; status=%r; destiny=%r>' %\
               self.study_book, self.group_code, self.actual_date, self.status, self.destiny


class SubjectSheet(db.Model):

    __tablename__ = 'subjectsheet'
    subj_name = db.Column('subj_name', db.String(64), db.ForeignKey('subjects.name'), primary_key=True)
    group_code = db.Column('group_code', db.String(64), db.ForeignKey('students.group_code'), primary_key=True)
    study_book = db.Column('study_book', db.String(64), db.ForeignKey('students.study_book'), primary_key=True)
    date_of_mark = db.Column('date_of_mark', db.Date, primary_key=True)
    mark = db.Column('mark', db.Float, nullable=False)
    student_group = db.relationship('Students', backref='sheet_group', lazy=True,
                              foreign_keys=[group_code])
    student_spook = db.relationship('Students', backref='sheet_spook', lazy=True,
                              foreign_keys=[study_book])

    def __init__(self, subj_name, group_code, study_book, date_of_mark, mark):

        self.subj_name = subj_name
        self.group_code = group_code
        self.study_book = study_book
        self.date_of_mark = date_of_mark
        self.mark = mark

    def __repr__(self):

        return '<SubjectSheet: subj_name=%r; group_code=%r; study_book=%r; date_of_mark=%r; mark=%r>' %\
               self.subj_name, self.group_code, self.study_book, self.date_of_mark, self.mark


class GroupSubject(db.Model):

    __tablename__ = 'group_subject'
    group_code = db.Column('group_code', db.String(64), db.ForeignKey('groups.code'), primary_key=True)
    subj_name = db.Column('subj_name', db.String(64), db.ForeignKey('subjects.name'), primary_key=True)
    year = db.Column('year', db.Integer, primary_key=True)
    semester = db.Column('semester', db.Integer, primary_key=True)

    def __init__(self, group_code, subj_name, year, semester):

        self.group_code = group_code
        self.subj_name = subj_name
        self.year = year
        self.semester = semester

    def __repr__(self):

        return '<GroupSubject: group_code=%r; subj_name=%r; year=%r; semester=%r>' %\
               self.group_code, self.subj_name, self.year, self.semester


class SubjectsMarks(db.Model):

    __tablename__ = 'subjects_marks'

    subj_name = db.Column('subj_name', db.String(64), db.ForeignKey('subjects.name'), primary_key=True)
    curr_max_mark = db.Column('curr_max_mark', db.String(64))
    actual_date = db.Column('actual_date', db.Date, primary_key=True)

    def __init__(self, subj_name, curr_max_mark, actual_date):

        self.subj_name = subj_name
        self.curr_max_mark = curr_max_mark
        self.actual_date = actual_date

    def __repr__(self):

        return '<SubjectsMarks: subj_name=%r; curr_max_mark=%r; actual_date=%r>' %\
               self.subj_name, self.curr_max_mark, self.actual_date


class Students(db.Model):

    __tablename__ = 'students'
    first_name = db.Column('first_name', db.String(64), nullable=False)
    last_name = db.Column('last_name', db.String(64), nullable=False)
    study_book = db.Column('study_book', db.String(64), primary_key=True)
    group_code = db.Column('group_code', db.String(64), db.ForeignKey('groups.code'), primary_key=True)

    def __init__(self, first_name, last_name, study_book, group_code):

        self.first_name = first_name
        self.last_name = last_name
        self.study_book = study_book
        self.group_code = group_code

    def __repr__(self):

        return '<Student: first_name=%r; last_name=%r; study_book=%r; group_code=%r>' % \
               self.first_name, self.last_name, self.study_book, self.group_code


class Providers(db.Model):

    __tablename__ = 'providers'
    name_provider = db.Column('name_provider', db.String(64), primary_key=True)
    type_product = db.Column('type_product', db.String(64), nullable=False)
    products = db.relationship('Products', backref='providers', lazy='dynamic')

    def __init__(self, name_provider, type_product):

        self.name_provider = name_provider
        self.type_product = type_product

    def __repr__(self):

        return '<Provider: name_provider=%r; type_product=%r>' % \
               self.name_provider, self.type_product



class Products(db.Model):

    __tablename__ = 'products'
    name_product = db.Column('name_product', db.String(64), primary_key=True)
    price = db.Column('price', db.String(64), nullable=False)
    provider_name_provider = db.Column('provider_name_provider', db.String(64), db.ForeignKey('providers.name_provider'), primary_key=True)
    advs = db.relationship('Advs', backref='products', lazy='dynamic')

    def __init__(self, name_product, price, provider_name_provider):

        self.name_product = name_product
        self.price = price
        self.provider_name_provider = provider_name_provider

    def __repr__(self):

        return '<Product: name_product=%r; price=%r; provider_name_provider=%r>' % \
               self.name_product, self.price, self.provider_name_provider

class Advs(db.Model):

    __tablename__ = 'advs'
    name_adv = db.Column('name_adv', db.String(64), primary_key=True)
    description = db.Column('description', db.String(200), nullable=False)
    products_name_product = db.Column('products_name_product', db.String(64), db.ForeignKey('products.name_product'), primary_key=True)

    def __init__(self, name_adv, description, products_name_product):

        self.name_adv = name_adv
        self.description = description
        self.products_name_product = products_name_product

    def __repr__(self):

        return '<Adv: name_adv=%r; description=%r; products_name_product=%r>' % \
               self.name_adv, self.description, self.products_name_product


class Viewers(db.Model):

    __tablename__ = 'viewers'
    email = db.Column('email', db.String(50), primary_key=True)
    nikname = db.Column('nikname', db.String(30), nullable=False)
    firstname = db.Column('firstname', db.String(30), nullable=False)
    lastname = db.Column('lastname', db.String(30), nullable=True)
    age = db.Column('age', db.Integer)

    country = db.Column('country', db.String(50))



    def __init__(self, nikname, email, firstname, lastname, age, country):

        self.nikname = nikname
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

        self.country = country


    def __repr__(self):

        return '<Viewer: nikname=%r; email=%r; firstname=%r; lastname=%r; age=%r;  country=%r>' % \
               self.nikname, self.email, self.firstname, self.lastname, self.age,  self.country



'''
class ViewersCanProductsORM(db.Model):

    __tablename__ = 'ViewersCanProducts'
    transasction = db.Column('transasction', db.String(50), nullable=False)
    product_name_product = db.Column('product_name_product', db.String(50), nullable=False)
    product_price = db.Column('product_price', db.Integer, nullable=False)
    viewers_email = db.Column('viewers_email', db.String(30), nullable=True)


    def __init__(self, transasction, product_name_product, product_price, viewers_email):

        self.transasction = transasction
        self.product_name_product = product_name_product
        self.product_price = product_price
        self.viewers_email = viewers_email


    def __repr__(self):

        return '<ViewersCanProducts: transasction=%r; product_name_product=%r; product_price=%r; viewers_email=%r>' % \
               self.transasction, self.product_name_product, self.product_price, self.viewers_email
'''

