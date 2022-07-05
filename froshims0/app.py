import os
from os import path 
import smtplib
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

#students = [] # store students as list not db, v1

@app.route('/')
def index():
    name = request.args.get('name', 'world')
    return render_template('index.html', name = name)

"""
#v1
@app.route('/registrants', methods = ['post','get'])
def registrants():
    return render_template('registered.html', students = students)
"""

@app.route('/register', methods = ['post'])
def register():
    """_summary_
    flask saves arguments coming via post in form 
    and those coming via get method inargs
    """
    
    name = request.form.get('name') 
    email = request.form.get('email')
    dorm = request.form.get('dorm')
    if not name or not dorm or not email:
        return render_template('failure.html')
    
    message = 'You are registered!'
    
    server = smtplib.SMTP('smtp.gmail.com', 587) # 587 is tcp port
    server.starttls() # turn on encryption
    server.login('yastesh10@gmail.com', os.getenv('PASSWORD'))
    server.sendmail('yasabneh.teshager@gmail.com', email,message) # from, to , message
    return render_template('success.html')

    #students.append(f"{name} from {dorm}")  3for v1, lists
    #return redirect('success.html') # wqs for v0'
    #return redirect('/registrants') # v1







if __name__=="__main":
    app.run(debug=True)