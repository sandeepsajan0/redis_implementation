import os
from flask import Flask
from flask import Flask, render_template,redirect
import requests
from flask import request
import redis
from redisgraph import Node, Edge, Graph
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

r = redis.Redis(host='localhost',db=0)

@app.route('/<name>')
def get_add(name):
    return r.get(name)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        n1 = request.form['name']
        a1 = request.form['address']
        print(n1,a1)
        r.set(n1,a1)
        print (r.get(n1))
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
