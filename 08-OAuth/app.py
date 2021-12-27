"""
OAuth
- You may not always want to deal with the responsibility of maintaining user profiles and authorization and registration.
- There are already many popular services that can be used as potential logins.
- Even popular services will use Facebook, Google, Twitter, etc. as login portals.
- We can use the flask-dance library to easily add in OAuth (Open Authorization) backends for our application.
- OAuth is an open-standard authorization protocol or framework that describes how unrelated servers and services can safely allow authenticated access to their assets without actually sharing the initial, related, single logon credential.

Flask Dance
- We will be working on top of the following “stack”
    OAuth 2.0
    Flask-OAuth
    Flask-Dance
- Flask-Dance library easily integrates a large variety of OAuth options. 
- More importantly, it has detailed QuickStart guides allowing you to easily implement any of these OAuth backends in your web app.
- Official flask-dance documentation: https://flask-dance.readthedocs.io/en/latest/
"""

from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

# As we don’t want to worry about setting up SSL now, let’s tell Requests-OAuthlib that it’s OK to use plain HTTP
# DO NOT leave this option enabled when running in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = "1"

blueprint = make_google_blueprint(client_id=os.environ['GOOGLE_CLIENT_ID'], client_secret=os.environ['GOOGLE_CLIENT_SECRET'], offline=True, scope=['profile', 'email'])
app.register_blueprint(blueprint, url_prefix='/login')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/welcome')
def welcome():
    # RETURN ERROR IF USER NOT LOGGED IN
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']
    return render_template("welcome.html", email=email)


@app.route('/login/google')
def login():
    if not google.authorized:
        return redirect(url_for('google.login'))
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']
    return render_template('welcome.html', email=email)


if __name__ == "__main__":
    app.run(debug=True)