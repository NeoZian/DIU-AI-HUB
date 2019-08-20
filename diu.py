from flask import Flask, render_template, request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mysqldb import MySQL
import MySQLdb
from flask_mail import Mail
import json
from datetime import datetime



from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
# from werkzeug import secure_filename
from werkzeug import secure_filename
from werkzeug.utils import secure_filename

from flask_mail import Mail
import json
import os
import math
from datetime import datetime






with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True






# from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap
import pandas as pd
import numpy as np

# ML Packages
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib




app = Flask(__name__)
app.secret_key='super-secret-key'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/diu'
db = SQLAlchemy(app)



conn = MySQLdb.connect(host="localhost",user="root",password="",db="diu")



Bootstrap(app)


class Visitor(db.Model):
    '''
    id,name,email.message
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    # phone_num = db.Column(db.String(12), nullable=False)

    # date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)
    message = db.Column(db.String(120), nullable=False)

class Users(db.Model):
    '''
    id,full_name,email,phone,job,password
    '''
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone= db.Column(db.String(20), nullable=False)
    job= db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(50), nullable=False)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    tagline = db.Column(db.String(120), nullable=False)
    img_file = db.Column(db.String(12), nullable=True)
    date = db.Column(db.String(12), nullable=True)







@app.route("/", methods = ['GET', 'POST'])
def home():
	# def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        # phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Visitor(name=name,email = email,message=message )
        db.session.add(entry)
        db.session.commit()

    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')


#
# @app.route("/login",methods = ['GET','POST'])
# def login():
#     if(request.method=='POST'):
#         return render_template('login.html')
#     elif(request.method=='GET'):
#         return render_template('login.html')


@app.route("/signup", methods = ['GET', 'POST'])
def signUp():

	if(request.method=='POST'):
		name = request.form.get('full_name')
		email = request.form.get('email')
		phone = request.form.get('phone')
		job = request.form.get('job')
		password = request.form.get('password')


		entry = Users(full_name = name, email = email,phone=phone, job = job, password = password)
		db.session.add(entry)
		db.session.commit()
		return render_template('login.html')



	return render_template('signup.html')

@app.route("/mydash")
def mdash():
     return render_template('dashboard.html')


@app.route("/checkUser",methods = ['GET','POST'])
def check():


    if(request.method=='GET'):
        posts = Posts.query.filter_by().all()
        last = math.ceil(len(posts)/int(params['no_of_posts']))
        #[0: params['no_of_posts']]
        #posts = posts[]
        page = request.args.get('page')
        if(not str(page).isnumeric()):
            page = 1
        page= int(page)
        posts = posts[(page-1)*int(params['no_of_posts']): (page-1)*int(params['no_of_posts'])+ int(params['no_of_posts'])]
        #Pagination Logic
        #First
        if (page==1):
            prev = "#"
            next = "?page="+ str(page+1)
        elif(page==last):
            prev = "?page=" + str(page - 1)
            next = "#"
        else:
            prev = "?page=" + str(page - 1)
            next = "?page=" + str(page + 1)
        return render_template('index_blog.html', params=params, posts=posts,prev=prev, next=next)


    if(request.method=='POST'):
        posts = Posts.query.filter_by().all()[0:params['no_of_posts']]

        email = str(request.form["email"])
        password = str(request.form["password"])
        #
        # if ('user' in session and session['user'] == params['admin_user']):
        #     posts = Posts.query.all()
        #     return render_template('dashboard.html', params=params, posts = posts)

        if (email == params['admin_user'] and password == params['admin_password']):
            #set the session variable
            session['user'] = email
            posts = Posts.query.all()
            visitor=Visitor.query.all()
            return render_template('dashboard.html', params=params, posts = posts,visitor=visitor)

             # return render_template('login.html', params=params)




        cursor = conn.cursor()
        cursor.execute("SELECT email FROM users WHERE email ='"+email+"' AND password ='"+password+"' ")
        user = cursor.fetchone()

        try:
            if len(user) is 1:
                return render_template('index_blog.html', params=params, posts=posts)
        except:
            flash('Login Failed', 'danger')
            return render_template('login.html')




@app.route("/checkUser/ueditd")
def ueditt():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['no_of_posts']))
    #[0: params['no_of_posts']]
    #posts = posts[]
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page= int(page)
    posts = posts[(page-1)*int(params['no_of_posts']): (page-1)*int(params['no_of_posts'])+ int(params['no_of_posts'])]
    #Pagination Logic
    #First
    if (page==1):
        prev = "#"
        next = "?page="+ str(page+1)
    elif(page==last):
        prev = "?page=" + str(page - 1)
        next = "#"
    else:
        prev = "?page=" + str(page - 1)
        next = "?page=" + str(page + 1)
    return render_template('index_blog.html', params=params, posts=posts,prev=prev, next=next)





@app.route("/checkUser/uedit/<string:sno>", methods = ['GET', 'POST'])
def Uedit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()

            if sno=='0':
                post = Posts(title=box_title, slug=slug, content=content, tagline=tline, img_file=img_file, date=date)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = box_title
                post.slug = slug
                post.content = content
                post.tagline = tline
                post.img_file = img_file
                post.date = date
                db.session.commit()
                return redirect('/checkUser/uedit/'+sno)
        post = Posts.query.filter_by(sno=sno).first()
        return render_template('uedit.html', params=params, post=post, sno=sno)






@app.route("/checkUser/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)




@app.route("/checkUser/dash")
def dash():
    posts = Posts.query.all()
    visitor=Visitor.query.all()
    return render_template('dashboard.html', params=params, posts = posts,visitor=visitor)




#
#
# @app.route("/checkUser/dashboard", methods=['GET', 'POST'])
# def dashboard():
#
#     if ('user' in session and session['user'] == params['admin_user']):
#         posts = Posts.query.all()
#         return render_template('dashboard.html', params=params, posts = posts)
#
#
#     if request.method=='POST':
#         username = request.form.get('unam # session['user'] = emaile')
#         userpass = request.form.get('pass')
#         if (username == params['admin_user'] and userpass == params['admin_password']):
#             #set the session variable
#             session['user'] = username
#             posts = Posts.query.all()
#             return render_template('dashboard.html', params=params, posts = posts)
#
#     return render_template('login.html', params=params)
#

@app.route("/checkUser/edit/<string:sno>", methods = ['GET', 'POST'])
def edit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()

            if sno=='0':
                post = Posts(title=box_title, slug=slug, content=content, tagline=tline, img_file=img_file, date=date)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = box_title
                post.slug = slug
                post.content = content
                post.tagline = tline
                post.img_file = img_file
                post.date = date
                db.session.commit()
                return redirect('/checkUser/edit/'+sno)
        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', params=params, post=post, sno=sno)














#
# @app.route("/checkUser/uploader", methods = ['GET', 'POST'])
# def uploader():
#     if ('user' in session and session['user'] == params['admin_user']):
#         if (request.method == 'POST'):
#             f= request.files['file1']
#             f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename) ))
#             return "Uploaded successfully"
#
#
#
# @app.route("/checkUser/logout/")
# def Logout():
#     # session.pop('user')
#     return render_template('index.html')


@app.route("/checkUser/delete/<string:sno>", methods = ['GET', 'POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
        posts = Posts.query.all()
        visitor=Visitor.query.all()
    return render_template('dashboard.html', params=params, posts = posts,visitor=visitor)


# @app.route("/dashboard")
# def Dashboard():
#     posts = Posts.query.all()
#     return render_template('dashboard.html', params=params, posts = posts)
#











@app.route('/gender')
def index():
	return render_template('genderIndex.html')

@app.route('/genderPredict', methods=['POST'])
def predict():
	df= pd.read_csv("data/names_dataset.csv")
	# Features and Labels
	df_X = df.name
	df_Y = df.sex

    # Vectorization
	corpus = df_X
	cv = CountVectorizer()
	X = cv.fit_transform(corpus)

	# Loading our ML Model
	naivebayes_model = open("models/naivebayesgendermodel.pkl","rb")
	clf = joblib.load(naivebayes_model)

	# Receives the input query from form
	if request.method == 'POST':
		namequery = request.form['namequery']
		data = [namequery]
		vect = cv.transform(data).toarray()
		my_prediction = clf.predict(vect)
	return render_template('genderResults.html',prediction = my_prediction,name = namequery.upper())







app.run(debug=True)





# from flask import Flask, render_template
# app = Flask(__name__)
#
#
# @app.route("/")
# def home():
#     return render_template('index.html')
#
#
# @app.route("/about")
# def about():
#     return render_template('about.html')
#
#
# @app.route("/contact")
# def contact():
#     return render_template('contact.html')
#
#
# app.run(debug=True)

