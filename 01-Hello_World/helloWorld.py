"""
Request Context Basics

- When your browser connects to a website, it includes a User-Agent field in its HTTP header. 
- The contents of the user agent field vary from browser to browser. 
- Each browser has its own, distinctive user agent. 
- A user agent is a way for a browser to identify what its using to visit the web app (safari on iphone vs chrome on laptop)
- The web server can use this information to serve different web pages to different web browsers and different operating systems.
- For example, a website could send mobile pages to mobile browsers, modern pages to modern browsers, and a “please upgrade your browser” message to Internet Explorer 6.
- The Web Server Gateway Interface (WSGI) is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language.
- When the Flask application handles a request, it creates a Request object based on the environment it received from the WSGI server. 
- Flask has a built-in request module that allows you to grab information about the visitor
- We won’t use this feature much in the beginning, but now is a good time to show what it is capable of.

"""

from flask import Flask

app = Flask(__name__)


# Basics
@app.route('/')
def index():
    return "<h1>Hello World!</h1>"


# Way to define routing in flask
@app.route('/info')
def info():
    return "<h1>This is info page</h1>"


# Dynamic Routing Example
@app.route('/page/<name>')
def page(name):
    return f"<h1>Welcome {name}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
