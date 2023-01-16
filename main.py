from flask import Flask, render_template,request,redirect
# from post import Post
from auto_email import send_mail
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = StringField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


#Render Headlines and subheadlines of your Blogs
@app.route('/')
def home():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", posts=posts)


@app.route("/allposts")
def get_allposts():
    posts = db.session.query(BlogPost).all()
    return render_template("allposts.html", posts=posts)


#get contact detail of your user and send email verification to user
@app.route("/contact",methods=["GET","POST"])
def get_contact():
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        send_mail(massage= f"Subject: submit \n\n"
                           f"{name}\n"
                           f"{email}\n" ,to_ad=email)
        return redirect(app.url_for('get_contact'))

    return render_template("contact.html")


#render the about page
@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/post/<int:id_>")
def get_post(id_):
    post = BlogPost.query.get(id_)
    return render_template("post.html", post=post)



# @app.route("/data_handler" ,methods=["POST"])
# def form_data_handle():
#     name=request.form['name']
#     return f"hey {name} your data is collected"

if __name__ == "__main__":
    app.run(debug=True)
