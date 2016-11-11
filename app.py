from flask import Flask, render_template,url_for,request,session,redirect
from flask_session import Session


app = Flask(__name__)
sess=Session()

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/index")
def index():
	return render_template('index.html')

# if __name__ == "__main__":

app.secret_key = 'kwoc'
app.config['SESSION_TYPE'] = 'filesystem'

sess.init_app(app)
app.debug = True
	# app.run()