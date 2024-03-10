from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key= 'your-secret-key'


#Meghubungkan Mysql
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'klasifikasi'

mysql = MySQL(app)


@app.route ('/')
def Index ():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login ():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request. form['password']
        cur = mysql.connection.cursor()
        cur.execute(f"select username, password from tbl_users where username = '{username}'")
        user = cur.fetchone()
        cur.close()
        if user and pwd == user [1]:
            session ['username'] = user[0]
            return redirect(url_for('Index'))
        else:
            return render_template('login.html',error='Invalid username or password')
    return render_template('login.html')


@app.route ('/user')
def user ():
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


