# from crypt import methods
# import email

from ipaddress import IPv4Address
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# from flask import session
import json
app = Flask(__name__)
# app.secret_key = 'super-secret-key'
with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server= True

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)
Id="SROS4M" 


@app.route("/")
def home():
    return render_template('login.html')

@app.route("/T42")
def t42():
    return render_template('T42.html')

@app.route("/Index", methods = ['GET', 'POST'])
def home1():
    # if "user" in session and session['user']==params['admin_user']:
    #             return render_template("Index.html")
    
    if (request.method=="POST"):
        groupId = request.form.get("Id")
        grouppass = request.form.get("password")
        if groupId =="SROS4M" and grouppass == "S4M11522":
        
            return render_template('Index.html')
            
        else:
            return render_template('login1.html')

@app.route("/Index1")
def home2():
    return render_template('Index.html')



@app.route("/projects")
def projects():
    return render_template('projects.html')
@app.route("/bbcovid")
def bbcovid():
    return render_template('bbcovid.html')
@app.route("/members")
def members():
    return render_template('members.html')
@app.route("/mr")
def mr():
    return render_template('mr.html')

@app.route("/sc")
def sc():
    return render_template('sc.html')
@app.route("/sg")
def sg():
    return render_template('sg.html')
@app.route("/sm")
def sm():
    return render_template('sm.html')

@app.route("/ss")
def ss():
    return render_template('ss.html')

@app.route("/sss")
def sss():
    return render_template('sss.html')
    
IPv4 =  IPv4Address






app.run(debug=True , host= IPv4)
