
from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime



app = Flask(__name__)
app.secret_key='secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/compscsoc"

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
    __tablename__='Posts'
    PostId = db.Column(db.Integer, primary_key=True)
    PostTitle = db.Column(db.String(80), nullable=False)
    PostContent = db.Column(db.String(500), nullable=False)
    ImgFile = db.Column(db.String(50), nullable=False)
    PostedBy = db.Column(db.String(20), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    DT = db.Column(db.String(12), nullable=True)


# Default value of nullabe is True so We make it False where for unique it is True so We dont mention we need column in any field


@app.route("/")
def home():
    posts=Posts.query.filter_by().all()[0:4]
    return render_template('index.html', Posts=posts)


@app.route("/about")
def about():
   
    return render_template('about.html')



@app.route("/contact", methods=['GET', 'POST'])

def contact():
    if(request.method=='POST'):
        # Add Entry To the database
        Name=request.form.get('Name')
        EmailId=request.form.get('Email')
        ContactNum=request.form.get('ContactNum')
        Msg=request.form.get('MSG')

        entry = Contacts(Name=Name, EmailId=EmailId, PhoneNum=ContactNum, Msg=Msg, DT=datetime.now() )# Here lhs are from class attribute and rhs are if ke andar wale
        
        db.session.add(entry)
        db.session.commit()



    return render_template('contact.html')



@app.route("/Post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    Post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', Post=Post)


@app.route("/delete/<string:PostId>", methods = ['GET', 'POST'])
def delete(PostId):
    if ('Admin' in session and session['Admin']=="Compssc"): # Only Loggged In user can edit the post
        post=Posts.query.filter_by(PostId=PostId).first()
        db.session.delete(post)
        db.session.commit()    
    return redirect('/DashBoard')



@app.route("/Logout")
def Logout():
    session.pop('Admin')
    return redirect('/DashBoard')

@app.route("/edit/<string:PostId>", methods = ['GET', 'POST'])
def edit(PostId):
    if ('Admin' in session and session['Admin']=="Compssc"): # Only Loggged In user can edit the post
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
                return redirect('/edit/'+PostId)
    Post=Posts.query.filter_by(PostId=PostId).first()
    
    return render_template('edit.html',  Post=Post, PostId=PostId)

















@app.route("/DashBoard", methods=['GET','POST'])
def DashBoard():

    if ('Admin' in session and session['Admin']=="Compssc"):
        Post=Posts.query.all()
        return render_template('AdminPanel.html', Posts=Post)

    if (request.method=='POST'):
        UserName=request.form.get('UserName')
        Password=request.form.get('Password')
        checkuse="Compssc"

        checkpass="LinusTovald"
        if(UserName==checkuse and Password==checkpass):
            # Set The Session Variable
            session['Admin']=UserName
            Post=Posts.query.all()

            return render_template('AdminPanel.html', Posts=Post)
        else:
            return render_template('contact.html')



    #    Ridirect To Admin Panel
    else:
        return render_template('SignUp.html')    


    



app.run(debug=True)








  