from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/form-validation')
def User_Sign_Up_Form():
    return render_template('form.html')

def char_count(x):
    if len(x) > 2 and len(x) < 21:
        return True
    else:
        return False

def field_value(x):
    if x:
        return True
    else:
        return False


def email_symbol(x):
    if x.count('@') == 1:
        return True
    else:
        return False

def email_dot(x):
    if x.count('.') == 1:
        return True
    else:
        return False

@app.route('/form-validation', methods=['POST'])
def User_Sign_Up_Form_Complete():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""
    

    if not char_count(password):
        password_error = "This field must contain between 3 and 20 characters."
        password = ''
        verify_password = ''
        verify_password_error = "Please try entering your password again."

    elif not field_value(password):
        password_error = "This field cannot be blank."
        password = ''
        verify_password = ''

    else:
        if " " in password:
            password_error = "This field cannot contain spaces."
            password = ''
            verify_password = ''
            verify_password_error = "Please try entering your password again."

    if verify_password != password:
        verify_password_error = "Passwords don't match."
        password = ''
        verify_password = ''
        password_error = "Password don't match."

    if not field_value(username):
        username_error = "This field cannot be blank."
        password = ''
        verify_password = ''
        password_error = "Please try entering your password again."
        verify_password_error = "Please try entering your password again."

    elif not char_count(username):
        username_error = "This field must contain between 3 and 20 characters."
        password = ''
        verify_password = ''
        password_error = "Please try entering your password again."
        verify_password_error = "Please try entering your password again."

    else:
        if " " in username:
            username_error = "This field cannot contain spaces."
            password = ''
            verify_password = ''
            password_error = "Please try entering your password again."
            verify_password_error = "Please try entering your password again."

    if field_value(email):
        if not char_count(email):
            email_error = "This field must contain between 3 and 20 characters."
            password = ''
            verify_password = ''
            password_error = "Please try entering your password again."
            verify_password_error = "Please try entering your password again."

    
        elif not email_symbol(email):
            email_error = "Email address requires one @ symbol."
            password = ''
            verify_password = ''
            password_error = "Please try entering your password again."
            verify_password_error = "Please try entering your password again."

        elif not email_dot(email):
            email_error = "Email address requires one dot."
            password = ''
            verify_password = ''
            password_error = "Please try entering your password again."
            verify_password_error = "Please try entering your password again."

        else: 
            if " " in email:
                email_error = "This field cannot contain spaces."
                password = ''
                verify_password = ''
                password_error = "Please try entering your password again."
                verify_password_error = "Please try entering your password again."

    if not username_error and not password_error and not verify_password_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('form.html', username_error=username_error, username=username, password_error=password_error, password=password, verify_password_error=verify_password_error, verify_password=verify_password, email_error=email_error, email=email)

@app.route('/welcome')
def valid_User_Sign_Up_Form():
    username = request.args.get('username')
    return render_template("welcome.html", username=username)

app.run()










