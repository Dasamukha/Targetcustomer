import pickle
import requests
from flask import Flask, render_template,request
# import streamlit as st

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods = ['GET','POST'])
def predit():
    income = request.form.get('income')
    spendi =  request.form.get('spend')
    ans = model.predict([[income,spendi]])
    if ans == 0 :
         pred = 'Careless'
    elif ans == 1:
        pred = 'Standard'
    elif ans == 2:
        pred = 'Target'
    elif ans == 3:
        pred = 'Sensible'
    elif ans == 4:
        pred = 'Careful'
    else:
        print('Unable to predict model need more data')
        # print(prediction)
    
    if ans == 0 :
         text = 'This Group is a Careless Group Because their spending is High and their Annual Income is Low '
         text1 = 'Can Fall for any Marketing Scheme'
    elif ans == 1:
        text = 'This Group is a Standard Group,Because their spending is Average and their Annual Income is Average'
        text1 ='Need a good Marketing Scheme to make Customer Buy'
    elif ans == 2:
        text = 'This Group is Our Target Group, Because their spending is High and their Annual Income is High'
        text1 ='They can buy High Value Goods '
    elif ans == 3:
        text = 'This Group is Our Sensible Group, Because their spending is Low and their Annual Income is Low'
        text1 = 'They are less effected by Marketing Scheme'
    elif ans == 4:
        text = 'This Group is Our Careful Group, Because their spending is Low and their Annual Income is High'
        text1 = 'They need a good Marketing Scheme or offer to make them Attract '
    else:
        print('Unable to predict model need more data')

    
    return render_template('index.html',ptext ={pred},ptext1={text},ptext2={text1})

if  __name__=='__main__':
    app.run(debug = True)


