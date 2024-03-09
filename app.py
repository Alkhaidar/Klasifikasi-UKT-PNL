from flask import Flask, render_template
app = Flask(__name__)

@app.route ('/')
def Index ():
    return render_template('dashboard.html')

@app.route ('/user')
def login ():
    return render_template('user.html')

@app.route ('/datatraining')
def datatraining ():
    return render_template('datatraining.html')

@app.route ('/datatesting')
def datatesting():
    return render_template('datatesting.html')

@app.route ('/dataklasifikasi')
def dataklasifikasi ():
    return render_template('dataklasifikasi.html')

@app.route ('/klasifikasi')
def klasifikasi ():
    return render_template('klasifikasi.html')

if __name__ == "__main__":
    app.run(debug=True)


