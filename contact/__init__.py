import os
from flask import Flask, render_template, request, redirect, url_for 

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True) 
	app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'contact.sqlite'),
    )
	if test_config is None:
        # load the instance config, if it exists, when not testing
		app.config.from_pyfile('config.py', silent=True)
	else:
        # load the test config if passed in
		app.config.from_mapping(test_config)
	try:
    	os.makedirs(app.instance_path)

    # ensure the instance folder exists
	except OSError:
        pass
	
	@app.route('/home')
	def home():
		return 'Hello Hello'

	from . import db
	db.init_app(app)
 
	return app

# @app.route("/", methods=["GET"]) 
# def home(): 
	
# 	return render_template('contact.html')
	
# @app.route("/result", methods=["POST"]) 
# def result(): 
# 	# append to data container
		
# 	data = [request.form['fullname'], request.form['email'], request.form['message']]
# 	#global_data.append(data)
# 	#fullname = request.form['fullname']
	
# 	return render_template('result.html', data = data)