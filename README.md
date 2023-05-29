# oCEO-flask-webapp
- A flask webapp for performing INSERT, UPDATE, DELETE, RENAME, WHERE operations in oCEO database
#### Assignment-4: [here](https://docs.google.com/document/d/1unkqi9Bnya8agH6RaStl4hAC0m7DIPNk5Yy5eTdskhM/edit#)
## Firstly download latest python version, its packages and flask framework shown below :-

  - Create a python virtual environment [Recommended]
     - Go to powershell(being in project directory) and follow the below steps :-
     1. Command: ```pip install virtualenv``` (enter)
     2. then type ```virtualenv env``` (enter)
        - Fig: a folder named "env" will be created[as shown] <br>
        ![Screenshot 2023-04-01 172523](https://user-images.githubusercontent.com/74257754/229287209-5862b91a-2410-4984-a727-67482836b840.png)
     3. Now, we have to activate this python virtual environment using command: ```.\env\Scripts\activate.ps1``` (press enter)
        - Fig: It will show something like this
        ![Screenshot 2023-04-01 172048](https://user-images.githubusercontent.com/74257754/229287002-89b92f89-0e6b-4692-9d5d-d0ddfbbdf944.png)

     2. install python packages(flask, pyyaml, flask-mysqldb) using command: ```pip install flask pyyaml flask-mysqldb``` (enter)
     3. Finally type command to run the flask-webapp: ```python .\app.py``` (press enter) 
        - Fig: Server got started[running on PORT shown]
        ![image](https://user-images.githubusercontent.com/74257754/229287434-1d1e95c6-d9a5-4a42-b937-77b3e1587e25.png)

### If you are getting an error, like this!!!
- sometime while activating python virtual env. we get an error as shown
![image](https://github.com/rahulraj22/oCEO-flask-webapp/assets/74257754/2c0c0587-51f1-4cbd-85e6-b9b370e3c098)

- to remove this, open ```windows powershell``` as ```admin``` and do as shown in Screenshot
![image](https://github.com/rahulraj22/oCEO-flask-webapp/assets/74257754/cd85954f-6818-4c1a-9e09-aca3c03e672b)

### Other way(if above steps not working) :-
  - install Flask(python web framework) using the commands as shown :
     - py -m pip install flask
  - Now, check their versions using command as shown :-
     - py -m flask --version
     - SS for the output :- <br>
     ![image](https://user-images.githubusercontent.com/74257754/226385040-edfc086c-b364-4c0c-8f2e-d2f041161926.png)
  - Then install following pip packages :-
     - pip3 install flask-mysqldb
     - pip3 install pyyaml <br>
## Open the oCEO-flask-webApp
  - command: python app.py (press enter)
  - then in terminal we get the ouput as shown in screenshot below <br>
  ![image](https://user-images.githubusercontent.com/74257754/226386377-c875f534-4847-48e4-ab30-3b5f8a21f2fd.png)
  - On clicking the default PORT(shown with arrow mark)[on clicking the link] : we will our app running and displays the homepage
## Home Page view:-
![image](https://user-images.githubusercontent.com/74257754/226375976-a54ba5f5-1a75-4816-bca7-37341dc47199.png)
  - On clicking the IITGN-logo, we get 3 options as follows:-
     - Login As Student
     - Login As Professor
     - Login As Admin
  - On clicking "Login As Student" we get the UI as shown :-
  ![image](https://user-images.githubusercontent.com/74257754/226418547-12e6a23d-cac9-4ab9-9e47-a9632bef4be5.png)
     - Login details of student(for registered student) i.e emailID and Password
  ![image](https://user-images.githubusercontent.com/74257754/226418715-55e2ce45-a952-4a78-b6aa-19d5dff262ff.png)
  - On clicking "Login As Professor" we get the UI as shown :-
  ![image](https://user-images.githubusercontent.com/74257754/226418780-3299b682-247c-467e-929c-c6a37fec989c.png)
  - On clicking "Login As Admin" we get the UI as shown :-
  ![Screenshot (726)](https://user-images.githubusercontent.com/74257754/226419187-e570d4b6-4c20-4724-a64d-470cdad65275.png)
  
## In MySQL, created database named "oceo" and tables as shown :-
![image](https://user-images.githubusercontent.com/74257754/226388745-921bac3e-78f7-4206-9199-a8894485bed3.png)

## These are the following commnads used for creating tables :-
  - Creating Student table
  ![image](https://user-images.githubusercontent.com/74257754/226392823-4a50df8e-2c25-4a66-88ba-f440dd5783b5.png)

  - Creating Professor table
  ![image](https://user-images.githubusercontent.com/74257754/226409383-14c7bc5c-98a3-42e8-92f4-4160aa58df5d.png)

  - Creating total_jobs table
  ![image](https://user-images.githubusercontent.com/74257754/226393820-240ff58d-dd8e-415f-86fd-5e23cd523c96.png)

  - Creating application table
  ![image](https://user-images.githubusercontent.com/74257754/226393974-3ff523b1-f5f4-429e-b1d2-e5c5bef2d55a.png)

  - Creating ongoing_jobs table
  ![image](https://user-images.githubusercontent.com/74257754/226394120-c8f38043-9a54-4c8d-b906-12905cab48e7.png)

  - Creating concluded_jobs table
  ![image](https://user-images.githubusercontent.com/74257754/226394275-32cfdc0c-959c-41dd-8654-73d098826ada.png)

  - Creating bank_details table
  ![image](https://user-images.githubusercontent.com/74257754/226394442-dd7c4e66-0203-43dd-b04c-6d7436f577fe.png)


# Working of all Operations shown below(with SS attached) :-

## RENAME Operation :-
![image](https://user-images.githubusercontent.com/74257754/226413056-698afb01-02bb-4cd7-9fcb-eed6aaec9d49.png)
- Same rename operation working on MySQL Workbench :-
![image](https://user-images.githubusercontent.com/74257754/226413320-698ad979-3b47-4cc2-a231-eb1aa5141bec.png)
   - RENAME queries

## SELECT with WHERE operation :-
- Professor login page
![image](https://user-images.githubusercontent.com/74257754/226416491-cd6d6c89-1758-4136-9045-91756aa98a05.png)
- Operation performed in MySQL workbench
![image](https://user-images.githubusercontent.com/74257754/226416782-bdcc6e4d-18ec-48f8-9e7b-7b7edbf7a699.png)
- Updated date get reflected in table shown
![image](https://user-images.githubusercontent.com/74257754/226416895-eba9b64c-c950-4bd2-addb-e9cea0ab5cad.png)

## UPDATE operation :-
![image](https://user-images.githubusercontent.com/74257754/226420882-f9e4b853-ea88-4d7f-9b0a-ab7ac5b9bbb9.png)
   - before update
![image](https://user-images.githubusercontent.com/74257754/226422038-7c4016ac-e679-4341-bae6-f146a5706010.png)
   - before update in schema
![image](https://user-images.githubusercontent.com/74257754/226422141-ca495ddf-b90d-41c1-9145-f8966cad36b1.png)
   - updated data in schema
![image](https://user-images.githubusercontent.com/74257754/226422259-d54baa7d-5273-425a-942f-456c9dad5844.png)
   - Alert dialog box to confirm the update operation
![image](https://user-images.githubusercontent.com/74257754/226422433-ebfcb0bf-1fb9-4ca0-a64d-1c2c7b313886.png)
   Dynamic execution in the frontEnd
## DELETE operation :-
![image](https://user-images.githubusercontent.com/74257754/226422575-90eb04ad-da30-4d84-aa4b-15978a943f4e.png)
   - Before delete operation
![image](https://user-images.githubusercontent.com/74257754/226422656-ddeeed14-7da4-43a6-b454-c518b87c2c70.png)
   - Before delete in schema(i.e MySQL workbench)
![image](https://user-images.githubusercontent.com/74257754/226422829-4bb090bc-62fa-4476-aa27-77440bc309cb.png)
   - Alert Box for confirming deletion operation
![image](https://user-images.githubusercontent.com/74257754/226423453-5e2954d1-ae78-4bdf-bf18-1d06b57190d7.png)
   - After delete operation from Schema(from MySQL workbench)
![image](https://user-images.githubusercontent.com/74257754/226423579-ee768e02-4ff9-48a4-be0e-09cf5a4a84c6.png)
   - deletion operation on table showing Dynamic Execution

## INSERT operation (for student Registration):-
![image](https://user-images.githubusercontent.com/74257754/226884307-5fb107ec-7330-414a-bda7-1a39b96b1308.png)
   - These data of student will be stored in student table in oceo database
![image](https://user-images.githubusercontent.com/74257754/226884890-bba78953-22b4-4c42-bd3a-73db29b92dfb.png)
   - Student will be prompted with "Student Login" page as shown below
![image](https://user-images.githubusercontent.com/74257754/226886297-3c41dd51-88d3-4372-88dd-dfb30455a22b.png)
   - The updated data can be viewed from mySQL Workbench

### Here are some of the dummy data used for testing our webApps shown below :-
![image](https://user-images.githubusercontent.com/74257754/226887015-83e72e26-c6f4-41e7-a470-6590dd0cc1b1.png)
![image](https://user-images.githubusercontent.com/74257754/226887039-261f59e9-2862-4a4f-a2a8-5dbddf07d8e2.png)
![image](https://user-images.githubusercontent.com/74257754/226887078-12b04652-03cb-4312-b976-f7fa3c1a1b1f.png)
![image](https://user-images.githubusercontent.com/74257754/226887121-005a9387-c097-41d9-bccc-9d17c9e1e595.png)


## If login details is wrong :-
![image](https://user-images.githubusercontent.com/74257754/226431207-3265b7ec-577e-45b1-a3cc-4676681aa8b0.png)

## About-Us page of oCEO database :-
<img width="1440" alt="Screenshot 2023-03-20 at 21 14 40" src="https://user-images.githubusercontent.com/74257754/226425049-ea839c15-7825-4b95-b85f-701871dea0ee.png">
## NavBar and Selection process in oCEO database :-
<img width="1440" alt="Screenshot 2023-03-20 at 21 15 30" src="https://user-images.githubusercontent.com/74257754/226425213-5366d970-7765-42fa-83df-95afd7eb8b0b.png">


#### Assignment - 3 | Contribution details : https://docs.google.com/document/d/1BiXMFtXF_6aI8bDtQSFaYC893RRDsi20zemd4p5jOqY/edit?usp=sharing
