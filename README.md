# **Learn Flask**
## Introduction
Refer below link to start with the Flask.

*Note - Please feel free to contribute and add more insightful Flask related blogs and study materials links.*
- [Official Docs](https://flask.palletsprojects.com/en/2.0.x/tutorial/index.html)
- [GeeksforGeeks](https://www.geeksforgeeks.org/python-introduction-to-web-development-using-flask/)
- [FullStackPython](https://www.fullstackpython.com/flask.html)
- [Hello World](https://github.com/Aman0509/learningFlask/blob/main/01-Hello_World/helloWorld.py)

## [Templates](https://github.com/Aman0509/learningFlask/blob/main/02-Templates/)
- [Template basics, variables, control flow](https://github.com/Aman0509/learningFlask/blob/main/02-Templates/1_flask_templates.py)
- [Templates inheritance, url_for function](https://github.com/Aman0509/learningFlask/blob/main/02-Templates/2_flask_templates.py)
- [Templates forms](https://github.com/Aman0509/learningFlask/blob/main/02-Templates/3_flask_templates.py)
- [Assignment](https://github.com/Aman0509/learningFlask/blob/main/02-Templates/assignment.py)

## [Forms](https://github.com/Aman0509/learningFlask/blob/main/03-Forms/)
- [Forms basics](https://github.com/Aman0509/learningFlask/blob/main/03-Forms/1_flask_forms.py)
- [Forms fields](https://github.com/Aman0509/learningFlask/blob/main/03-Forms/2_flask_forms.py)
- [Flash alerts](https://github.com/Aman0509/learningFlask/blob/main/03-Forms/3_flask_forms.py)
- [Assignment](https://github.com/Aman0509/learningFlask/blob/main/03-Forms/assignment.py)

## [Databases with Flask](https://github.com/Aman0509/learningFlask/blob/main/04-Database/)
- [Introduction to SQLAlchemy ORM, Model Creation, Flask Migrate](https://github.com/Aman0509/learningFlask/blob/main/04-Database/flask_and_database.py)
- [Setting up the database](https://github.com/Aman0509/learningFlask/blob/main/04-Database/setup_database.py)
- [Demonstration of CRUD operations](https://github.com/Aman0509/learningFlask/blob/main/04-Database/crud.py)

## [Handling DB relationship with flask](https://github.com/Aman0509/learningFlask/blob/main/05-Flask_DB_Relationships/)
- [Creating model for demonstrating One to One and One to Many relationship](https://github.com/Aman0509/learningFlask/blob/main/05-Flask_DB_Relationships/models.py)
- [Performing CRUD operation on tables created based on above models](https://github.com/Aman0509/learningFlask/blob/main/05-Flask_DB_Relationships/crud.py)

## [Connecting flask views with DB](https://github.com/Aman0509/learningFlask/blob/main/06-Connecting_views_with_DB/)
- [Views and Models](https://github.com/Aman0509/learningFlask/blob/main/06-Connecting_views_with_DB/app.py)
- [Forms](https://github.com/Aman0509/learningFlask/blob/main/06-Connecting_views_with_DB/forms.py)

## Large Flask Applications
- For larger Flask applications, it makes more sense to separate portions of the application into their own files (models.py, forms.py, views.py)
- Forms, Views, Templates for each major component.

![image appflowchart](https://github.com/Aman0509/learningFlask/blob/main/others/flask_app_flow.png)

- We’ll be able to use the blueprints library to connect these separate modular components to our main app.py file.
- Flask has a built-in blueprints capability which will allow us to register modular components for our Flask App.
- This way we can easily reference a view for each component.
- Keep in mind, we’re still keeping app.py, it will just be referencing these sub-components.
- Below is the sample flask directory structure.
- For example, we’ll have 2 views.py files, one for 'owners' and one for 'puppies'.
- Each of these views.py will have their own add view.
- In order for our Flask application to not get confused for a /add route, we use blueprints
- The blueprints will register a url_prefix for each views.py file.
    - /owners/add
    - /puppies/add

Fig 1: Flask Project Structure
```
./testproject
├── app.py
├── requirements.txt
└── testproject
    ├── __init__.py
    ├── app1
    │   ├── forms.py
    │   ├── templates
    │   │   └── app1
    │   └── views.py
    ├── app2
    │   ├── forms.py
    │   ├── templates
    │   │   └── app2
    │   └── views.py
    ├── models.py
    ├── static
    └── templates
        ├── base.html
        └── home.html
```

## [User Authentication](https://github.com/Aman0509/learningFlask/blob/main/07-User_Authentication/)
- [Hashing Library](https://github.com/Aman0509/learningFlask/blob/main/07-User_Authentication/password_hashing.py)
- [Authentication Demo](https://github.com/Aman0509/learningFlask/tree/main/07-User_Authentication/flask_login_demo/)

## [OAuth Login with Flask-Dance](https://github.com/Aman0509/learningFlask/tree/main/08-OAuth)

---

## [startproject.py](https://github.com/Aman0509/learningFlask/blob/main/startproject.py)

This script will create the flask project with all the apps/components information.

### Usage

```
usage: startproject.py [-h] [-p TARGETPATH] projectname

Create a new Flask project.

positional arguments:
  projectname           The name of the project to create.

optional arguments:
  -h, --help            show this help message and exit
  -p TARGETPATH, --targetpath TARGETPATH
                        Path to the directory where the project will be created.
```
&nbsp;

**Use case 1:** By running this script like below, 'testproject' dir will be created which have structure as shown in Fig 1.

```
user@laptop % pwd
/home
user@laptop % python startproject.py testproject
user@laptop % ls
testproject
```
&nbsp;

**Use case 2:** By running this script like below, sub project dir name (where all flask apps/component will live) will be same as pwd directory name.

```
user@laptop % pwd
/home/testproject
user@laptop % python startproject.py .
user@laptop % ls
app.py			requirements.txt	testproject
```
&nbsp;

**Use case 3:** By running this script like below, flask project will be created at the given target path.

```
user@laptop % pwd
/home
user@laptop % python startproject.py testproject -p /opt/temp
user@laptop % ls /opt/temp
testproject
```
&nbsp;

***Note - Please contribute for features and enhancements.***

---

### References

- [Python and Flask Bootcamp: Create Websites using Flask! - Udemy](https://www.udemy.com/course/python-and-flask-bootcamp-create-websites-using-flask/)
- [Handling Forms in Flask with Flask-WTF](https://hackersandslackers.com/flask-wtforms-forms/)
- Implement OAuth2.0 Login for Flask app
  - [atrium.ai](https://atrium.ai/resources/how-to-implement-oauth-2-0-login-for-python-flask-web-server-applications/)
  - [toptal.com](https://www.toptal.com/flask/flask-login-tutorial-sso)
