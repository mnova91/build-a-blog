from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:admin@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/', methods=['GET'])
def index():

    return render_template('post_list.html',title="Build-a-blog")

@app.route('/newpost', methods=['POST', 'GET'])
def create_new_post():

    if request.method == 'GET':
        return render_template('create_post.html')

    if request.method == 'POST':
        blog_title = request.form['blog-title']
        blog_content = request.form['blog-body']
        new_blog_post = Blog(blog_title,blog_content)
        db.session.add(new_blog_post)
        db.session.commit()        

    return render_template('post_list.html' ,title="Build-a-blog")

if __name__ == '__main__':
    app.run()