# from time import sleep, time
import requests
from flask import jsonify, request
from flask_cors import cross_origin
from repostories import create_blog, get_blogs
from app import app
# import time


@app.route('/posts', methods = ['GET', "POST"])
@cross_origin(supports_credentials=True)
def posts():
    if request.method == 'POST':
        title = request.json['title']
        
        
        new_blog = create_blog(title=title)
        post_data = {
            'type': 'PostCreated',
            'data': new_blog
        }
        requests.post('https://microservices-eventbus-service.herokuapp.com/events', json=post_data)
        return jsonify(new_blog), 201
    # time.sleep(1)    
    blogs = get_blogs()
    return jsonify(blogs)



