from flask import render_template
from flask import request
from flask import send_file
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
    print(quadKey + " -> " + imageUrl)

    # TODO - Run model on this image URL

    filename = 'static/img.jpg'
    return send_file(filename, mimetype='image/jpeg', as_attachment=True, attachment_filename=quadKey) 
