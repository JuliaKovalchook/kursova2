from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://enbazddkyxxwzr:b6ec78b08d3c77d444a87db3ad133790952e40089de037d6e1addca627631492@ec2-107-21-214-222.compute-1.amazonaws.com:5432/d3gl6r9dgqcu6c'

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
    '''
    products = db.relationship('Products', backref='providers', lazy='dynamic')
'''

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

    def __init__(self, name_product, price, provider_name_provider):

        self.name_product = name_product
        self.price = price
        self.provider_name_provider = provider_name_provider

    def __repr__(self):

        return '<Product: name_product=%r; price=%r; provider_name_provider=%r>' % \
               self.name_product, self.price, self.provider_name_provider

