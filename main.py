



from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:K@n@k2006@localhost/compsoc' 
# THIS IS MYSQL database connection  and the syntax is 'mysql://USER:PASSWORD@SERVER/DATABASE' I have no password so here my pass is blank 

db = SQLAlchemy(app)  # INITIALIZE THE DATABASE

class Contact(db.Model):   # This Contact Class is for contact table 
    QsnId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(35), nullable=False)   
    EmailId = db.Column(db.String(40), nullable=False)
    PhoneNum = db.Column(db.String(12), nullable=False)
    Msg = db.Column(db.String(300), nullable=False)
    DT = db.Column(db.String(20), nullable=True)

# Default value of nullabe is True so We make it False where for unique it is True so We dont mention we need column in any field


@app.route("/")
def home():
    
    return render_template('index.html')


@app.route("/about")
def about():
   
    return render_template('about.html')



@app.route("/contact", methods=["GET","POST"])

def contact():
    if(request.method=='POST'):
        # Add Entry To the database
        Name=request.form.get('Name')
        EmailId=request.form.get('Email')
        ContactNum=request.form.get('ContactNum')
        Msg=request.form.get('MSG')


        entry=Contact(Name=Name, EmailId=EmailId, PhoneNum=ContactNum, Msg=Msg, DT=datetime.now()) # Here lhs are from class attribute and rhs are if ke andar wale
        db.session.add(entry)
        db.session.commit()



    return render_template('contact.html')




@app.route("/Post")
def Post():
    return render_template('Post.html')




app.run(debug=True)
app.run(debug=True)
app.run(debug=True)


  