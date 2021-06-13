from flask import render_template

def index():
    return "welcome To HomePage"

def index_temp():
    return render_template('index.html',name =  "Free AI")

def index_for():
    data = { 'Statistics' : 70 , 'Machine Learning': 50, 'Deep Learning' : 75, 'Python': 90 }
    return render_template('index_for.html',data = data)