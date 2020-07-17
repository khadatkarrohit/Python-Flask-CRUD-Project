from flask import Flask, render_template, request, redirect
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

@app.route('/')
def Index():
    sql = "SELECT  * FROM employee_details"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    return render_template('index.html', students=data)


if __name__ == "__main__":
    app.run(debug=True)
