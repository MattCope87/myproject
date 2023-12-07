import os
from flask import Flask, render_template, request, redirect, url_for 

app = Flask(__name__, instance_relative_config=True) 
app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'contact.sqlite'),
    )




@app.route("/", methods=["GET"]) 
def home(): 
	
	return render_template('contact.html')
	
@app.route("/result", methods=["POST"]) 
def result(): 
	# append to data container
		
	data = [request.form['fullname'], request.form['email'], request.form['message']]
	#global_data.append(data)
	#fullname = request.form['fullname']
	
	return render_template('result.html', data = data)


from . import db
db.init_app(app)