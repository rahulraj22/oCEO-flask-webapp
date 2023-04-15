from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mysqldb import MySQL
import yaml

from yaml import FullLoader
from os import urandom
# import javascript

# Load the YAML file using FullLoader as the Loader argument
with open('db.yaml') as f:
    db = yaml.load(f, Loader=FullLoader)

app = Flask(__name__)
app.secret_key = urandom(24)
# db = yaml.load(open('templates/db.yaml'))

app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

# if(mysql):
#     print("hello")


@app.route('/', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        userDetails = request.form
        if userDetails['action'] == 'Register':
            # Fetch form data
            num = userDetails['num']
            email = userDetails['email']
            name = userDetails['name']
            program = userDetails['program']
            depname = userDetails['depname']
            cpi = userDetails['cpi']
            pswd = userDetails['pswd']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO student(student_id, email,stud_name,program,dept_name,cpi,pswd) VALUES(%s, %s, %s, %s, %s, %s, %s)",
                        (num, email, name, program, depname, cpi, pswd))
            mysql.connection.commit()
            cur.close()
            return redirect('/show')
        elif userDetails['action'] == 'Sign-In':
            return redirect('/show')
        elif userDetails['action'] == 'Admin-Sign-In':
            return redirect('/test')
        elif userDetails['action'] == 'Prof-Register':
            return redirect('/prof')

    # elif request.method == 'POST' and userDetails['num'] == '':
    #     return redirect('/show')

    return render_template('student.html')


@app.route('/show', methods=['GET', 'POST'])
def show():
   # return("hello world")

    # cur = mysql.connection.cursor()

    if request.method == 'POST':
        userDetails = request.form
        email = userDetails['email']
        pswd = userDetails['pswd']

        cur = mysql.connection.cursor()
        # cur.execute("INSERT INTO professor(emp_id,email,emp_name,pswd) VALUES(%s, %s, %s, %s)",(num, email,name,pswd))
        resultValue = cur.execute(
            "select * from student where email=%s", (email,))
        # resultValue=cur.execute("SELECT s.stud_name, a.job_id, p.emp_name, t.activity, t.job_desc, a.sop, a.app_status FROM student s JOIN application a ON s.student_id = a.student_id AND a.app_status = 'Completed' JOIN total_job t ON a.job_id = t.job_id JOIN professor p ON t.emp_id = p.emp_id where s.email= %s",(email,))
        if resultValue > 0:
            userDetails = cur.fetchall()
            # return redirect('showprof.html')
            return render_template('show.html', userDetails=userDetails)
        else:
            return render_template('message.html')
        mysql.connection.commit()
        cur.close()

    return render_template('loginstudent.html')


# Sign-in as Admin
@app.route('/test', methods=['GET', 'POST'])
def test():
   # return("hello world")

    cur = mysql.connection.cursor()

    if request.method == 'POST':
        if 'update' in request.form:
            cur = mysql.connection.cursor()
            updatedata = request.form
            prgm = updatedata['prgm']
            print(prgm)
            deptname = updatedata['deptname']
            # cpi = updatedata['cpi']
            # pswd = updatedata['pswd']
            id = updatedata['id']
            print(id)
            # cur.execute("UPDATE table student(prgm,deptname,cpi,pswd) set VALUES(%s, %s, %s, %s)",(prgm, deptname,cpi,pswd))
            cur.execute("UPDATE student SET program=%s, dept_name=%s WHERE student_id=%s", (prgm, deptname, id))
            mysql.connection.commit()
            flash('updated succesfully', 'success')
            resultValue = cur.execute("Select * from student")
            if resultValue > 0:
                userDetails = cur.fetchall()
                return render_template('test.html', userDetails=userDetails)

                # return redirect('/test')
            # return redirect(url_for('test'))

        else:
            if 'delete' in request.form:
                cur = mysql.connection.cursor()
                deletedata = request.form
                id = deletedata['id']
                deptname = deletedata['deptname']
                # cpi = deletedata['cpi']
                # pswd = deletedata['pswd']
                cur.execute(
                    "DELETE FROM application WHERE student_id = %s", (id,))
                mysql.connection.commit()
                delete = cur.execute(
                    "delete  from student where student_id=%s", (id,))
                mysql.connection.commit()

                if (delete):

                    resultValue = cur.execute("Select * from student")
                    if resultValue > 0:
                        userDetails = cur.fetchall()
                        return render_template('test.html', userDetails=userDetails)

            else:
                resultValue = cur.execute("Select * from student")
                if resultValue > 0:
                    userDetails = cur.fetchall()
                    return render_template('test.html', userDetails=userDetails)
    
    else:
        return render_template('adminlogin.html')


# After clicking register as prof.
@app.route('/prof', methods=['GET', 'POST'])
def prof():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        if userDetails['action'] == 'Register':
            num = userDetails['num']
            email = userDetails['email']
            name = userDetails['name']
            pswd = userDetails['pswd']

            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO professor(emp_id,email,emp_name,pswd) VALUES(%s, %s, %s, %s)", (num, email, name, pswd))
            mysql.connection.commit()
            cur.close()
            userDetails = cur.fetchall()
            return render_template('showRegProf.html', userDetails = userDetails)
        else:  # if professor want to login [already registered]
            return redirect('/loginprof')

    return render_template('prof.html')


@app.route('/loginprof', methods=['GET', 'POST'])
def loginprof():
    # return("hello world")

    cur = mysql.connection.cursor()

    if request.method == 'POST':
        # resultValue = cur.execute("Select * from professor")
        profDetails = request.form
        profEmail = profDetails['email']
        profPaswd = profDetails['pswd']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM professor WHERE email = %s AND pswd = %s', (profEmail, profPaswd))
        userDetails = cur.fetchall()
        if userDetails:
            # userDetails = request.form
            # email = userDetails['email']
            # pswd = userDetails['pswd']
            # cur.execute(
            #     "SELECT * FROM professor WHERE email=%s AND pswd=%s", (email, pswd))
            # return redirect('/showprof')
            if profDetails['login'] == "Check Professor's Feedback":
                cur.execute('select student_id, email, stud_name, program, dept_name, prof_feedback from student')
                studentDetails = cur.fetchall()
                return render_template('proffeedback.html', studentDetails = studentDetails)
            else:
                cur.execute('SELECT emp_id, email, emp_name FROM professor')
                allProfDetails = cur.fetchall()
                return render_template('showRegProf.html', userDetails = userDetails, allProfDetails = allProfDetails)
        else:
            # print("login or password is incorrect, please try again")
            return render_template('message.html')
            # return render_template('loginprof.html')

    mysql.connection.commit()
    cur.close()

    return render_template('loginprof.html')

# update operation done by professor
@app.route('/update/<int:sno>', methods = ['GET', 'POST'])
def update(sno):
    cur = mysql.connection.cursor()
    cur.execute('select prof_feedback from student where student_id = %s', (sno, ))
    feedbackData = cur.fetchone()
    return render_template('updateProfMessage.html', feedbackData = feedbackData)

@app.route('/delete/<int:sno>', methods = ['GET', 'POST'])
def delete(sno):
    cur = mysql.connection.cursor()
    cur.execute('delete from student where student_id = %s', (sno,))
    
    # show an alert message to the user using the flash method
    flash('Record deleted successfully!', 'success')
    
    cur.execute('select student_id, email, stud_name, program, dept_name, prof_feedback from student')
    studentDetails = cur.fetchall()
    return render_template('proffeedback.html', studentDetails = studentDetails)


@app.route('/showprof', methods=['GET', 'POST'])
def showprof():

    if request.method == 'POST':
        userDetails = request.form
        email = userDetails['email']
        pswd = userDetails['pswd']

        cur = mysql.connection.cursor()
        # cur.execute("INSERT INTO professor(emp_id,email,emp_name,pswd) VALUES(%s, %s, %s, %s)",(num, email,name,pswd))
        # resultValue=cur.execute("select * from professor where email=%s",(email,) )
        resultValue = cur.execute(
            "select t.job_id,  p.emp_name, t.emp_id, t.activity, t.job_desc, t.prereq, t.eligibility, t.total_jobs, t.duration, t.app_status from total_job t join professor p on p.emp_id=t.emp_id where email=%s", (email,))
        if resultValue > 0:
            userDetails = cur.fetchall()
            # return redirect('showprof.html')
            return render_template('showprof.html', userDetails=userDetails)
        mysql.connection.commit()
        cur.close()

    return render_template('loginprof.html')

    # return redirect('/test.html')


@app.route('/loginstudent', methods=['GET', 'POST'])
def loginstudent():
    # return("hello world")

    cur = mysql.connection.cursor()

    if request.method == 'POST':
        resultValue = cur.execute("Select * from student")
        if resultValue > 0:
            userDetails = cur.fetchone()
            userDetails = request.form
            email = userDetails['email']
            pswd = userDetails['pswd']
            cur.execute(
                "SELECT * FROM student WHERE email=%s AND pswd=%s", (email, pswd))
            return redirect('/show')

    mysql.connection.commit()
    cur.close()

    return render_template('loginstudent.html')



@app.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        userDetails = request.form
        email = userDetails['email']
        pswd = userDetails['pswd']

        cur = mysql.connection.cursor()
        if (email == "jain01@gmail.com" and pswd == "12345"):
            # return redirect('showprof.html')
            mysql.connection.commit()
            cur.close()
            return redirect('/test')
        else:
            # return redirect('/message')
            return render_template('message.html')

    return render_template('adminlogin.html')


@app.route('/message', methods=['GET', 'POST'])
def message():

    return render_template('message.html')


@app.route('/rename')
def rename():

    cur = mysql.connection.cursor()
    val = cur.execute("alter table renamee RENAME TO rename_names")
    mysql.connection.commit()
    if (val):
        print("Table name is renamed")
        mysql.connection.commit()


# for nav bar
@app.route('/aboutus')
def about():
    return render_template('about.html')  # about us page

@app.route('/whatwedo')
def whatwedo():
    return render_template('index.html')

@app.route('/jobopenings')
def oceo_positions():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM oceo_positions')
    userDetails = cur.fetchall()
    return render_template('showprof.html', userDetails = userDetails)


@app.route('/proffeedback')
def profFeedback():
    cur = mysql.connection.cursor()
    cur.execute('select student_id, email, stud_name, program, dept_name, prof_feedback from student')
    studentDetails = cur.fetchall()
    # return render_template('proffeedback.html', studentDetails = studentDetails)
    return redirect('/prof')


if __name__ == "__main__":
    app.run(debug=True)
