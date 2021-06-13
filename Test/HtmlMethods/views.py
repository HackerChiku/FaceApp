from flask import render_template
from flask.globals import request


def index():
    if request.method == 'POST':
        first_name = request.form.get('first')
        last_name = request.form.get('last')
        email =     request.form.get('email')
        print(" first name = {} \n last name = {} \n email = {} ".format(first_name,last_name,email))

    return render_template('index.html')