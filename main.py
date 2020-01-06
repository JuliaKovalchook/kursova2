import plotly
import plotly.graph_objs as go
import json
from sqlalchemy import Integer, String, Date, func, Sequence, Table, Column, ForeignKey, text


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
            return render_template("subjects.html", row=selected_row, form=form)

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


@app.route('/edit_subject2', methods=['GET', 'POST'])
def edit_subject2():
    form = Subjects2Form()
    select_result = Subjects2.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required.')
            return render_template('edit_subject2.html')
        else:
            subject2_predmet = session['subject2_edit_pk_data']
            subject2 = Subjects2.query.filter_by(predmet=subject2_predmet).first()
            subject2.predmet = form.predmet.data
            db.session.commit()
            return render_template("subjects2.html", data=select_result, form=form)

    return render_template("subjects2.html", data=select_result, form=form)

@app.route('/subjects2', methods=['GET', 'POST'])
def subjects2():

    form = Subjects2Form()
    select_result = Subjects2.query.filter_by().all()
    if request.method == 'POST':

        selected_predmet = request.form.get('del')
        if selected_predmet is not None:
            selected_row = Subjects.query.filter_by(predmet=selected_predmet).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('subjects2.html', data=select_result, form=form)

        selected_predmet = request.form.get('edit')
        if selected_predmet is not None:
            selected_row = Subjects2.query.filter_by(predmet=selected_predmet).first()
            session['subject2_edit_pk_data'] = selected_predmet
            return render_template("subjects2.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('subjects2.html', data=select_result, form=form)
        else:
            subject2 = Subjects2(form.predmet.data)
            db.session.add(subject2)
            db.session.commit()
            select_result.append(subject2)

    return render_template('subjects2.html', data=select_result, form=form)


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


@app.route('/edit_provider', methods=['GET', 'POST'])
def edit_provider():

    form = ProvidersForm()
    select_result = Providers.query.filter_by().all()
    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required')
            return render_template('providers.html', data=select_result, form=form)
        else:
            selected_pk_data_list = session['provider_edit_pk_data'].split("█")
            selected_name_provider = selected_pk_data_list[0]
            selected_type_product = selected_pk_data_list[1]
            print(selected_name_provider, selected_type_product)
            provider = Providers.query.filter_by(name_provider=selected_name_provider, type_product=selected_type_product).first()
            provider.name_provider = form.name_provider.data
            provider.type_product = form.type_product.data
            db.session.commit()

    return render_template("providers.html", data=select_result, form=form)


@app.route('/providers', methods=['GET', 'POST'])
def providers():

    form = ProvidersForm()
    select_result = Providers.query.filter_by().all()
    if request.method == 'POST':

        selected_pk_data = request.form.get('del')
        if selected_pk_data is not None:
            selected_pk_data = selected_pk_data.split("█")
            selected_name_provider = selected_pk_data[0]
            selected_type_product = selected_pk_data[1]
            print(selected_name_provider, selected_type_product)
            selected_row = Providers.query.filter_by(name_provider=selected_name_provider, type_product=selected_type_product).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('providers.html', data=select_result, form=form)

        selected_pk_data = request.form.get('edit')
        if selected_pk_data is not None:
            selected_pk_data_list = selected_pk_data.split("█")
            selected_name_provider = selected_pk_data_list[0]
            selected_type_product = selected_pk_data_list[1]
            selected_row = Providers.query.filter_by(name_provider=selected_name_provider, type_product=selected_type_product).first()
            session['provider_edit_pk_data'] = selected_pk_data
            return render_template("edit_provider.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('providers.html', data=select_result, form=form)
        else:
            provider = Providers(form.name_provider.data, form.type_product.data)
            db.session.add(provider)
            db.session.commit()
            select_result.append(provider)

    return render_template('providers.html', data=select_result, form=form)

@app.route('/edit_product', methods=['GET', 'POST'])
def edit_product():

    form = ProductsForm()
    select_result = Products.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required')
            return render_template('products.html', data=select_result, form=form)
        else:
            selected_pk_data_list = session['product_edit_pk_data'].split("█")
            selected_name_product = selected_pk_data_list[0]
            selected_price = selected_pk_data_list[1]
            selected_provider_name_provider = selected_pk_data_list[2]

            print(selected_name_product, selected_price, selected_provider_name_provider)
            product = Products.query.filter_by(name_product=selected_name_product, price=selected_price, provider_name_provider=selected_provider_name_provider).first()
            product.name_product = form.name_product.data
            product.price = form.price.data
            product.provider_name_provider = form.provider_name_provider.data
            db.session.commit()


    return render_template('products.html', data=select_result, form=form)


@app.route('/products', methods=['GET', 'POST'])
def products():

    form = ProductsForm()
    select_result = Products.query.filter_by().all()
    if request.method == 'POST':

        selected_pk_data = request.form.get('del')
        if selected_pk_data is not None:
            selected_pk_data = selected_pk_data.split("█")
            selected_name_product = selected_pk_data[0]
            selected_price = selected_pk_data[1]
            selected_provider_name_provider = selected_pk_data[2]

            print(selected_name_product, selected_price, selected_provider_name_provider)
            selected_row = Products.query.filter_by(name_product=selected_name_product, price=selected_price, provider_name_provider =selected_provider_name_provider).first()

            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('prodicts.html', data=select_result, form=form)

        selected_pk_data = request.form.get('edit')
        if selected_pk_data is not None:
            selected_pk_data_list = selected_pk_data.split("█")
            selected_name_product = selected_pk_data_list[0]
            selected_price = selected_pk_data_list[1]
            selected_provider_name_provider = selected_pk_data_list[2]

            selected_row = Products.query.filter_by(name_product=selected_name_product, price=selected_price, provider_name_provider=selected_provider_name_provider).first()

            session['product_edit_pk_data'] = selected_pk_data
            return render_template("edit_product.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('products.html', data=select_result, form=form)
        else:
            product = Products(form.name_product.data, form.price.data, form.provider_name_provider.data)
            db.session.add(product)
            db.session.commit()
            select_result.append(product)

    return render_template('products.html', data=select_result, form=form)



@app.route('/edit_adv', methods=['GET', 'POST'])
def edit_adv():

    form = AdvsForm()
    select_result = Advs.query.filter_by().all()
    return render_template('advs.html', data=select_result, form=form)


@app.route('/advs', methods=['GET', 'POST'])
def advs():

    form = AdvsForm()
    select_result = Advs.query.filter_by().all()
    return render_template('advs.html', data=select_result, form=form)


@app.route('/edit_viewer', methods=['GET', 'POST'])
def edit_viewer():

    form = ViewersForm()
    select_result = Viewers.query.filter_by().all()
    return render_template('viewers.html', data=select_result, form=form)


@app.route('/viewers', methods=['GET', 'POST'])
def viewers():

    form = ViewersForm()
    select_result = Viewers.query.filter_by().all()
    return render_template('viewers.html', data=select_result, form=form)
'''
@app.route('/edit_ViewersCanProduct', methods=['GET', 'POST'])
def edit_ViewersCanProduct():

    form = ViewersCanProductsForm()
    select_result = ViewersCanProductsORM.query.filter_by().all()
    return render_template('ViewersCanProducts.html', data=select_result, form=form)


@app.route('/ViewersCanProducts', methods=['GET', 'POST'])
def ViewersCanProducts():

    form = ViewersCanProductsForm()
    select_result = ViewersCanProductsORM.query.filter_by().all()
    return render_template('ViewersCanProducts.html', data=select_result, form=form)

'''
'''
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    last_char = None
    if request.method == 'POST':

        last_char = request.form.get('last_char')
        if len(last_char) > 1:
            return redirect('/dashboard')

    select_result_raw = Groups.query.filter_by().all()
    if last_char is not None and last_char != "":
        select_result = [select_result_row.code for select_result_row in select_result_raw
                         if select_result_row.code[-1] == last_char]
    else:
        select_result = [select_result_row.code for select_result_row in select_result_raw]

    codes_starts_result = list(map(lambda s: s[:2], select_result))
    codes = list(set(codes_starts_result))
    counting_stars = [0] * len(codes)

    for no_more_counting_dollars in codes_starts_result:
        counting_stars[codes.index(no_more_counting_dollars[:2])] += 1

    bar, pie = go.Bar(x=codes, y=counting_stars, marker=dict(color='rgb(122, 122, 122)')), go.Pie(labels=codes, values=counting_stars)

    data1, data2 = [bar], [pie]
    ids = ["1", "2"]

    graphJSON1 = json.dumps(data1, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(data2, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard1.html',
                           graphJSON1=graphJSON1, graphJSON2=graphJSON2, ids=ids)
'''
def dashboard():
    query1 = (
        db.session.query(
            func.count(),
            Providers.type_product
        ).group_by(Providers.type_product)
    ).all()



    type_product, type_product_count = zip(*query1)
    pie = go.Pie(
        labels=type_product_count,
        values=type_product
    )
    print(type_product, type_product_count)

    data = {
        "pie": [pie]
    }
    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphsJSON)

if __name__ == '__main__':
    app.run(debug=True)
