from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("3_home.html")


@app.route('/signup')
def signup():
    """
    This view will render the simple signup page and after submitting the form, it will
    redirect to the thankyou page.
    """
    return render_template("3_signup.html")


@app.route('/thankyou')
def thankyou():
    """
    This view will render the thank you page after user will submit the form.
    It will receive the form data and display it on the page. In this case, user's
    first and last name.
    """
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template("3_thankyou.html", first=first, last=last)

@app.errorhandler(404)
def page_not_found(e):
    """
    Checkout the official docs at https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
    """
    return render_template("3_404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)