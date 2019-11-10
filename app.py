import os
import cv2
#import magic
import urllib.request
import requests
import stripe
#from app import app
from flask import Flask, flash, request, redirect, render_template, session
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)
app.secret_key = os.urandom(12)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
KERAS_REST_API_URL = "http://127.0.0.1:5001/api/recognize_image"
stripe_keys = {
  'secret_key': 'sk_test_2kTbEmMlGASai1WWTJK6gZFI00aKtwd8i9',
  'publishable_key': 'pk_test_gEZVK3BBQuxnT0vY0MV7ECXt00fVwJKzHX'
}

stripe.api_key = stripe_keys['secret_key']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route('/')
def upload_form():
    session['payment_complete'] = False
    return render_template('index_new.html', key=stripe_keys['publishable_key'])

@app.route('/charge', methods=['POST'])
def charge():
    if not session.get('payment_complete'):
        try:
            amount = 2500   # amount in cents
            customer = stripe.Customer.create(
                email='sample1@customer.com',
                source=request.form['stripeToken']
            )
            stripe.Charge.create(
                customer=customer.id,
                amount=amount,
                currency='usd',
                description='An AUTOMC Charge'
            )
            session['payment_complete'] = True        
            return render_template('index.html', amount=amount)
        except stripe.error.StripeError:
            emessage="You must Pay"
            return render_template('error.html',emessage=emessage)
    else:
        return render_template('index.html', amount=amount) 

@app.route('/', methods=['POST'])
def upload_file():
    if session.get('payment_complete'):
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No file selected for uploading')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                #filename = secure_filename(file.filename)
                basepath = os.path.dirname(__file__)
                file_path = os.path.join(
                basepath, 'uploads', secure_filename(file.filename))
                file.save(file_path)
                # prepare headers for http request
                content_type = 'image/jpeg'
                headers = {'content-type': content_type}
                # encode image as jpeg
                img = cv2.imread(file_path)
                _, img_encoded = cv2.imencode('.jpg', img)
                # send http request with image and receive response
                r = requests.post(KERAS_REST_API_URL, data=img_encoded.tostring(), headers=headers)
                pred = r.json()["data"]
                prediction = pred["prediction"]
                confidence = pred["confidence"]
                return render_template('predict.html',prediction=prediction,confidence=confidence)
            else:
                emessage = 'Allowed file types are png, jpg, jpeg'
                return render_template('error.html',emessage=emessage)
    else:
        return ('You must Pay')

@app.route('/predict', methods=['POST'])
def predict():
    session['payment_complete'] = False
    return render_template('index_new.html', key=stripe_keys['publishable_key'])

@app.route('/back', methods=['POST'])
def back():
    return render_template('index.html')

if __name__ == "__main__":
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()