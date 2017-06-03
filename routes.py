import os,json



from settings import app
from flask import request,render_template,send_file
import requests


"""   home page   """
@app.route("/")
def home():
    return render_template("upload.html",title="ReCapcha",current_url = request.url)


"""  file upload  """
@app.route("/check_capcha",methods=["POST"])
def check_capcha():

    data = {};

    if request.method == 'POST':

        try:

            response = request.form["response"]

            req = requests.post('https://www.google.com/recaptcha/api/siteverify',data={"secret":"6LeQ_SMUAAAAAJdimLwN9FvqJwnMZ-iGj85goGfh","response":response});

            return req.text
        except Exception as e:
            pass    


    return json.dumps(data);

