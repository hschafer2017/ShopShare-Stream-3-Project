import os 
from flask import Flask, redirect, render_template, request 

app = Flask(__name__)

shopping_list = []

@app.route('/')
def get_homepage():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login(): 
    group = request.form['group']
    username = request.form['username']
    return redirect("/" + group + "/" + username) 
# Pass two arguments through redirect without having to make an extra page 

# @app.route('/<group>')
# def get_group_page(group):
#     return render_template('chat_page.html')

@app.route('/<group>/<username>')
def get_user_page(group, username):
    return render_template('chat_page.html')
    # return render_template("chat_page.html", group = group, username = username)
    
# @app.route('/<group>/<username>/list')
# def add_shopping_item(group,username):
    
#     return redirect(group,username)
    
    
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug = True)