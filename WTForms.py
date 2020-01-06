
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField,FloatField,Label
from wtforms import validators
from wtforms.validators import NumberRange, Required, DataRequired



class GroupsForm(FlaskForm):

    code = StringField("Code: ", [validators.data_required("Please, enter a code of the group.")])

    submit = SubmitField("Enter")



class SubjectsForm(FlaskForm):

    name = StringField("Name: ", [validators.data_required("Please, enter a name of the subject.")])
    submit = SubmitField("Enter")



class Subjects2Form(FlaskForm):

    predmet = StringField("Predmet: ", [validators.data_required("Please, enter a name of the predmet.")])

    submit = SubmitField("Enter")



class StudentsForm(FlaskForm):

    first_name = StringField("First name: ", [validators.data_required("Please, enter a first name of the student.")])
    last_name = StringField("Last name: ", [validators.data_required("Please, enter a last name of the student.")])
    study_book = StringField("Study book: ", [validators.data_required("Please, enter a study book of the student.")])
    group_code = StringField("Group code: ", [validators.data_required("Please, enter a group code of the student.")])

    submit = SubmitField("Enter")



class ProvidersForm(FlaskForm):

    name_provider = StringField("name_provider: ", [validators.data_required("Please, enter a first name of the student.")])
    type_product = StringField("type_product : ", [validators.data_required("Please, enter a last name of the student.")])

    submit = SubmitField("Enter")


class SubjectSheetForm(FlaskForm):

    subj_name = StringField("Subject Name: ", [validators.data_required("Please, enter a name of the subject.")])
    group_code = StringField("Group code: ", [validators.data_required("Please, enter a group code of the student.")])
    study_book = StringField("Study book: ", [validators.data_required("Please, enter a study book of the student.")])
    date_of_mark = DateField("Date of Mark: ", [validators.data_required("Please, enter a date of the mark.")])
    mark = FloatField("Mark: ", [validators.data_required("Please, enter the mark.")])

    submit = SubmitField("Enter")


class ProductsForm(FlaskForm):

    name_product = StringField("name_product: ", [validators.data_required("Please, enter a name of the subject.")])
    price = StringField("price: ", [validators.data_required("Please, enter a group code of the student.")])
    provider_name_provider = StringField("provider_name_provider: ", [validators.data_required("Please, enter a study book of the student.")])

    submit = SubmitField("Enter")



class AdvsForm(FlaskForm):

    name_adv = StringField("name_adv: ", [validators.data_required("Please, enter a name of the subject.")])
    description = StringField("description: ", [validators.data_required("Please, enter a group code of the student.")])
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

class ViewersCanProductsForm(FlaskForm):

    transasction = StringField("transasction: ", [validators.data_required("Please, enter a nikname of the Viewer")])
    product_name_product = StringField("product_name_product: ", [validators.data_required("Please, enter a email of the Viewer")])
    product_price = IntegerField("product_price: ", [validators.data_required("Please, enter a firstnameof the Viewer")])
    viewers_email = StringField("viewers_email: ", [validators.data_required("Please, enter a lastname of the Viewer")])

    submit = SubmitField("Enter")



