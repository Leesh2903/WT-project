from flask import Flask, render_template, redirect, request
import os 
import sqlite3 

#used to get location of database
currentlocation = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

#root / login page
@app.route("/")
def login():
    return render_template("login.html")

#method used to create connection to database and access username + password
#request method is POST
@app.route("/", methods=["POST"])
def checklogin():
    #get username and password
    UN = request.form['username']
    PW = request.form['password']

    #establish connection
    sqlconnection = sqlite3.Connection(currentlocation + "/users.db")
    cursor = sqlconnection.cursor()
    #sql query 
    query1 = "SELECT username, password FROM users WHERE username ='{un}' AND password = '{pw}'".format(un = UN, pw = PW)

    rows = cursor.execute(query1)
    rows = rows.fetchall()
    #if record found return home page else redirect to register
    if len(rows) ==1:
        return render_template("home.html")
    else:
        return redirect("/register")

#method used to establish connection to database and create new users
@app.route("/register", methods=["GET","POST"])
def register():
    #request method is POST 
    if request.method == "POST": 
         dUN = request.form['dusername']
         dPW = request.form['dpassword']
         #connection to db
         sqlconnection = sqlite3.Connection(currentlocation + "/users.db")
         cursor = sqlconnection.cursor()
         #query to add new users
         query1 = "INSERT INTO users VALUES('{u}','{p}')".format(u=dUN, p=dPW)
         cursor.execute(query1)
         sqlconnection.commit()
         #returns login page
         return redirect("/")
     #return register page
    return render_template("register.html")

#home page route
@app.route('/home/')
def home():
    return render_template('home.html'), 200

#option 1 page route
@app.route('/o1/')
def o1():
    return render_template('choice1.html'), 200

#option 1 A page route
@app.route('/choice1A')
def ch1A():
    return render_template('choice1A.html'), 200

#ending 1A page route
@app.route('/ending1A')
def e1A():
    return render_template('ending1A.html'), 200

#choice 1B page route
@app.route('/choice1B')
def ch1B():
    return render_template('choice1B.html'), 200 

#ending 1B page route
@app.route('/ending1B')
def e1B():
    return render_template('ending1B.html'), 200 

#choice 1C page route
@app.route('/choice1C')
def ch1C():
    return render_template('choice1C.html'), 200

#ending 1C page route
@app.route('/ending1C')
def e1C():
    return render_template('ending1C.html'), 200

#choice 2A page route
@app.route('/choice2A') 
def ch2A():
    return render_template('choice2A.html'), 200

#ending 2A page route
@app.route('/ending2A')
def e2A():
    return render_template('ending2A.html'), 200

#choice 2B page route
@app.route('/choice2B')
def ch2B():
    return render_template('choice2B.html'), 200

#ending 2B page route
@app.route('/ending2B') 
def e2B():
    return render_template('ending2B.html'), 200

#choice 2C page route
@app.route('/choice2C')
def ch2C():
    return render_template('choice2C.html'), 200 

#ending 2C page route
@app.route('/ending2C')
def e2C(): 
    return render_template('ending2C.html'), 200

#choice 3A page route
@app.route('/choice3A')
def ch3A():
    return render_template('choice3A.html'), 200

#choice 3B page route
@app.route('/choice3B')
def ch3B():
    return render_template('choice3B.html'), 200

#choice 3C page route
@app.route('/choice3C')
def ch3C():
    return render_template('choice3C.html'), 200

#choice 4A page route
@app.route('/choice4A')
def ch4A():
    return render_template('choice4A.html'), 200

#choice 4B page route
@app.route('/choice4B')
def ch4B():
    return render_template('choice4B.html'), 200

#ending 3A page route
@app.route('/ending3A')
def e3A(): 
    return render_template('ending3A.html'), 200

#ending 3B page route
@app.route('/ending3B')
def e3B():
    return render_template('ending3B.html'), 200

#ending 4A page route
@app.route('/ending4A')
def e4A():
    return render_template('ending4A.html'), 200

#ending 4B page route
@app.route('/ending4B')
def e4B():
    return render_template('ending4B.html'), 200

#used to run web app.
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
