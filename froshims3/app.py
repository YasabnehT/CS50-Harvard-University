import csv
import os
from os import path 
import smtplib
from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    name = request.args.get('name', 'world')
    return render_template('index.html', name = name)


@app.route('/register', methods = ['post'])
def register():
    """_summary_
    flask saves arguments coming via post in form 
    and those coming via get method inargs
    """
    
    name = request.form.get('name') 
    dorm = request.form.get('dorm')
    
    if not name or not dorm:
        return render_template('failure.html')
    file = open('registered.csv', 'a')
    writer = csv.writer(file)
    writer.writerow((name, dorm))
    file.close()
    return render_template('success.html')

@app.route('/registered', methods=['get'])
def registered():
    
    """file = open('registered.csv')
    reader =csv.reader(file)
    students = list(reader)
    file.close()"""
    
    with open('registered.csv','r') as file:
        reader = csv.reader(file)
        students = list(reader)
        
    return render_template('registered.html', students=students)




if __name__=="__main":
    app.run(debug=True)