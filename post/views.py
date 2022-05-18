from flask import render_template, redirect, url_for,flash,request


from flask_login import login_user, logout_user, login_required

from . import post

@post.route('/post/new', methods=['GET','POST'])
def new_post():
   
   
 return render_template('create_post.html')


@post.route('/post', methods=["GET","POST"])
def post_all():
    
     
    
    return render_template('post.html')
