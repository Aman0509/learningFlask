"""
- For this project you will create a very simple username requirements check website.
The user will type out a username, submit it, then the Flask application will check to see if the username passes 3 requirements.

- The user will type out a username, submit it, then the Flask application will check to see if the username passes 3 requirements.

- Requirements
    Username must contain a lowercase letter
    Username must contain an uppercase letter
    Username must end in a number

- 3 Template HTML Files
    Base with a NavBar with home Link.
    Index with a simple form that redirects to a “Report” page upon hitting submit.
    “Report” page that indicates if the username passed the requirements.

"""

from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("assignment_home.html")

@app.route('/report')
def report():
    start = time.time()
    username = request.args.get('username')
    temp = []
    if username == "":
        temp.append("No username was entered")
        passed = None
    else:
        if username.islower():
            temp.append("All letters are in lowercase")
            passed = False
        if username.isupper():
            temp.append("All letters are in uppercase")
            passed = False
        
        if not username[-1].isdigit():
            temp.append("Username does not ends with a number")
            passed = False
    if len(temp) == 0:
        passed = True
    end = time.time()

    return render_template("assignment_report.html", username=username, temp=temp, passed=passed, time=end-start)


if __name__ == "__main__":
    app.run(debug=True)

