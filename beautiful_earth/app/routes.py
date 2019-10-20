from flask import render_template
from flask import request
from flask import send_file
from flask import make_response
import cv2
import urllib
import numpy as np
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

    # Dummy code - get image as cv2 image
    resp = urllib.urlopen(imageUrl)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # TODO - Run model on this image URL

    # This is how we could go from cv2 to jpeg - https://stackoverflow.com/questions/48465739/send-and-receive-opencv-images-flask

    filename = 'static/img.jpg'
    response = make_response(send_file(filename, mimetype='image/jpeg', as_attachment=True, attachment_filename=quadKey))
    response.headers['X-quadKey'] = quadKey
    return response