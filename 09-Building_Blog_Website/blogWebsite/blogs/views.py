from os import abort
from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from blogWebsite import db
from blogWebsite.models import BlogPost
from blogWebsite.blogs.forms import BlogPostForm

blogs = Blueprint('blogs', __name__, template_folder='templates/blogs')

# Create a blog post
@blogs.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = BlogPostForm()

    if form.validate_on_submit():
        blog_post = BlogPost(title=form.title.data, text=form.text.data, user_id=current_user.id)
        db.session.add(blog_post)
        db.session.commit()
        flash('Blog Post Created')
        return redirect(url_for('home.index'))

    return render_template('create_post.html', form=form)


# View blog post
@blogs.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog_post.html', title=blog_post.title, date=blog_post.date, post=blog_post)


# Update blog post
@blogs.route('/<int:blog_post_id>/update', methods=['GET', 'POST'])
@login_required
def update(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)

    form = BlogPostForm()
    if form.validate_on_submit():

        blog_post.title=form.title.data
        blog_post.text=form.text.data
        blog_post.user_id=current_user.id
        
        db.session.commit()
        flash('Blog Post Updated')
        return redirect(url_for('blogs.blog_post', blog_post_id=blog_post.id))
    
    elif request.method == 'GET':
        form.title.data = blog_post.title
        form.text.data = blog_post.text
    
    return render_template('create_post.html', title='Update', form=form)


# Delete blog post
@blogs.route('/<int:blog_post_id>/delete', methods=['POST'])
@login_required
def delete_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)

    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog Post Deleted')
    return redirect(url_for('home.index'))