from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email


class ContactForm(FlaskForm):
	name = StringField('Name', validators=[InputRequired()])
	email = StringField('Email', validators=[InputRequired(), Email("Please provide a valid email.")])
	subject = StringField('Subject', validators=[InputRequired()])
	message = TextAreaField('Message', validators=[InputRequired()])


