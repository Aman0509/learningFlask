import os, sys, time
import argparse


def create_file(name, mode_type="w", content=""):
    """Create a file at the specified path."""

    with open(name, mode_type) as f:
        f.write(content)


def create_dir(name, perm=0o755):
    """Create a directory at the specified path."""

    os.makedirs(name, perm)


def create_app(app_dict, project_name):
    """Create flask apps or components at the specified path."""

    forms_file_content = '''from flask_wtf import FlaskForm'''

    for app_name, app_path in app_dict.items():
        
        views_file_content = f"from flask import Blueprint, render_template, redirect, url_for\nfrom {project_name} import db\n\n{app_name} = Blueprint('{app_name}', __name__, template_folder='templates/{app_name}')"

        create_dir(app_path)
        create_file(os.path.join(app_path, '__init__.py'))
        create_file(os.path.join(app_path, 'forms.py'), content=forms_file_content)
        create_file(os.path.join(app_path, 'views.py'), content=views_file_content)
        create_dir(os.path.join(app_path+'/templates/', app_name))


def create_project_dir(path):
    """Create a project directory at the specified path."""

    try:
        app_dict = dict()
        temp_str1, temp_str2 = "", ""
        project_root_path = os.path.split(path)[0]
        project_name = os.path.split(path)[-1]

        app_file_content = f"from {project_name} import app\nfrom flask import render_template\n\n@app.route('/')\ndef index():\n\treturn render_template('home.html')\n\nif __name__ == '__main__':\n\tapp.run(debug=True)"
        init_file_content = '''from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

'''
    
        base_html_file_content = '''<!-- Base HTML -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title></title>
</head>
<body>

    <nav class="navbar navbar-light bg-light">
        <div class="container-fluid">
            <span class="navbar-text">
                <a href="{{ url_for('index')}}" class="navbar-brand">Home</a>
            </span>
        </div>
    </nav>
    <br><br><br>
    
    {% block content %}
        
    {% endblock %}
    
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

</body>
</html>
'''
        home_html_file_content = '''{% extends 'base.html' %}


{% block content %}
    <div class="jumbotron">
        <div class="contain">
            <h1 class="display-4">Welcome</h1>
            <p class="display-4">Enjoy building with Flask :)</p>
        </div>
    </div>
{% endblock content %}
'''
        handlers_file_content = '''from flask import Blueprint, render_template


error_pages = Blueprint('error_pages', __name__)

@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html'), 404

'''

        handlers_html_file_content = '''{% extends 'base.html' %}
{% block content %}
    <div class="jumbotron">
        <div class="container">
            <h1 class="display-4">404: PAGE NOT FOUND</h1>
        </div>
    </div>
{% endblock content %}
'''

        models_file_content = f"from {project_name} import db"
        
        # create the project directory
        if not os.path.exists(project_root_path):
            create_dir(project_root_path, perm=0o766)

        # create project root level files
        create_file(os.path.join(project_root_path, 'app.py'), content=app_file_content)
        create_file(os.path.join(project_root_path, 'requirements.txt'))
        
        # create project sub-directory level files
        create_dir(os.path.join(path, 'static'))
        create_dir(os.path.join(path, 'templates/error_pages'))  # create dirs 'templates' and 'error_pages'
        create_dir(os.path.join(path, 'error_pages'))
        create_file(os.path.join(path, '__init__.py'), content=init_file_content)
        create_file(os.path.join(path, 'models.py'), content=models_file_content)
        create_file(os.path.join(path+'/error_pages', 'handlers.py'), content=handlers_file_content)
        create_file(os.path.join(path+'/templates/', 'base.html'), content=base_html_file_content)
        create_file(os.path.join(path+'/templates/', 'home.html'), content=home_html_file_content)
        create_file(os.path.join(path+'/templates/error_pages/', '404.html'), content=handlers_html_file_content)

        num_of_apps = input('How many apps/components do you want to create? ')
        if num_of_apps != "" and int(num_of_apps) > 0:
            for i in range(int(num_of_apps)):
                app_name = input(f'Enter {i+1} app name: ')
                if app_name != '':
                    temp_str1 += f"\nfrom {os.path.split(path)[-1]}.{app_name}.views import {app_name}"
                    temp_str2 += f"\napp.register_blueprint({app_name}, url_prefix='/{app_name}')"
                    app_path = os.path.join(path, app_name)
                    app_dict[app_name] = app_path
            temp_str1 += f"\nfrom {os.path.split(path)[-1]}.error_pages.handlers import error_pages"
            temp_str2 += f"\napp.register_blueprint(error_pages)"
            temp_str = temp_str1+'\n'+temp_str2
            create_file(os.path.join(path, '__init__.py'), mode_type="a" ,content=temp_str)
            create_app(app_dict, os.path.split(path)[-1])
        else:
            print('No apps/components created as no input provided.')
        return 0
    except Exception as exception:
        print("Exception: {}".format(type(exception).__name__))
        print("Exception message: {}".format(exception))
        return 1


if __name__ == "__main__":

    path = ""
    project_name = ""
    parser = argparse.ArgumentParser(description="Create a new Flask project.")
    parser.add_argument('projectname', help="The name of the project to create.")
    parser.add_argument('-p','--targetpath', help="Path to the directory where the project will be created.")
    args = parser.parse_args()

    # Handling the arguments passed during the execution of the script
    if args.targetpath:
        if os.path.exists(args.targetpath):
            if args.projectname != ".":
                project_name = args.projectname
                path = os.path.join(args.targetpath, args.projectname+"/"+args.projectname)
            else:
                sys.exit("'.' is not a valid project name.")
        else:
            sys.exit("The target path does not exist. Please check the path and try again.")
    else:
        if args.projectname == ".":
            project_name = os.path.split(os.getcwd())[-1]
            path = os.getcwd()+"/"+project_name
        else:
            path = os.path.join(os.getcwd(), args.projectname+"/"+args.projectname)
    start = time.perf_counter()
    exit_code = create_project_dir(path)
    stop = time.perf_counter()
    print()
    print("="*100)
    print("Execution time: {} seconds".format(stop-start))
    if exit_code:
        sys.exit("[ERROR]: Exit Code 1 - Project creation failed.")
    else:
        sys.exit(f"[INFO]: Exit Code 0 - Project '{project_name}' created successfully at '{os.path.split(path)[0]}'")
