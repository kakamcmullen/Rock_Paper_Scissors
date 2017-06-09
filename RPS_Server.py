from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "password"

@app.route('/')
def hello_world():
    session["result"] = ""
    session["WIN"] = 0
    session["LOST"] = 0
    session["DRAWS"] = 0
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
    print request.form['name']
    z = random.randint(1, 3)
    print z
    y = request.form['name']
    if str(z) == y:
        session["result"] = "DRAW"
        session["DRAWS"] += 1
    elif z == 1:
        if y == "2":
            session["result"] = "WIN"
            session["WIN"] += 1
        else:
           session["result"] = "LOST"
           session["LOST"] += 1 
    elif z == 2:
        if y == "3":
            session["result"] = "WIN"
            session["WIN"] += 1
        else:
           session["result"] = "LOST"
           session["LOST"] += 1    
    elif z == 3:
        if y == "1":
            session["result"] = "WIN"
            session["WIN"] += 1
        else:
           session["result"] = "LOST"
           session["LOST"] += 1
    print session["result"]
#    return redirect ('/')
    return render_template('index.html')



app.run(debug=True)
