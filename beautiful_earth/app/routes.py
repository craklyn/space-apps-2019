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
sys.path.insert(1, '/Users/parismorgan/space-apps-2019/beautiful_earth/pytorch-CycleGAN-and-pix2pix')

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

    # # Dummy code - get image as cv2 image
    # resp = urllib.urlopen(imageUrl)
    # image = np.asarray(bytearray(resp.read()), dtype="uint8")
    # image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # This is how we could go from cv2 to jpeg - https://stackoverflow.com/questions/48465739/send-and-receive-opencv-images-flask


    # TODO - Run model on this image URL
    
    temp = inference.infer(imageUrl)

    #print(temp)

    temp = (temp.detach().numpy() + 0.5) * 512
    print(temp.shape)

    temp = np.squeeze(temp, axis=0)
    print(temp.shape)
    temp = np.transpose(temp, (1,2,0))

    print(temp.shape)

    print(temp)
    filename = "/Users/parismorgan/space-apps-2019/beautiful_earth/app/static/"+quadKey+".png" 
    
    cv2.imwrite(filename, temp)

    print("PARISDEBUG: " + filename)

    response = make_response(send_file(filename, mimetype='image/jpeg', as_attachment=True, attachment_filename=quadKey))
    response.headers['X-quadKey'] = quadKey
    return response