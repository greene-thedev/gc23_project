from flask import Flask, render_template, request, redirect
from gpio import engage

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():

        
    return render_template("index.html")

@app.route("/engage", methods = ["POST"])
def eng():
    engage()
    return redirect("/")
# @app.route('/whoami')
# def whoami():
#     return 
    

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
    