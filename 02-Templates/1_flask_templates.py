"""
Templates in Flask
- So far we’ve only returned back HTML manually through a Python string.
- Realistically we will want to connect a view function to render HTML templates (HTML files we’ve already created for a page)
- Flask will automatically look for HTML Templates in the templates directory.
- Later on we will discuss how to separate larger applications to have multiple template directories.
- We can render templates simply by importing the render_template function from flask and returning an .html file from our view function.

Templates Variables
- Using the render_template function we can directly render an HTML file with our Flask web app.
- But we haven’t leveraged the power of python at all yet!
- We want a way to be able to use Python code in our app, changing and updating variables and logic, and then send that information to the template.
- We can use the Jinja template engine to do this.
- Jinja templating will let us directly insert variables from our Python code to the HTML file.
- The syntax for inserting a variable is -> {{ variable_name }}
- We can pass in python strings, lists, dictionaries, and more into the templates.
- We set parameters (of our choosing) in the render_template function and then use the {{ }} syntax to insert them in the template.

Template Control Flow
- With Jinja templating we can pass variables using {{ variable }} syntax.
- We also have access to control flow syntax in our templates such as for loops and if statements.
- These use a {% %} syntax
- Imagine you passed a list variable to the HTML using template variables.
- Instead of displaying the entire list at once, we can display each item in the python list as a bulleted HTML list.

    <ul>
      {% for item in mylist %}
      <li> {{ item }} </li>
      {% endfor %}
    </ul>
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("1_basic.html")  # flask will look inside the dir 'templates' for 'basic.html'


@app.route('/var')
def temp_variable():
    var1 = "Hello World as string"
    var2 = ["Hello", "World", "as", "List"]
    var3 = {"Hello": "World"}
    var4 = ["Google", "Netflix", "Facebook", "Amazon", "Apple"]
    var5 = {"name": "john", "job": "IT"}
    return render_template("1_temp.html", var1=var1, var2=var2, var3=var3, var4=var4, var5=var5)


if __name__ == "__main__":
    app.run(debug=True)
