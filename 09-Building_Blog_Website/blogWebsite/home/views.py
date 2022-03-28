from flask import Blueprint, render_template, redirect, url_for, request
from blogWebsite import db
from blogWebsite.models import BlogPost

home = Blueprint('home', __name__, template_folder='templates/home')

@home.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', blog_posts=blog_posts)

@home.route('/about')
def about():
    return render_template('about.html')