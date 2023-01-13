from flask import Flask, render_template,request,redirect
from post import Post
from auto_email import send_mail

my_post = Post()
app = Flask(__name__)


@app.route('/')
def home():
    posts = my_post.get_allposts()
    return render_template("index.html", posts=posts)


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


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/post/<int:id_>")
def get_post(id_):
    post = my_post.get_post_with_id(id_)
    return render_template("post.html", post=post)

@app.route("/allposts")
def get_allposts():
    posts = my_post.get_allposts()
    return render_template("allposts.html", posts=posts)

# @app.route("/data_handler" ,methods=["POST"])
# def form_data_handle():
#     name=request.form['name']
#     return f"hey {name} your data is collected"

if __name__ == "__main__":
    app.run()
