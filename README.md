# An App to call an image classifier api

## This project is an app which can be used to request an api that will classifiy if a patient x-ray has Pneumonia or not. An x-ray image will be passed from this app to the api server and the api server will be able to send following JSON response:
1) Prediction of the image i.e if the patient has Pneumonia or not.
2) Confidence of the classification in terms of percentage.

The api code and other details related to the api are present at:

https://github.com/mhosankalp/automc_api

Also note this app has test integration with stripe for payment purpose

### Prerequisites

1. Python 3.6
2. The api server should be up and running
For details on how to run the api please refer to https://github.com/mhosankalp/automc_api


### Installing

A step by step series of examples that tell you how to get a development env running

1. Git Clone this repository - git clone https://github.com/mhosankalp/automcx
2. cd automcx
3. Create a virual enviornment
4. source activate virtual enviornment
5. pip install -r requirements.txt
6. python app.py
7. Navigate to 127.0.0.1:5000 in your browser (safari/chrome) and follow steps as per the screenshot below:

a)Home Screen - About

![Home Screen - About](https://github.com/mhosankalp/automcx/blob/master/media/image1.png)

b)Home Screen - Pricing

![Home Screen - Pricing](https://github.com/mhosankalp/automcx/blob/master/media/image2.png)

c)Home Screen - Contact

![Home Screen - Contact](https://github.com/mhosankalp/automcx/blob/master/media/image3.png)

d)Home Screen - Payment

![Home Screen - Payment](https://github.com/mhosankalp/automcx/blob/master/media/image4.png)

e)Home Screen - Choose File

![Home Screen - Choose File](https://github.com/mhosankalp/automcx/blob/master/media/image5.png)

f)Home Screen - File Chosen

![Home Screen - File Chosen](https://github.com/mhosankalp/automcx/blob/master/media/image6.png)

g)Home Screen - Api is call from 127.0.0.1:5001 and prediction is made

![Home Screen - File Chosen](https://github.com/mhosankalp/automcx/blob/master/media/image7.png)



