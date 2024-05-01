from flask import Flask,render_template,redirect,request
from database import DB
import api
db = DB()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('login.html')

@app.route("/register")
def registration():
    return render_template("register.html")

@app.route("/perform_registration", methods=['POST'])
def perform_registration():
    name = request.form.get("user_ka_name")
    email = request.form.get("user_ka_email")
    password = request.form.get("user_ka_password")
    response = db.insert_user_data(name,email,password)
    if response == 1:
        return render_template("login.html", message="Registration successful")
    else:
        return render_template('register.html',message='Email already exist')
    
@app.route("/perform_login", methods=['POST'])
def perform_login():
    email = request.form.get("user_ka_email")
    password = request.form.get("user_ka_password")
    response = db.search_user_data(email,password)
    if response == 1:
        return redirect("/profile")
    else:
        return render_template("login.html", message="email/password incorrect")    

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route("/perform_ner",methods=['post'])
def perform_ner():
        text = request.form.get('ner_text')
        response = api.ner(text)
        result = ''
        for i in response['entities']:
            result = result + i['name'] + " " + i['category'] + '\n'
        return render_template('ner.html',result=result)

@app.route("/sentiment")
def sentiment():
    return render_template("sentiment.html")

@app.route("/perform_sentiment", methods=['POST'])
def perform_sentiment():
    text = request.form.get('sentiment_text')
    response = api.sentiment_analysis(text)
    result = ''
    result = result + "negative: " + str(response['sentiment']["negative"]) + " " + "neutral: " + str(response['sentiment']["neutral"]) + " " + "positive: " + str(response['sentiment']["positive"])
    return render_template('sentiment.html', result=result)

@app.route("/abuse")
def abuse():
    return render_template("abuse.html")

@app.route("/perform_abuse", methods=['POST'])
def perform_abuse():
    text = request.form.get("abuse_text")
    response = api.abuse_detection(text)
    result = "abusive :" + str(response['abusive']) + " " + "hate_speech :" + str(response['hate_speech']) + " " + "neither :" + str(response['neither'])
    return render_template("abuse.html", result=result)

    
if __name__ == "__main__":
    app.run(debug=True)