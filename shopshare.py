import os 
from flask import Flask, redirect, render_template, request 

app = Flask(__name__)

shopping_list = {
        'Nottingham': {
            'user': "Haley",
            'items':  [{
                'user': "Haley",
                'food': "Bread",
            },
            {
                'user': 'Claire',
                'food': 'TP',
            },
            {
                'user': 'Meabh',
                'food': 'pasta',
            }]
        }
    }

@app.route('/')
def get_homepage():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login(): 
    group = request.form['group']
    username = request.form['username']
    return redirect("/" + group + "/" + username) 
# Pass two arguments through redirect without having to make an extra page 


@app.route('/<group>/<username>')
def get_user_page(group, username):
    return render_template('chat_page.html', group = group, username = username, shop_items = shopping_list[group]['items'])
    

    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug = True)


