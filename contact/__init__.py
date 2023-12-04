from flask import Flask, render_template, request, redirect, url_for 


app = Flask(__name__) 
# create global data variable
global_data = []

@app.route("/", methods=["GET"]) 
def home(): 
	return render_template('contact.html')

@app.route("/result", methods=["POST"]) 
def result(): 
	# append to data container
		
	

	data = [request.form['fullname'], request.form['email'], request.form['message']]
	global_data.append(data)
	#fullname = request.form['fullname']
	
	return render_template('result.html', data = data)

