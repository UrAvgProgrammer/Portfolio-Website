from flask import render_template, redirect, url_for
from app import app, mail
from flask_mail import Message
from .forms import ContactForm


@app.route('/', methods=['GET'])
def index():
	return render_template('landing-page.html')

@app.route('/projects', methods=['GET'])
def projects():
	return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if form.validate_on_submit():
		data = {
			'name': form.name.data,
			'email': form.email.data,
			'subject': form.subject.data,
			'message': form.message.data
		}
		msg = Message(
				body=data['message'],
				sender=data['email'],
				subject=data['subject'],
				recipients=['pvtcortez@gmail.com']
			)
		return redirect(url_for('index'))
	else:
		return render_template('contact.html', form=form)
	return render_template('contact.html', form=form)