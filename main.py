from flask import Flask, render_template, redirect, request
import os 
import sqlite3 

currentlocation = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/", methods=["POST"])
def checklogin():
    UN = request.form['username']
    PW = request.form['password']

    sqlconnection = sqlite3.Connection(currentlocation + "/users.db")
    cursor = sqlconnection.cursor()
    query1 = "SELECT username, password FROM users WHERE username ='{un}' AND password = '{pw}'".format(un = UN, pw = PW)

    rows = cursor.execute(query1)
    rows = rows.fetchall()
    if len(rows) ==1:
        return render_template("home.html")
    else:
        return redirect("/register")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST": 
         dUN = request.form['dusername']
         dPW = request.form['dpassword']
         sqlconnection = sqlite3.Connection(currentlocation + "/users.db")
         cursor = sqlconnection.cursor()
         query1 = "INSERT INTO users VALUES('{u}','{p}')".format(u=dUN, p=dPW)
         cursor.execute(query1)
         sqlconnection.commit()
         return redirect("/")
    return render_template("register.html")

@app.route('/home/')
def home():
    return render_template('home.html'), 200

@app.route('/o1/')
def o1():
    return render_template('choice1.html'), 200

@app.route('/choice1A')
def ch1A():
    return render_template('choice1A.html'), 200

@app.route('/ending1A')
def e1A():
    return render_template('ending1A.html'), 200

@app.route('/choice1B')
def ch1B():
    return render_template('choice1B.html'), 200 

@app.route('/ending1B')
def e1B():
    return render_template('ending1B.html'), 200 

@app.route('/choice1C')
def ch1C():
    return render_template('choice1C.html'), 200

@app.route('/ending1C')
def e1C():
    return render_template('ending1C.html'), 200

@app.route('/choice2A') 
def ch2A():
    return render_template('choice2A.html'), 200

@app.route('/ending2A')
def e2A():
    return render_template('ending2A.html'), 200

@app.route('/choice2B')
def ch2B():
    return render_template('choice2B.html'), 200

@app.route('/ending2B') 
def e2B():
    return render_template('ending2B.html'), 200

@app.route('/choice2C')
def ch2C():
    return render_template('choice2C.html'), 200 

@app.route('/ending2C')
def e2C(): 
    return render_template('ending2C.html'), 200

@app.route('/choice3A')
def ch3A():
    return render_template('choice3A.html'), 200

@app.route('/choice3B')
def ch3B():
    return render_template('choice3B.html'), 200

@app.route('/choice3C')
def ch3C():
    return render_template('choice3C.html'), 200

@app.route('/choice4A')
def ch4A():
    return render_template('choice4A.html'), 200

@app.route('/choice4B')
def ch4B():
    return render_template('choice4B.html'), 200

@app.route('/ending3A')
def e3A(): 
    return render_template('ending3A.html'), 200

@app.route('/ending3B')
def e3B():
    return render_template('ending3B.html'), 200

@app.route('/ending4A')
def e4A():
    return render_template('ending4A.html'), 200

@app.route('/ending4B')
def e4B():
    return render_template('ending4B.html'), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
