from flask import Flask, render_template
from threading import Thread
app = Flask(__name__)
@app.route('/')
def index():
  return "alive"
def rün():
 app.run(host='0.0.0.0',port=8080)
def keep_alove():
  t = Thread(target=rün)
  t.start()