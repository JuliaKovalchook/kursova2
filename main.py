import plotly
import plotly.graph_objs as go
import json

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from math import e

from flask import render_template, flash, request, redirect, session
from ORM import *
from WTForms import *

app.secret_key = 'development key'

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@app.route('/edit_group', methods = ['GET', 'POST'])
def edit_group():

    form = GroupsForm()
    select_result = Groups.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required')
            return render_template('groups.html', data=select_result, form=form)
        else:
            group_code = session['group_edit_pk_data']
            group = Groups.query.filter_by(code=group_code).first()
            group.code = form.code.data
            db.session.commit()
            return render_template("groups.html", data=select_result, form=form)

    return render_template("groups.html", data=select_result, form=form)


@app.route('/groups', methods=['GET', 'POST'])
def groups():

    form = GroupsForm()
    select_result = Groups.query.filter_by().all()

    if request.method == 'POST':

        selected_code = request.form.get('del')
        if selected_code is not None:
            selected_row = Groups.query.filter_by(code=selected_code).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('groups.html', data=select_result, form=form)

        selected_code = request.form.get('edit')
        if selected_code is not None:
            selected_row = Groups.query.filter_by(code=selected_code).first()
            session['group_edit_pk_data'] = selected_code
            return render_template("edit_group.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('groups.html', data=select_result, form=form)
        else:
            group = Groups(form.code.data)
            db.session.add(group)
            db.session.commit()
            select_result.append(group)

    return render_template('groups.html', data=select_result, form=form)


@app.route('/edit_subject', methods=['GET', 'POST'])
def edit_subject():

    form = SubjectsForm()
    select_result = Subjects.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required.')
            return render_template('edit_subject.html')
        else:
            subject_name = session['subject_edit_pk_data']
            subject = Subjects.query.filter_by(name=subject_name).first()
            subject.name = form.name.data
            db.session.commit()
            return render_template("subjects.html", data=select_result, form=form)

    return render_template("subjects.html", data=select_result, form=form)


@app.route('/subjects', methods=['GET', 'POST'])
def subjects():

    form = SubjectsForm()
    select_result = Subjects.query.filter_by().all()

    if request.method == 'POST':

        selected_name = request.form.get('del')
        if selected_name is not None:
            selected_row = Subjects.query.filter_by(name=selected_name).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('subjects.html', data=select_result, form=form)

        selected_name = request.form.get('edit')
        if selected_name is not None:
            selected_row = Subjects.query.filter_by(name=selected_name).first()
            session['subject_edit_pk_data'] = selected_name
            return render_template("edit_subject.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('subjects.html', data=select_result, form=form)
        else:
            subject = Subjects(form.name.data)
            db.session.add(subject)
            db.session.commit()
            select_result.append(subject)

    return render_template('subjects.html', data=select_result, form=form)



@app.route('/edit_student', methods=['GET', 'POST'])
def edit_student():

    form = StudentsForm()
    select_result = Students.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required')
            return render_template('students.html', data=select_result, form=form)
        else:
            selected_pk_data_list = session['student_edit_pk_data'].split("█")
            selected_group_code = selected_pk_data_list[0]
            selected_spooky_book = selected_pk_data_list[1]
            print(selected_group_code, selected_spooky_book)
            student = Students.query.filter_by(study_book=selected_spooky_book, group_code=selected_group_code).first()
            student.first_name = form.first_name.data
            student.last_name = form.last_name.data
            student.study_book = form.study_book.data
            student.group_code = form.group_code.data
            db.session.commit()


    return render_template("students.html", data=select_result, form=form)


@app.route('/students', methods=['GET', 'POST'])
def students():

    form = StudentsForm()
    select_result = Students.query.filter_by().all()

    if request.method == 'POST':

        selected_pk_data = request.form.get('del')
        if selected_pk_data is not None:
            selected_pk_data = selected_pk_data.split("█")
            selected_group_code = selected_pk_data[0]
            selected_spooky_book = selected_pk_data[1]
            print(selected_spooky_book, selected_group_code)
            selected_row = Students.query.filter_by(study_book=selected_spooky_book, group_code=selected_group_code).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('students.html', data=select_result, form=form)

        selected_pk_data = request.form.get('edit')
        if selected_pk_data is not None:
            selected_pk_data_list = selected_pk_data.split("█")
            selected_group_code = selected_pk_data_list[0]
            selected_spooky_book = selected_pk_data_list[1]
            selected_row = Students.query.filter_by(study_book=selected_spooky_book, group_code=selected_group_code).first()
            session['student_edit_pk_data'] = selected_pk_data
            return render_template("edit_student.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('students.html', data=select_result, form=form)
        else:
            student = Students(form.first_name.data, form.last_name.data, form.study_book.data, form.group_code.data)
            db.session.add(student)
            db.session.commit()
            select_result.append(student)

    return render_template('students.html', data=select_result, form=form)



@app.route('/edit_subjectsheet', methods=['GET', 'POST'])
def edit_subjectsheet():

    form = SubjectSheetForm()
    select_result = SubjectSheet.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required')
            return render_template('subjectsheet.html', data=select_result, form=form)
        else:
            selected_pk_data_list = session['subjectsheet_edit_pk_data'].split("█")
            selected_subj_name = selected_pk_data_list[0]
            selected_group_code = selected_pk_data_list[1]
            selected_spooky_book = selected_pk_data_list[2]
            selected_date_of_mark = selected_pk_data_list[3]
            subjectsheet = SubjectSheet.query.filter_by(subj_name=selected_subj_name,
                                                        study_book=selected_spooky_book,
                                                        group_code=selected_group_code,
                                                        date_of_mark=selected_date_of_mark).first()
            subjectsheet.subj_name = form.subj_name.data
            subjectsheet.group_code = form.group_code.data
            subjectsheet.study_book = form.study_book.data
            subjectsheet.date_of_mark = form.date_of_mark.data
            subjectsheet.mark = form.mark.data
            db.session.commit()
            return render_template("subjectsheet.html", data=select_result, form=form)

    return render_template("subjectsheet.html", data=select_result, form=form)


@app.route('/subjectsheet', methods=['GET', 'POST'])
def subjectsheet():

    form = SubjectSheetForm()
    select_result = SubjectSheet.query.filter_by().all()

    if request.method == 'POST':

        selected_pk_data = request.form.get('del')
        if selected_pk_data is not None:
            selected_pk_data = selected_pk_data.split("█")
            selected_subj_name = selected_pk_data[0]
            selected_group_code = selected_pk_data[1]
            selected_spooky_book = selected_pk_data[2]
            selected_date_of_mark = selected_pk_data[3]
            selected_row = SubjectSheet.query.filter_by(subj_name=selected_subj_name, group_code=selected_group_code,
                                                    study_book=selected_spooky_book, date_of_mark=selected_date_of_mark).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('subjectsheet.html', data=select_result, form=form)

        selected_pk_data = request.form.get('edit')
        if selected_pk_data is not None:
            selected_pk_data_list = selected_pk_data.split("█")
            selected_subj_name = selected_pk_data_list[0]
            selected_group_code = selected_pk_data_list[1]
            selected_spooky_book = selected_pk_data_list[2]
            selected_date_of_mark = selected_pk_data_list[3]
            selected_row = SubjectSheet.query.filter_by(subj_name=selected_subj_name,
                                                        study_book=selected_spooky_book,
                                                        group_code=selected_group_code,
                                                        date_of_mark=selected_date_of_mark).first()
            session['subjectsheet_edit_pk_data'] = selected_pk_data
            return render_template("edit_subjectsheet.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('subjectsheet.html', data=select_result, form=form)
        else:
            subjectsheet = SubjectSheet(form.subj_name.data, form.group_code.data, form.study_book.data,
                                        form.date_of_mark.data, form.mark.data)
            db.session.add(subjectsheet)
            db.session.commit()
            select_result.append(subjectsheet)

    return render_template('subjectsheet.html', data=select_result, form=form)

@app.route('/edit_Provider123', methods=['GET', 'POST'])
def edit_Provider123():

    form = Provider123sForm()
    select_result = Provider123s.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required.')
            return render_template('edit_Provider123.html')
        else:
            Provider123_Name_Provider123 = session['Provider123_edit_pk_data']
            Provider123 = Provider123s.query.filter_by(Name_Provider123=Provider123_Name_Provider123).first()
            Provider123.Name_Provider123 = form.Name_Provider123.data
            db.session.commit()
            return render_template("Provider123s.html", data=select_result, form=form)

    return render_template("Provider123s.html", data=select_result, form=form)


@app.route('/Provider123s', methods=['GET', 'POST'])
def Provider123s():

    form = Provider123sForm()
    select_result = Provider123s.query.filter_by().all()

    if request.method == 'POST':

        selected_Name_Provider123 = request.form.get('del')
        if selected_Name_Provider123 is not None:
            selected_row = Provider123s.query.filter_by(Name_Provider123=selected_Name_Provider123).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('Provider123s.html', data=select_result, form=form)

        selected_Name_Provider123 = request.form.get('edit')
        if selected_Name_Provider123 is not None:
            selected_row = Provider123s.query.filter_by(Name_Provider123=selected_Name_Provider123).first()
            session['Provider123_edit_pk_data'] = selected_Name_Provider123
            return render_template("edit_Provider123.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('Provider123s.html', data=select_result, form=form)
        else:
            Provider123 = Provider123s(form.Name_Provider123.data)
            db.session.add(Provider123)
            db.session.commit()
            select_result.append(Provider123)

    return render_template('Provider123s.html', data=select_result, form=form)



if __name__ == '__main__':
    app.run(debug=True)