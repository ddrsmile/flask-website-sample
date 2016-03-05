# project/contact/forms.py

from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Email, Length

class ContactForm(Form):
  contact_id = IntegerField()
  name = StringField('User Name', validators=[DataRequired()])
  company = StringField('Company Name')
  email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
  subject = StringField('Subject')
  message = StringField('Message', widget=TextArea())