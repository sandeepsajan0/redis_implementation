import os
from flask import Flask, render_template,redirect,url_for
import requests
from flask import request
import redis
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

r = redis.Redis(host='localhost',db=1)


def get_add():
    #print (r.hmget(name,{"addr","dist"}))
    #v=(r.hgetall(name))
    print (r.keys())
    flag =0
    query = bytes(input(">>>"),'utf-8')

    for key in r.keys():
        if (key) == query:
            print (r.hgetall(key))
            flag = 1
            break
            
    if flag ==0:
        print ("no key found") 
    return start()
               
    
def start():
    print ("feed C for create a new key and G for querying")
    print(r.keys())
    check = input("feed your choice>>>")
    
    if check == 'C':
        app.run()
    elif check == 'G':
        get_add()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        n1 = request.form['name']
        a1 = request.form['city']
        a2 = request.form['dist']
        a3 = request.form['country']
        key_value = {'name':n1,
                     'city':a1,
                     'dist':a2,
                     'country':a3,}
        r.hmset(n1,key_value)
        return start()
    return render_template('index.html')


if __name__ == '__main__':
    start()

