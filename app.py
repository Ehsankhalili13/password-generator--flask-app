from gen.generate_password import *
from flask import Flask, flash, request, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = "ererlkjejt068957kj5ou646oi78"

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/process', methods=['POST'])
def process():
    field_value = request.form['field_value']  # دریافت مقدار از فرم
    
    if field_value.isdigit() == True :
        field_value = int(field_value) # successful
    
    mojaz = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]


    password_create = generate_password(field_value)

    flash(password_create)
    return redirect(url_for("home"))
    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")