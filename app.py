from flask import Flask, render_template, request, redirect, flash, url_for
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3309",
    user="root",
    passwd="root",
    database="crud_project"
 )

cursor = mydb.cursor()

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Set the secret key to some random bytes

@app.route('/')
def Index():
    sql = "SELECT * FROM employee_details where active = 1"
    cursor.execute(sql)
    data = cursor.fetchall()
    return render_template('index.html', students=data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        fname = request.form['firstname']
        lname = request.form['lastname']
        email = request.form['email']
        designation = request.form['designation']
        total_exp = request.form['total_exp']
        sql = "INSERT INTO employee_details (`first_name`, `last_name`, `designation`, `total_experiance`, `email`) VALUES (%s, %s, %s, %s, %s)"
        val = (fname, lname, designation, total_exp, email)
        cursor.execute(sql, val)
        mydb.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    sql = "update employee_details SET active = %s where id = %s"
    val = (0, id_data)
    cursor.execute(sql, val)
    mydb.commit()
    return redirect(url_for('Index'))

@app.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        fname = request.form['firstname']
        lname = request.form['lastname']
        email = request.form['email']
        designation = request.form['designation']
        total_exp = request.form['total_exp']
        sql = "update employee_details SET first_name = %s, last_name = %s, designation = %s, total_experiance = %s, email = %s where id = %s"
        val = (fname, lname, designation, total_exp, email, id_data)
        cursor.execute(sql, val)
        mydb.commit()
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
