from flask import Flask, render_template, request, redirect, url_for, session, flash
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
    if 'nama' in session:
        return render_template('dashboard.html', nama=session['nama'])
    else:
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login ():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request. form['password']
        cur = mysql.connection.cursor()
        cur.execute(f"select username, nama, password from tbl_users where username = '{username}'")
        user = cur.fetchone()
        cur.close()
        if user and pwd == user [2]:
            session ['nama'] = user[1]
            return redirect(url_for('Index'))
        else:
            return render_template('login.html',error='Invalid username or password')
    return render_template('login.html')


@app.route ('/insert', methods = ['POST'])
def insert():
    if request.method == "POST": 
        flash("Register Berhasil")
        nama = request.form ['nama']
        email = request.form ['email']
        username = request.form ['username']
        password = request.form ['password']
        
        cur = mysql.connection.cursor()
        cur.execute ("INSERT into tbl_users (nama, email, username, password) VALUES (%s, %s, %s, %s)", ( nama, email, username, password))
        mysql.connection.commit()
        return redirect(url_for('user'))

@app.route('/delete/<string:id_data>', methods = ['POST','PUT','DELETE'])
def delateuser(id_data):
    if(request.form['_method'] == 'PUT'):
        username = request.form['username']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM tbl_users WHERE id = %s", (id_data))
        mysql.connection.commit()
        cur.close()
        
        return redirect (url_for('user'))
    elif(request.form['_method'] == 'DELETE'):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM tbl_users WHERE id = %s", (id_data))
        mysql.connection.commit()
        cur.close()
        return redirect (url_for('user'))
    
@app.route ('/user')
def user ():

    cur = mysql.connection.cursor()
    cur.execute ("SELECT * From tbl_users")
    data =cur.fetchall()
    cur.close()
    return render_template('user.html', tbl_users = data, nama=session['nama'] )
    



@app.route ('/datatraining')
def datatraining ():
    return render_template('datatraining.html', nama=session['nama'])

@app.route ('/datatesting')
def datatesting():
    return render_template('datatesting.html', nama=session['nama'])

@app.route ('/dataklasifikasi')
def dataklasifikasi ():
    return render_template('dataklasifikasi.html', nama=session['nama'])

@app.route ('/klasifikasi')
def klasifikasi ():
    return render_template('klasifikasi.html')


if __name__ == "__main__":
    app.run(debug=True)


