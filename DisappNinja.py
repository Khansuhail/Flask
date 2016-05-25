from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app, and import                                         # render_template to allow us to render index.html.
app = Flask(__name__) 
app.secret_key = 'ThisIsSecret'


@app.route('/', methods=['GET'])                           # The "@" symbol designates a "decorator" which attaches the                                         # following function to the '/' route. This means that                                         # whenever we send a request to localhost:5000/ we will run                                         # the following "hello_world" function.
def home():
  return render_template('noninjas.html')

@app.route('/ninja', methods=['GET'])                           # The "@" symbol designates a "decorator" which attaches the                                         # following function to the '/' route. This means that                                         # whenever we send a request to localhost:5000/ we will run                                         # the following "hello_world" function.
def allninjas():
  return render_template('allninjas.html')

@app.route('/ninja/blue', methods=['GET'])                           # The "@" symbol designates a "decorator" which attaches the                                         # following function to the '/' route. This means that                                         # whenever we send a request to localhost:5000/ we will run                                         # the following "hello_world" function.
def ninja_blue():
   return render_template('leonardo.html')

@app.route('/ninja/orange', methods=['GET'])                           # The "@" symbol designates a "decorator" which attaches the                                         # following function to the '/' route. This means that                                         # whenever we send a request to localhost:5000/ we will run                                         # the following "hello_world" function.
def ninja_orange():
   return render_template('michelangelo.html')

@app.route('/ninja/red', methods=['GET'])                           # The "@" symbol designates a "decorator" which attaches the                                         # following function to the '/' route. This means that                                         # whenever we send a request to localhost:5000/ we will run                                         # the following "hello_world" function.
def ninja_red():
   return render_template('raphael.html')

@app.route('/ninja/purple', methods=['GET'])                           # The "@" symbol designates a "decorator" which attaches the                                         # following function to the '/' route. This means that                                         # whenever we send a request to localhost:5000/ we will run                                         # the following "hello_world" function.
def ninja_purple():
   return render_template('donatello.html')

@app.route('/ninja/123')                           # The "@" symbol designates a "decorator" which attaches the                                         # following function to the '/' route. This means that                                         # whenever we send a request to localhost:5000/ we will run                                         # the following "hello_world" function.
def megan_fox():
    return render_template('notapril.html')

@app.route('/ninja/black', methods=['GET'])                           # The "@" symbol designates a "decorator" which attaches the                                         # following function to the '/' route. This means that                                         # whenever we send a request to localhost:5000/ we will run                                         # the following "hello_world" function.
def fox_megan():
	return render_template('notapril.html')



app.run(debug=True)