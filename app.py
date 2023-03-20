
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mysqldb import MySQL
import yaml

from yaml import FullLoader
from os import urandom
#import javascript

# Load the YAML file using FullLoader as the Loader argument
with open('db.yaml') as f:
    db = yaml.load(f, Loader=FullLoader)

app=Flask(__name__)
app.secret_key = urandom(24)
#db = yaml.load(open('templates/db.yaml'))

app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

if(mysql):
    print("hello")


@app.route('/show',methods=['GET', 'POST'])
def show():
   # return("hello world")
    
 #cur = mysql.connection.cursor()

      
 if request.method == 'POST':
        userDetails = request.form
        email = userDetails['email']
        pswd = userDetails['pswd']
        
        cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO professor(emp_id,email,emp_name,pswd) VALUES(%s, %s, %s, %s)",(num, email,name,pswd))
        resultValue=cur.execute("select * from student where email=%s",(email,) )
        #resultValue=cur.execute("SELECT s.stud_name, a.job_id, p.emp_name, t.activity, t.job_desc, a.sop, a.app_status FROM student s JOIN application a ON s.student_id = a.student_id AND a.app_status = 'Completed' JOIN total_job t ON a.job_id = t.job_id JOIN professor p ON t.emp_id = p.emp_id where s.email= %s",(email,))
        if resultValue > 0:
          userDetails = cur.fetchall()
          #return redirect('showprof.html')
          return render_template('show.html',userDetails=userDetails)
        mysql.connection.commit()
        cur.close()
      
    
 return render_template('loginstudent.html')


 
@app.route('/', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        num = userDetails['num']
        email = userDetails['email']
        name = userDetails['name']
        program = userDetails['program']
        depname = userDetails['depname']
        cpi = userDetails['cpi']
        pswd = userDetails['pswd']
        
        cur = mysql.connection.cursor()
        insert=cur.execute("INSERT INTO student(student_id, email,stud_name,program,dept_name,cpi,pswd) VALUES(%s, %s, %s, %s, %s, %s, %s)",(num, email,name,program,depname,cpi,pswd))
        if(insert):
            mysql.connection.commit()
            cur.close()
            return redirect('/show')
       
      
    return render_template('student.html')





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
     cpi = updatedata['cpi']
     pswd = updatedata['pswd']
     id=updatedata['id']
     print(id)
         #cur.execute("UPDATE table student(prgm,deptname,cpi,pswd) set VALUES(%s, %s, %s, %s)",(prgm, deptname,cpi,pswd))
     update=cur.execute("UPDATE student SET program=%s, dept_name=%s, cpi=%s, pswd=%s WHERE student_id=%s", (prgm, deptname, cpi, pswd,id))
     mysql.connection.commit()
     if(update):
      
        flash('updated succesfully','success')
        resultValue = cur.execute("Select * from student")
        if resultValue > 0:
                userDetails = cur.fetchall()
                return render_template('test.html',userDetails=userDetails)
          
        #return redirect('/test')
            #return redirect(url_for('test'))
        
    else:
     if 'delete' in request.form:
        cur = mysql.connection.cursor()
        deletedata = request.form
        id=deletedata['id']
        deptname = deletedata['deptname']
        cpi = deletedata['cpi']
        pswd = deletedata['pswd']
        cur.execute("DELETE FROM application WHERE student_id = %s", (id,))
        mysql.connection.commit()
        delete=cur.execute("delete  from student where student_id=%s",(id,))
        mysql.connection.commit()
       
        if(delete):
        
          resultValue = cur.execute("Select * from student")
          if resultValue > 0:
                userDetails = cur.fetchall()
                return render_template('test.html',userDetails=userDetails)
       
        
     
     else:
        resultValue = cur.execute("Select * from student")
        if resultValue > 0:
         userDetails = cur.fetchall()
         return render_template('test.html',userDetails=userDetails)
  
 else:
        return render_template('adminlogin.html')
    
        
      

     
@app.route('/prof', methods=['GET', 'POST'])
def prof():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        num = userDetails['num']
        email = userDetails['email']
        name = userDetails['name']
        pswd = userDetails['pswd']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO professor(emp_id,email,emp_name,pswd) VALUES(%s, %s, %s, %s)",(num, email,name,pswd))
        mysql.connection.commit()
        cur.close()
      
        return redirect('/loginprof')
       
      
    return render_template('prof.html')



@app.route('/showprof', methods=['GET', 'POST'])
def showprof():
  
   
   if request.method == 'POST':
        userDetails = request.form
        email = userDetails['email']
        pswd = userDetails['pswd']
        
        cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO professor(emp_id,email,emp_name,pswd) VALUES(%s, %s, %s, %s)",(num, email,name,pswd))
        #resultValue=cur.execute("select * from professor where email=%s",(email,) )
        resultValue=cur.execute("select t.job_id,  p.emp_name, t.emp_id, t.activity, t.job_desc, t.prereq, t.eligibility, t.total_jobs, t.duration, t.app_status from total_job t join professor p on p.emp_id=t.emp_id where email=%s",(email,))
        if resultValue > 0:
          userDetails = cur.fetchall()
          #return redirect('showprof.html')
          return render_template('showprof.html',userDetails=userDetails)
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
        cur.execute("SELECT * FROM student WHERE email=%s AND pswd=%s", (email, pswd))
        return redirect('/show')
     
 mysql.connection.commit()
 cur.close() 

 return render_template('loginstudent.html')



@app.route('/loginprof', methods=['GET', 'POST'])
def loginprof():
   # return("hello world")
    
 cur = mysql.connection.cursor()

 if request.method == 'POST':
     resultValue = cur.execute("Select * from professor")
     if resultValue > 0:
        userDetails = cur.fetchone()
        userDetails = request.form
        email = userDetails['email']
        pswd = userDetails['pswd']
        cur.execute("SELECT * FROM professor WHERE email=%s AND pswd=%s", (email, pswd))
        return redirect('/showprof')
     else:
        print("login or password is incorrect, please try again")
        return render_template('loginprof.html')
     
 mysql.connection.commit()
 cur.close() 

 return render_template('loginprof.html')
   


@app.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
 if request.method == 'POST':
        userDetails = request.form
        email = userDetails['email']
        pswd = userDetails['pswd']
        
        cur = mysql.connection.cursor()
        if (email=="jain01@gmail.com" and pswd=="12345"):
          #return redirect('showprof.html')
          mysql.connection.commit()
          cur.close()
          return redirect('/test')
        else:
           #return redirect('/message')
           return render_template('message.html')
        
        
 return render_template('adminlogin.html')
        


@app.route('/message', methods=['GET', 'POST'])
def message():
     
    
  return render_template('message.html')



@app.route('/rename')
def rename():
 
        cur=mysql.connection.cursor()
        val=cur.execute("alter table renamee RENAME TO rename_names")
        mysql.connection.commit()
        if(val):
            print("Table name is renamed")
            mysql.connection.commit()
       
        
      
    
  


if __name__=="__main__":
    app.run(debug=True)


