from flask import render_template
from flask import request
from flask import send_file
from flask import make_response
import cv2
import urllib
import numpy as np

# Add the pytorch folder to our script path
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/danielblackburn/space-apps-2019/beautiful_earth/pytorch-CycleGAN-and-pix2pix')

import inference
from inference import infer

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

    temp = inference.infer(imageUrl)

    filename = "/Users/danielblackburn/space-apps-2019/beautiful_earth/app/static/"+quadKey+".png" 
    cv2.imwrite(filename, temp)

    response = make_response(send_file(filename, mimetype='image/jpeg', as_attachment=True, attachment_filename=quadKey))
    response.headers['X-quadKey'] = quadKey
    return response
