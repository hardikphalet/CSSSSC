
from flask import Flask, render_template, request, session, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
import re
import math
from datetime import datetime
import os
# from werkzeug import secure_filename 
from werkzeug.utils import secure_filename  
app = Flask(__name__)
app.secret_key='secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/compscsoc" 
app.config['UPLOAD_FOLDER'] = "C:\\Users\\SSC\\Desktop\\Flask\\CompSocBlog\\static\\img"

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


# Default value of nullabe is True 
# Default value of unique is False 
# nullable = false => SQL column NOT NULL


# Ridrect to the homepage










@app.route("/")
def home():
    posts=Posts.query.all()  
    Len=len(posts)
    last=math.ceil(Len/4)
    


    Page=(request.args.get('Page'))



    if(not str(Page).isnumeric()):
        Page=1
        
    Page=int(Page)
    posts= posts[int((Page-1)*4):int((Page-1)*4+4)]


    if (Page==1):
        Previous='#'
        Next="/?Page="+str(Page+1)
    elif (Page==last):
        Next='#'
        Previous="/?Page="+str(Page-1)
    else:
        Previous="/?Page="+str(Page-1)
        Next="/?Page="+str(Page+1)




    posts=Posts.query.filter_by().all()[int((Page-1)*4):int((Page-1)*4+4)]
    return render_template('index.html', Posts=posts, Prev=Previous, Next=Next )












# Leads to About us section
@app.route("/about")
def about():
   
    return render_template('about.html')



@app.route("/contact", methods=['GET', 'POST'])

def contact():
    #checks Form submission
    if(request.method=='POST'):
        # Add Entry To the database
        Name=request.form.get('Name')
        EmailId=request.form.get('Email')
        ContactNum=request.form.get('ContactNum')
        Msg=request.form.get('MSG')

        entry = Contacts(
            Name=Name,
             EmailId=EmailId,
              PhoneNum=ContactNum,
               Msg=Msg, 
               DT=datetime.now() )# #LHS from Class Contacts, RHS Values taken from form
        
        db.session.add(entry)
        db.session.commit()


        flash("Thanks, For Contacting, Get back to you soon!!  ","success")

    return render_template('contact.html')














@app.route("/Uploader", methods=['GET', 'POST'])
def Upload():
    if ('Admin' in session and session['Admin']=="Compssc"): # Only Loggged In user can edit the post
        if(request.method=='POST'):
            FileComing=request.files['ImgF']

            FileComing.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(FileComing.filename)))
            flash("Your Image added Successfully  ","success")

        else:
                flash("Your File can't be upload try again ","danger")
        return redirect('/DashBoard')
            








@app.route("/Post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
     #checks that the post slug contains no characters other than alphanumeric ones and '-'
    # \W = any character not [A-Za-z0-9_]
    match = re.search(r"\W", post_slug)
    #if an unknown character found, redirect to homepage, else render post template with slug as Post.Slug
    if match:
        return redirect('/')
    else :
        Post = Posts.query.filter_by(slug=post_slug).first()
        # splits up the content by para so that it's easier to output in the template file. Then resets Post.PostContent to the generated list of paras
        contenttobreak = Post.PostContent.split('\n')
        Post.PostContent = contenttobreak
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

             #section checks if the slug entered is a repeat value
            # **IDEA: Generate the slug instead of asking the user to enter**
            #Loop goes through each post in the Posts table
            for post in Posts.query.all():
                #Need to check if the new slug (PrevSlug) as a slug in a post that isn't the post being edited.
                #using PostId as the verifier since PostId is the Primary Key of the table
                # LOGIC:
                # Post Ids match    and slugs match     > No Action
                # Post Ids X match  and slugs match     > Error
                # Post Ids match    and slugs X match   > No Action
                # Post Ids X match  and slugs X match   > No Action 
                if post.PostId != PostId and PrevSlug == post.slug:
                    #flash method passes the error to the redirected page
                    flash("Another post exists with the same slug, please modify")
                    return redirect('/edit/'+str(PostId))
            #for creating a new post, basically uses the same page
            #same pattern matching as in post URL, checking to make sure no special characters are allowed in the slug
            match = re.search(r"\W", PrevSlug)
            #if character found, then flash error message
            if match:
                flash("Cannot use any character other than A-Z, a-z, 0-9 and _ in the slug")
                return redirect('/edit/'+str(PostId))
            PostId = str(PostId) 
            
            if PostId=='0':
                Post = Posts(PostTitle=PrevTitle, PostContent=PrevContent, ImgFile=PrevImg, PostedBy=Author, slug=PrevSlug, DT=Dt)
                db.session.add(Post)
                db.session.commit()


                # 0 is for add new article and else condition for edit
                
            else:
                Post=Posts.query.filter_by(PostId=PostId).first()
                Post.PostTitle     = PrevTitle                                      
                Post.PostContent  = PrevContent
                Post.PostedBy  = Author
                Post.ImgFile  = PrevImg
                Post.slug  = PrevSlug
                Post.DT      = Dt
                
                db.session.commit()
                flash("You have edited a Article,successfully ","success")
    
                return redirect('/edit/'+PostId)
        # else:
        #     return redirect('/')        
    Post=Posts.query.filter_by(PostId=PostId).first()
    return render_template('edit.html',  Post=Post, PostId=PostId)

















@app.route("/DashBoard", methods=['GET','POST'])
def DashBoard():
 #checks if user already logged in
    if ('Admin' in session and session['Admin']=="Compssc"):
        Post=Posts.query.all()
        return render_template('AdminPanel.html', Posts=Post)
 #Checks if login form submitted
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
            # flash("Your UserName and Password didn't match","danger")
            return render_template('SignUp.html')



    #    Ridirect To Admin Panel
    else:
        return render_template('SignUp.html')    


    



app.run(debug=True)








  