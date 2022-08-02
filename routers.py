from flask import jsonify , request
from repostories import create_blog, get_blogs
from app import app

@app.route('/posts',methods = ['GET',"POST"])
def posts():
    if request.method == 'POST':
        title = request.json['title']
        new_blog = create_blog(title=title)
        return jsonify(new_blog), 201
    blogs = get_blogs()
    return jsonify(blogs)


