from flask import Flask, render_template
app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
