"""
Template Inheritance
- We know we can create view functions that directly link to an HTML template.
- But that still means we need to make an HTML template for every page.
- Usually pages across a web application already share a lot of features (e.g. navigation bar, footer, etc..)
- A great solution is template inheritance.
- We set up a base.html template file with the re-usable aspects of our site.
- Then we use {% extend “base.html” %} and {% block %} statements to extend these re-usable aspects to other pages.

- In this section, we will also briefly introduce filters.
- Filters are a great way to quickly change/edit a variable passed to a template.
- Syntax: {{ variable_name|filter_name }}
    For example:
        {{ name }}
        jose
        {{ name | capitalize }}
        Jose 

URL links with Templates
- Flask comes with a very convenient url_for() helper function that allows us to easily connect other template pages or files within our templates.

"""


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('2_home.html', user='testuser')

@app.route('/test')
def test():
    return render_template('2_test.html')

if __name__ == "__main__":
    app.run(debug=True)
