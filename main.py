
from flask import Flask, render_template, request, session, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from re import search
import math
from datetime import datetime
import os
# from werkzeug import secure_filename 
from werkzeug.utils import secure_filename 
from werkzeug.exceptions import RequestEntityTooLarge 
app = Flask(__name__)
app.secret_key='secretkey'
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/compscsoc" 
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://testing:testing@123@localhost/compsocssc"
# app.config['UPLOAD_FOLDER'] = "C:\\Users\\SSC\\Desktop\\Flask\\CompSocBlog\\static\\img"
#uses a relative path name instead of a complete path name,
#redirects all uploads to the folder .static/img/ within the project folder
app.config['UPLOAD_FOLDER'] = './static/img'
#Popular Image file extensions, can be supplemented later on
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff' }
#sets the maximum file size that can be uploaded to 10MB
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

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
    __tablename__='posts' #Always better to assume strict checking of SQL
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


# Redirect to the homepage of our website
@app.route("/")
def home():
    #gets all the posts
    posts=Posts.query.all()  
    #calculates the number of posts
    Len=len(posts)
    #finds the number of pages we'll have (rounding up Len/4)
    last=math.ceil(Len/4)
    #checks the value of the Page Variable being passed through GET in the URL
    Page=(request.args.get('Page'))
    #Checks whether the value is not numeric, indicating first page
    if(not str(Page).isnumeric()):
        Page=1
    #makes sure to convert the value of the GET into int
    #Possible TypeError arising here
    Page=int(Page)
    #Slices our dictionary of posts into the posts for this current page
    posts= posts[int((Page-1)*4):int((Page-1)*4+4)]
    #Conditions for the previous and next pages
    if (Page==1):
        Previous=''
        #makes sure to recast page to a string for use in the URL
        Next="/?Page="+str(Page+1)
    elif (Page==last):
        Next=''
        Previous="/?Page="+str(Page-1)
    else:
        Previous="/?Page="+str(Page-1)
        Next="/?Page="+str(Page+1)
    #Don't really need to call this again
    #Might be better to change the pervious operation we do on posts to being posts1 or page_posts
    posts=Posts.query.filter_by().all()[int((Page-1)*4):int((Page-1)*4+4)]
    #renders template for homepage
    return render_template('index.html', Posts=posts, Prev=Previous, Next=Next )

# Leads to About us section
@app.route("/about")
def about():
    return render_template('about.html')

# Leads to the contact us page
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    #checks Form submission
    #Need to remember to escape all the values before finally implementing, though flask might alread do that for us
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
            DT=datetime.now()
        )
        #LHS from Class Contacts, RHS Values taken from form 
        db.session.add(entry)
        db.session.commit()
        # Adds a success message, to be flashed in contact.html when rendered
        flash("Thanks, For Contacting, Get back to you soon!!  ","success")

    return render_template('contact.html')

#handles individual post pages, by the post slug set
@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
     #checks that the post slug contains no characters other than alphanumeric ones and '-'
    # \W = any character not [A-Za-z0-9_]
    match = search(r"\W", post_slug)
    #if an unknown character found, redirect to homepage, else render post template with slug as Post.Slug
    if match:
        return redirect('/')
    else :
        Post = Posts.query.filter_by(slug=post_slug).first()
        # splits up the content by para so that it's easier to output in the template file. Then resets Post.PostContent to the generated list of paras
        contenttobreak = Post.PostContent.split('\n')
        Post.PostContent = contenttobreak
        return render_template('post.html', Post=Post)

#ADMIN PANEL SECTION BEGINS HERE    
#wondering whether to move these all to /dashboard/ to prevent rogue users accessing areas of the site
#uploader section handles the uploading of files
#Also converting all of the naming to either camelCase (first letter of word small, otherFirstLettersCapitalized)

#checking file extension to prevent loading malware onto the site
#using template provided by the Flask Project documentation
def allowed_file(filename):
    #checks that the file has an extension, and that the extension is allowed
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/dashboard/uploader", methods=['GET', 'POST'])
def Upload():
    #might need to add more validation here, rogue users may still be able to view the form
     # Only Loggged In user can edit the post
    if ('Admin' in session and session['Admin']=="Compssc"):
        #checks if form containing the file is submitted
        if(request.method=='POST'):
            #checks whether a file has been selected for upload or not
            if 'ImgF' not in request.files:
                flash("No file uploaded", "danger")
                return redirect('/dashboard')

            FileComing=request.files['ImgF']
            #Checks to see if filename not blank
            if FileComing.filename == '':
                flash("No selected file for upload", "danger")
                return redirect('/dashboard')

            if FileComing and allowed_file(FileComing.filename):
                #save the file in the path given in the UPLOAD FOLDER VARIABLE  at line 14/15
                try: 
                    FileComing.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(FileComing.filename)))
                    flash("Your Image added Successfully  ","success")
                except RequestEntityTooLarge:
                    flash("Your file is too big. Try a smaller file (Max 10MB limit).","danger")
                    pass
                return redirect('/dashboard')
            else:
                flash("Your file is of an invalid format. Try again, with a different format. ","danger")
                return redirect('/dashboard')
    else:
        return redirect('/dashboard')

#Handles a RequestEntityTooLarge error
@app.errorhandler(413)
@app.errorhandler(RequestEntityTooLarge)
def redirect_to_dashboard(e):
    flash("Your file is too big. Try a smaller file (Max 10MB limit).", "danger")
    return redirect('/dashboard')

#making sure that the value passed is only an int, preventing scripts being run
#delete section handles deleting of files
@app.route("/delete/<int:PostId>", methods = ['GET', 'POST'])
def delete(PostId):
    # Only Loggged In user can edit the post
    if ('Admin' in session and session['Admin']=="Compssc"): 
        PostId = str(PostId)
        post=Posts.query.filter_by(PostId=PostId).first()
        db.session.delete(post)
        db.session.commit()    
    return redirect('/dashboard')

#Logout section handles logging out
@app.route("/logout")
def Logout():
    session.pop('Admin')
    return redirect('/dashboard')

#edit section handles editing/creating articles
#<int:PostId> forces the get value to only be an integer, saving from XSS
@app.route("/dashboard/edit/<int:PostId>", methods = ['GET', 'POST'])
def edit(PostId):
    # Only Loggged In user can edit the post
    if ('Admin' in session and session['Admin']=="Compssc"):
        #Checks if form is submitted
        if request.method == 'POST':
            #Vars hold intermediate values that are filled into the form
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
                    return redirect('/dashboard/edit/'+str(PostId))
            #for creating a new post, basically uses the same page
            #same pattern matching as in post URL, checking to make sure no special characters are allowed in the slug
            match = search(r"\W", PrevSlug)
            #if character found, then flash error message
            if match:
                flash("Cannot use any character other than A-Z, a-z, 0-9 and _ in the slug")
                return redirect('/dashboard/edit/'+str(PostId))
            # creates a new post, using the same edit page 
            if PostId=='0':
                Post = Posts(PostTitle=PrevTitle, PostContent=PrevContent, ImgFile=PrevImg, PostedBy=Author, slug=PrevSlug, DT=Dt)
                db.session.add(Post)
                db.session.commit()
                #If the post already exists in the database
            else:
                Post=Posts.query.filter_by(PostId=PostId).first()
                Post.PostTitle  = PrevTitle
                Post.PostContent= PrevContent
                Post.PostedBy   = Author
                Post.ImgFile    = PrevImg
                Post.slug       = PrevSlug
                Post.DT         = Dt
                
                db.session.commit()
                flash("You have edited a Article,successfully ","success")
    
                return redirect('/dashboard/edit/'+str(PostId))
    else:
        return redirect('/')        
    Post=Posts.query.filter_by(PostId=PostId).first()
    return render_template('edit.html',  Post=Post, PostId=PostId)

#section handles generating the dashboard
@app.route("/dashboard", methods=['GET','POST'])
def dashboard():
 #checks if user already logged in
    if ('Admin' in session and session['Admin']=="Compssc"):
        Post=Posts.query.all()
        return render_template('adminPanel.html', Posts=Post)
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

            return render_template('adminPanel.html', Posts=Post)
        else:
            # flash("Your UserName and Password didn't match","danger")
            return render_template('signUp.html')
    #    Ridirect To Admin Panel
    else:
        return render_template('signUp.html')    

app.run(debug=True)








  