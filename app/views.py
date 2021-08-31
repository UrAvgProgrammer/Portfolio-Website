from flask import render_template, redirect, url_for
from app import app

@app.route('/')
def index():
	return render_template('landing-page.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')