from flask import Flask,make_response,render_template,request
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello"
app.run(debug=True,host='0.0.0.0')

