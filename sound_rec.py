from flask import Flask,request, render_template
from twilio.http.http_client import TwilioHttpClient
from twilio.rest import Client

client = Client(account_sid, auth_token,http_client=proxy_client)
app = Flask(__name__)

@app.route('/wtsapp')
def student():
   return render_template('watsapp.html')

@app.route("/get_data", methods=["GET", "POST"])
def get_data():
    if request.method == "POST":
        message=request.form["msg"]
        message = client.messages.create(body=message,from_='+12013080312',to='+919492767634')
        return render_template('watsapp.html',message = message)
    return render_template('watsapp.html')
  
  if __name__ == '__main__':
    app.run()
