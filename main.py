import plotly
import plotly.graph_objs as go
import json
from sqlalchemy import Integer, String, Date, func, Sequence, Table, Column, ForeignKey, text

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from math import e

from flask import render_template, flash, request, redirect, session
from ORM import *
from WTForms import *

app.secret_key = 'development key'
list_adv = []


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


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
            provider = Providers.query.filter_by(name_provider=selected_name_provider,
                                                 type_product=selected_type_product).first()
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
            selected_row = Providers.query.filter_by(name_provider=selected_name_provider,
                                                     type_product=selected_type_product).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('providers.html', data=select_result, form=form)

        selected_pk_data = request.form.get('edit')
        if selected_pk_data is not None:
            selected_pk_data_list = selected_pk_data.split("█")
            selected_name_provider = selected_pk_data_list[0]
            selected_type_product = selected_pk_data_list[1]
            selected_row = Providers.query.filter_by(name_provider=selected_name_provider,
                                                     type_product=selected_type_product).first()
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
            product = Products.query.filter_by(name_product=selected_name_product, price=selected_price,
                                               provider_name_provider=selected_provider_name_provider).first()
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
            selected_row = Products.query.filter_by(name_product=selected_name_product, price=selected_price,
                                                    provider_name_provider=selected_provider_name_provider).first()

            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('products.html', data=select_result, form=form)

        selected_pk_data = request.form.get('edit')
        if selected_pk_data is not None:
            selected_pk_data_list = selected_pk_data.split("█")
            selected_name_product = selected_pk_data_list[0]
            selected_price = selected_pk_data_list[1]
            selected_provider_name_provider = selected_pk_data_list[2]

            selected_row = Products.query.filter_by(name_product=selected_name_product, price=selected_price,
                                                    provider_name_provider=selected_provider_name_provider).first()

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

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required')
            return render_template('advs.html', data=select_result, form=form)
        else:
            selected_pk_data_list = session['adv_edit_pk_data'].split("█")
            selected_name_adv = selected_pk_data_list[0]
            selected_description = selected_pk_data_list[1]
            selected_products_name_product = selected_pk_data_list[2]

            print(selected_name_adv, selected_description, selected_products_name_product)
            adv = Advs.query.filter_by(name_adv=selected_name_adv, description=selected_description,
                                       products_name_product=selected_products_name_product).first()

            adv.name_adv = form.name_adv.data
            adv.description = form.description.data
            adv.provider_name_provider = form.products_name_product.data
            db.session.commit()

    return render_template('advs.html', data=select_result, form=form)


@app.route('/advs', methods=['GET', 'POST'])
def advs():
    form = AdvsForm()
    select_result = Advs.query.filter_by().all()

    if request.method == 'POST':

        selected_pk_data = request.form.get('del')
        if selected_pk_data is not None:
            selected_pk_data = selected_pk_data.split("█")
            selected_name_adv = selected_pk_data[0]
            selected_description = selected_pk_data[1]
            selected_products_name_product = selected_pk_data[2]

            print(selected_name_adv, selected_description, selected_products_name_product)
            selected_row = Advs.query.filter_by(name_adv=selected_name_adv, description=selected_description,
                                                products_name_product=selected_products_name_product).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('advs.html', data=select_result, form=form)

        selected_pk_data = request.form.get('edit')
        if selected_pk_data is not None:
            selected_pk_data_list = selected_pk_data.split("█")
            selected_name_adv = selected_pk_data_list[0]
            selected_description = selected_pk_data_list[1]
            selected_products_name_product = selected_pk_data_list[2]
            selected_row = Advs.query.filter_by(name_adv=selected_name_adv, description=selected_description,
                                                products_name_product=selected_products_name_product).first()

            session['adv_edit_pk_data'] = selected_pk_data
            return render_template("edit_adv.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('advs.html', data=select_result, form=form)
        else:
            adv = Advs(form.name_adv.data, form.description.data, form.products_name_product.data)
            db.session.add(adv)
            db.session.commit()
            select_result.append(adv)

    return render_template('advs.html', data=select_result, form=form)


@app.route('/edit_viewer', methods=['GET', 'POST'])
def edit_viewer():
    form = ViewersForm()
    select_result = Viewers.query.filter_by().all()
    '''
    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required')
            return render_template('viewers.html', data=select_result, form=form)
        else:
            selected_pk_data_list = session['viewer_edit_pk_data'].split("█")
            selected_email = selected_pk_data_list[0]
            selected_nikname = selected_pk_data_list[1]
            selected_firstname = selected_pk_data_list[2]
            selected_lastname = selected_pk_data_list[2]
        selected_age = selected_pk_data_list[2]
        selected_country = selected_pk_data_list[2]

        print(selected_email, selected_nikname, selected_firstname, selected_lastname, selected_age, selected_country)
        viewer = Viewers.query.filter_by(email=selected_email, nikname=selected_nikname, firstname=selected_firstname,
                                         lastname=selected_lastname, age=selected_age, country=selected_country).first()

        viewer.email = form.email.data
        viewer.nikname = form.nikname.data
        viewer.firstname = form.firstname.data
        viewer.lastname = form.lastname.data
        viewer.age = form.age.data
        viewer.country = form.country.data
        db.session.commit()
    '''
    return render_template('viewers.html', data=select_result, form=form)


@app.route('/viewers', methods=['GET', 'POST'])
def viewers():
    form = ViewersForm()
    select_result = Viewers.query.filter_by().all()

    if request.method == 'POST':

        selected_pk_data = request.form.get('del')
        if selected_pk_data is not None:
            selected_pk_data = selected_pk_data.split("█")
            selected_nikname  = selected_pk_data[0]
            selected_email = selected_pk_data[1]
            selected_firstname = selected_pk_data[2]
            selected_lastname = selected_pk_data[3]
            selected_age = selected_pk_data[4]
            selected_country = selected_pk_data[5]

            print(selected_nikname, selected_email,  selected_firstname, selected_lastname, selected_age, selected_country)
            selected_row = Viewers.query.filter_by( nikname=selected_nikname,email=selected_email,
                                                   firstname=selected_firstname, lastname=selected_lastname,
                                                   age=selected_age, country=selected_country).first()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('viewers.html', data=select_result, form=form)

        selected_pk_data = request.form.get('edit')
        if selected_pk_data is not None:
            selected_pk_data_list = selected_pk_data.split("█")
            selected_nikname = selected_pk_data_list[0]
            selected_email = selected_pk_data_list[1]
            selected_firstname = selected_pk_data_list[2]
            selected_lastname = selected_pk_data_list[3]
            selected_age = selected_pk_data_list[4]
            selected_country = selected_pk_data_list[5]

            selected_row = Viewers.query.filter_by(nikname=selected_nikname, email=selected_email,  firstname=selected_firstname,
                                                   lastname=selected_lastname, age=selected_age,
                                                   country=selected_country).first()
            session['viewer_edit_pk_data'] = selected_pk_data
            return render_template("edit_viewer.html", row=selected_row, form=form)


        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('viewers.html', data=select_result, form=form)
        else:
            viewer = Viewers(form.nikname.data, form.email.data, form.firstname.data, form.lastname.data, form.age.data,
                             form.country.data)
            db.session.add(viewer)
            db.session.commit()
            select_result.append(viewer)

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


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    last_char = None
    if request.method == 'POST':

        last_char = request.form.get('last_char')
        if len(last_char) > 1:
            return redirect('/dashboard')

    select_result_raw = Providers.query.filter_by().all()

    select_result = [select_result_row.type_product for select_result_row in select_result_raw]

    type_product_starts_result = list(map(lambda s: s[:20], select_result))
    type_product = list(set(type_product_starts_result))
    counting_stars = [0] * len(type_product)

    for no_more in type_product_starts_result:
        counting_stars[type_product.index(no_more[:20])] += 1

    bar, pie = go.Bar(x=type_product, y=counting_stars, marker=dict(color='rgb(122, 122, 122)')), go.Pie(
        labels=type_product, values=counting_stars)

    data1, data2 = [bar], [pie]
    ids = ["1", "2"]

    graphJSON1 = json.dumps(data1, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(data2, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html',
                           graphJSON1=graphJSON1, graphJSON2=graphJSON2, ids=ids)


@app.route('/claster', methods=['GET', 'POST'])
def claster():
    df = pd.DataFrame()

    for name_product, provider_name_provider in db.session.query(Products.name_product,
                                                                 Products.provider_name_provider):
        df = df.append({"name_product": name_product, "provider_name_provider": provider_name_provider},
                       ignore_index=True)

    X = pd.get_dummies(data=df)
    print(X)
    count_clasters = len(df['provider_name_provider'].unique())
    print(count_clasters)
    kmeans = KMeans(n_clusters=count_clasters, random_state=0).fit(X)
    print(kmeans)
    count_columns = len(X.columns)
    test_list = [0] * count_columns
    test_list[1] = 1
    test_list[-1] = 1
    print(test_list)
    print(kmeans.labels_)
    print(kmeans.predict(np.array([test_list])))
    db.session.close()
    query1 = (
        db.session.query(
            func.count(),
            Products.provider_name_provider
        ).group_by(Products.provider_name_provider)
    ).all()

    skills, user_count = zip(*query1)
    pie = go.Pie(
        labels=user_count,
        values=skills
    )

    data = [pie]
    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('claster.html', row=kmeans.predict(np.array([test_list]))[0],
                           count_claster=count_clasters, graphsJSON=graphsJSON)


@app.route('/correlations', methods=['GET', 'POST'])
def correlations():
    df = pd.DataFrame()

    for name_product, count, avg in db.session.query(Products.name_product, func.count(Products.name_product),
                                                     func.avg(Products.price)
                                                     ).group_by(Products.name_product):
        df = df.append({"count_name_product": float(count), "avg_price": float(avg)}, ignore_index=True)
    db.session.close()
    query = (
        db.session.query(Products.name_product, func.count(Products.name_product), func.avg(Products.price)
                         ).group_by(Products.name_product)
    ).all()

    scaler = StandardScaler()
    scaler.fit(df[["count_name_product"]])
    train_X = scaler.transform(df[["count_name_product"]])
    print(train_X, df[["avg_price"]])
    reg = LinearRegression().fit(train_X, df[["avg_price"]])

    test_array = [[5]]
    test = scaler.transform(test_array)
    result = reg.predict(test)

    name_product, price, user_count = zip(*query)
    scatter = go.Scatter(
        x=price,
        y=user_count,
        mode='markers',
        marker_color='rgba(255, 0, 0, 100)',
        name="data"
    )
    x_line = np.linspace(0, 10)
    y_line = x_line * reg.coef_[0, 0] + reg.intercept_[0]
    line = go.Scatter(
        x=x_line,
        y=y_line,
        mode='lines',
        marker_color='rgba(255, 149, 0, 1)',
        name="regretion"
    )

    data = [scatter, line]

    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('regretion.html', graphsJSON=graphsJSON)


'''
@app.route('/correlation', methods=['GET', 'POST'])
def correlation():
    counts = []

    for name_product, count, provider_name_provider in db.session.query(Products.name_product, func.count(Products.name_product),
                                                 func.max(Products.provider_name_provider)).group_by(Products.name_product):
        counts.append({"name_product": name_product, "count_events": count, "name": provider_name_provider})
    seq = [x['count_events'] for x in counts]
    print(counts)
    res = ''
    for row in counts:
        if row['count_events'] == max(seq):
            res = row['name']
    return render_template('correlation.html', row=res)



@app.route('/search', methods=['GET', 'POST'])
def search():
    form = CreateQuery()
    if request.method == 'POST':

        list_adv.clear()
        for name_adv, description, products_name_product in db.session.query(Advs.name_adv, Advs.description,
                                                                             Advs.products_name_product):
            if products_name_product == form.products_name_product.data:
                list_adv.append(name_adv)

        return redirect(url_for('searchList'))

    return render_template('search.html', form=form, form_name="Search", action="search")


'''
@app.route('/search/result')
    def searchList():
        res = []
        try:
            for i in list_adv:
                name, new_skill, hashtag, city, dates, bonus = db.session \
                    .query(ormEvent.name_adv, ormPlan.description, ormEvent.hashtag, ormEvent.city, ormEvent.dates, ormBonus.name) \
                    .join(ormBonus, ormEvent.event_id == ormBonus.event_id).join(ormPlan,
                                                                                 ormEvent.event_id == ormPlan.event_id) \
                    .filter(ormEvent.event_id == i).one()
                res.append(
                    {"name_adv": name_adv, "description": description, "products_name_product": products_name_product})

                                 name, new_skill, hashtag, city, dates, bonus = db.session \
                    .query(Advs.name_adv, Advs.description, Advs.products_name_product) \
                    .join(Products, Products.name_product == Advs.products_name_product)
                    .filter(Products.name_product == i).one()
        except:
            print("don't data")
        print(list_adv)

    return render_template('search_list_adv.html', name="result", results=res, action="/search/result")
'''

if __name__ == '__main__':
    app.run(debug=True)

