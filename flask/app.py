#importing Flask class from flask library
from flask import Flask, redirect, url_for, request

#creating an application instance
#the argument for the constructor is the main module name
#main module name will be the dunder __name__
app = Flask(__name__)

#defining a route in flask using the app.route decorator
#app is our flask application obj
#/ is the root of the website, like the default index.html
#greet() function will be executed when accessing default route
@app.route('/')
def greet():
    return 'Good Day!'

@app.route('/hello')
def hello():
    return '<h1>Hi Hello World!</h1>'

#demonstrate dymaic url building
@app.route('/admin')
def welcome_admin():
    return f'<h2>Welcome admin</h2>'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return f'<h2>Welcome {guest}, You are our guest </h2>'

@app.route('/user/<name>')
def user(name):
    if name == "admin":
        return redirect(url_for('welcome_admin'))
    else:
        return redirect(url_for("hello_guest", guest=name))


@app.route('/mylogin', methods=["POST"])
def mylogin():
    username = request.form['username']
    password = request.form['password']
    if username == 'Venky' and password == 'pass':
        return 'Welcome %s' %username
    else:
        return 'Username or password is not valid'


#check if its the main module, then run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)