from flask import render_template
from flask import request
from flask import send_file
from flask import make_response
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Beautiful Earth')

@app.route('/image', methods = ['POST'])
def image():
    json = request.json
    imageUrl = json['imageUrl']
    quadKey = json['quadKey']
    tileLocRect = json['tileLocRect']

    # TODO - Run model on this image URL

    filename = 'static/img.jpg'
    response = make_response(send_file(filename, mimetype='image/jpeg', as_attachment=True, attachment_filename=quadKey))
    response.headers['X-quadKey'] = quadKey
    return response