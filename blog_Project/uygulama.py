from flask import Flask, flash, request, redirect, url_for,render_template,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////Users/asus/Desktop/pythonProject2/blog.db'
db=SQLAlchemy(app)

class Blogpost(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50))
    subtitle=db.Column(db.String(50))
    author=db.Column(db.String(25))
    date_posted=db.Column(db.DateTime)
    content=db.Column(db.Text)


@app.route("/")
def index():
    posts=Blogpost.query.order_by(Blogpost.date_posted.desc()).all()

    return render_template("index.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:post_id>")
def post(post_id):
    post=Blogpost.query.filter_by(id=post_id).one()

    return render_template("post.html",post=post)

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/addpost",methods=['post'])
def addpost():
    title=request.form['title']
    subtitle=request.form['subtitle']
    author=request.form['author']
    content=request.form['content']

    post=Blogpost(title=title,subtitle=subtitle,author=author,content=content,date_posted=datetime.now())
    db.session.add(post)
    db.session.commit()
    return redirect(url_for("index"))


if __name__=="__main__":
    db.create_all()
    app.run(debug=True)

