
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class BookForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired(), Length(min=1, max=100)])
    authors = StringField('Autorzy (oddziel przecinkiem)', validators=[DataRequired()])
    year = IntegerField('Rok wydania', validators=[NumberRange(min=0, max=2100)])
    genre = StringField('Gatunek', validators=[Length(max=100)])
    pages = IntegerField('Liczba stron', validators=[NumberRange(min=1, max=10000)])
    description = TextAreaField('Opis', validators=[Length(max=500)])
    is_available = BooleanField('Dostępna na półce')
    submit = SubmitField('Zapisz książkę')