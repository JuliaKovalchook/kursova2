
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField,FloatField,Label
from wtforms import validators
from wtforms.validators import NumberRange, Required, DataRequired



class ProvidersForm(FlaskForm):

    name_provider = StringField("name_provider: ", [validators.data_required("Please, enter a first name_provider.")])
    type_product = StringField("type_product : ", [validators.data_required("Please, enter a last type_product.")])

    submit = SubmitField("Enter")



class ProductsForm(FlaskForm):

    name_product = StringField("name_product: ", [validators.data_required("Please, enter a name_product.")])
    price = StringField("price: ", [validators.data_required("Please, enter a price.")])
    provider_name_provider = StringField("provider_name_provider: ", [validators.data_required("Please, enter a name_provider.")])

    submit = SubmitField("Enter")



class AdvsForm(FlaskForm):

    name_adv = StringField("name_adv: ", [validators.data_required("Please, enter a name_adv.")])
    description = StringField("description: ", [validators.data_required("Please, enter a description.")])
    products_name_product = StringField("products_name_product: ", [validators.data_required("Please, enter a name product.")])

    submit = SubmitField("Enter")

class ViewersForm(FlaskForm):

    nikname = StringField("nikname: ", [validators.data_required("Please, enter a nikname of the Viewer")])
    email = StringField("email: ", [validators.data_required("Please, enter a email of the Viewer")])
    firstname = StringField("firstname: ", [validators.data_required("Please, enter a firstnameof the Viewer")])
    lastname = StringField("lastname: ", [validators.data_required("Please, enter a lastname of the Viewer")])
    age = IntegerField("age: ", [validators.data_required("Please, enter an age of the Viewer")])

    country = StringField("country: ", [validators.data_required("Please, enter a country book of the Viewer")])

    submit = SubmitField("Enter")
'''
class ViewersCanProductsForm(FlaskForm):

    transasction = StringField("transasction: ", [validators.data_required("Please, enter a nikname of the Viewer")])
    product_name_product = StringField("product_name_product: ", [validators.data_required("Please, enter a email of the Viewer")])
    product_price = IntegerField("product_price: ", [validators.data_required("Please, enter a firstnameof the Viewer")])
    viewers_email = StringField("viewers_email: ", [validators.data_required("Please, enter a lastname of the Viewer")])

    submit = SubmitField("Enter")


'''
