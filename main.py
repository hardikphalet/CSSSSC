
from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy

import json
from datetime import datetime
import os
# from werkzeug import secure_filename 
from werkzeug.utils import secure_filename  
app = Flask(__name__)
app.secret_key='secretkey'
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/compscsoc"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://testing:testing@123@localhost/compsocssc"
#app.config['UPLOAD_FOLDER'] = "C:\\Users\\Bindal\\Desktop\\Flask\\CompSocBlog\\static\\img"

db = SQLAlchemy(app) # INITIALIZE THE DATABASE

class Contacts(db.Model): # This Contact Class is for contact table 
    __tablename__='contact'
    Qstnd = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), nullable=False)
    EmailId = db.Column(db.String(20), nullable=False)
    PhoneNum = db.Column(db.String(12), nullable=False)
    Msg = db.Column(db.String(120), nullable=False)
    DT = db.Column(db.String(12), nullable=True)
   

class Posts(db.Model): # This Posts Class is for Posts table 
    __tablename__='posts'
    PostId = db.Column(db.Integer, primary_key=True)
    PostTitle = db.Column(db.String(80), nullable=False)
    PostContent = db.Column(db.String(500), nullable=False)
    ImgFile = db.Column(db.String(50), nullable=False)
    PostedBy = db.Column(db.String(20), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    DT = db.Column(db.String(12), nullable=True)

# nullable = false => SQL column NOT NULL

#redirects to main homepage of the society
@app.route("/")
def home():
    #gets all the posts, filtered from 0 to 4, need to figure out how to add more pages
    posts=Posts.query.filter_by().all()[0:4]
    return render_template('index.html', Posts=posts)

#leads to the about us section
@app.route("/about")
def about():
    return render_template('about.html')


#The contact us page
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    #checks Form submission
    #Need to remember to escape characters before using
    if(request.method=='POST'):
        Name=request.form.get('Name')
        EmailId=request.form.get('Email')
        ContactNum=request.form.get('ContactNum')
        Msg=request.form.get('MSG')

        entry = Contacts(
            Name=Name, 
            EmailId=EmailId, 
            PhoneNum=ContactNum, 
            Msg=Msg, 
            DT=datetime.now()
        )
        #LHS from Class Contacts, RHS Values taken from form
        
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')

# Handles Individual posts, gets by PostSlug
@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    Post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', Post=Post)

#ADMIN PANEL SECTION BEGINS HERE
#wondering whether to move these all to /dashboard/ to prevent rogue users accessing areas of the site
#uploader section handles files
@app.route("/dashboard/uploader", methods=['GET', 'POST'])
def Upload():
    # Only Loggged In user can upload files
    if ('Admin' in session and session['Admin']=="Compssc"): 
        if(request.method=='POST'):
            FileComing=request.files['ImgF']
            FileComing.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(FileComing.filename)))
            return "Upload Complete"
    else :
        return redirect('/dashboard')


#delete section handles deleting files
@app.route("/delete/<int:PostId>", methods = ['GET', 'POST'])
def delete(PostId):
    # Only Loggged In user can delete files
    if ('Admin' in session and session['Admin']=="Compssc"):
        PostId = str(PostId) 
        post=Posts.query.filter_by(PostId=PostId).first()
        db.session.delete(post)
        db.session.commit()    
    return redirect('/dashboard')

#logout section to handle logging out
@app.route("/logout")
def Logout():
    session.pop('Admin')
    return redirect('/dashboard')

@app.route("/dashboard/edit/<int:PostId>", methods = ['GET', 'POST'])
def edit(PostId):
    if ('Admin' in session and session['Admin']=="Compssc"): # Only Loggged In user can edit the post
        PostId = str(PostId) 
        if request.method == 'POST':
            PrevTitle=request.form.get('Title')
            PrevContent=request.form.get('Content')
            PrevSlug=request.form.get('Slug')
            PrevImg=request.form.get('ImageFile')    
            Author=request.form.get('WrittenBy')    
            Dt=datetime.now()

            if PostId=='0':
                Post = Posts(PostTitle=PrevTitle, PostContent=PrevContent, ImgFile=PrevImg, PostedBy=Author, slug=PrevSlug, DT=Dt)
                db.session.add(Post)
                db.session.commit()
            else:
                Post=Posts.query.filter_by(PostId=PostId).first()
                Post.PostTitle     = PrevTitle                                      
                Post.PostContent  = PrevContent
                Post.PostedBy  = Author
                Post.ImgFile  = PrevImg
                Post.Slug  = PrevSlug
                Post.DT      = Dt
                db.session.commit()
                return redirect('/dashboard/edit/'+PostId)
        #Post=Posts.query.filter_by(PostId=PostId).first()
    else:
        return redirect('/')

@app.route("/dashboard", methods=['GET','POST'])
def dashboard():

    if ('Admin' in session and session['Admin']=="Compssc"):
        Post=Posts.query.all()
        return render_template('adminpanel.html', Posts=Post)

    if (request.method=='POST'):
        UserName=request.form.get('UserName')
        Password=request.form.get('Password')
        checkuse="Compssc"

        checkpass="LinusTovald"
        if(UserName==checkuse and Password==checkpass):
            # Set The Session Variable
            session['Admin']=UserName
            Post=Posts.query.all()

            return render_template('adminpanel.html', Posts=Post)
        else:
            return render_template('contact.html')




    else:
        return render_template('SignUp.html')    


    



app.run(debug=True)








  