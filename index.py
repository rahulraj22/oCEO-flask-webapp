from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

# lets initialize our flask app
app = Flask(__name__)

# Let's configure our database
db = yaml.full_load(open('db.yaml'))  # this will read the file named db.yaml to get all necessary details for connecting our database

# This db will store data in dictionary format(key-value pair)
# print(db) 

app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

# Now we will create routes for all necessary tables to fetch in our flask app

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        formDetails = request.form
        entityName = formDetails['student']
        operationName = formDetails['operName']

        # for student :-
        if(entityName == 'student'):
            # insert 
            if(operationName == 'insert'):
                return redirect('/student-insert')
            # update

            # delete

            # rename

            # where
        
        # for other entities
            # update
            # delete
            # rename
            # where
    return render_template('index.html')

# student | insert
@app.route('/student-insert', methods = ['GET', 'POST'])
def student_insert():
    if request.method == 'POST':
        formDetails = request.form
        studID = formDetails['id']
        studName = formDetails['name']
        studProg = formDetails['program']
        studDeptName = formDetails['dept_name']
        studEmail = formDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO student(student_id, name, program, dept_name, email) VALUES(%s, %s, %s, %s, %s)", (studID, studName, studProg, studDeptName, studEmail))
        mysql.connection.commit()
        cur.close()
        return redirect('/student-insert-commit')
    return render_template('student_insert.html')

# student | insert | commit(for changes)
@app.route('/student-insert-commit')
def student_insert_commit():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM student")
    if resultValue > 0:
        studentDetails = cur.fetchall()
        return render_template('student-insert-commit.html', students = studentDetails)




if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False, host='0.0.0.0') # for hosting in pythonanywhere.com








# @app.route('/')
# def oCEO_dbms():
#     return render_template('index.html')
