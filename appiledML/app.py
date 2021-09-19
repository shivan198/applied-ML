from flask import Flask,render_template, request, session, Response
# from werkzeug import secure_filename
# from flask_session import Session
import io
import random
from algorithms import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import json
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model, metrics

app = Flask(__name__)
app.secret_key = "any random string"

@app.route('/')
def upload_file():
   return render_template('fileupload.html')
	
@app.route('/uploader', methods = ['GET','POST'])
def uploader():
    fname=request.form.get("filename")
    MLtype=request.form.get("algotype")
    df = pd.read_csv(fname,header=None)
    session["df"]=df.to_json()
    # print(df.to_json())
    session["MLtype"]=MLtype
    print(fname)
    print(MLtype)
#    if request.method == 'POST':
#       f = request.files['file']
#     #   f.save(secure_filename(f.filename))
    return render_template('SecondPage.html')


# @app.route('/linear',  methods = ['GET','POST'])
# def linear():
#     automate=request.form.get("automate")
#     session["automate"]=automate
#     print(session["automate"])
#     return render_template('linear.html',auto=automate)

@app.route('/linearregression',  methods = ['GET','POST'])
def linearregression():
    automate=request.form.get("automate")
    # automate=session["automate"]
    # if(automate=="yes"):
    #     alpha=0.2
    #     epochs=30
    # else:
    #     alpha = request.form.get("alpha")
    #     epochs = request.form.get("epoch")
    #     print(alpha, epochs)
    
    # session["testdata"]=data.to_json()
    df=session["df"]
    df=pd.read_json(df)
    df = pd.concat([pd.Series(1,index = df.index,name='00'),df],axis=1)
    drop_col = len(df.columns)-2
    X = df.drop(columns=drop_col)
    y = df.iloc[:,-1]
    # for i in range(1,len(X.columns)):
    #     X[i-1] = X[i-1]/np.max(X[i-1])
    # theta = np.array([0]*len(X.columns))
    print("@@@@@@@@@@@@@ in linear regression")
    reg = linear_model.LinearRegression()
    reg.fit(X,y)
    # data = session['testdata']
    test_file=request.form.get("filename")
    data = pd.read_csv(test_file,header=None)
    data_n2 = data.values
    m2 = len(data_n2)
    data = pd.concat([pd.Series(1,index = data.index,name='00'),data],axis=1)
    # data = pd.read_json(data)
    ypred = reg.predict(data)
    data = pd.DataFrame(data)   
    # print(session["automate"])
    if(request.method == ['GET']):
        output = io.BytesIO()
        FigureCanvas(plt).print_png(output)
        img=Response(output.getvalue(), mimetype='image/png')
        return render_template('linear.html',img=img)

    x=data.values.tolist()
    print("@@@@@@@@@@@@@@@@@@@@@ x value = ",x)
    print("@@@@@@@@@@@@@ y value = ",y)
    return render_template('linear.html',auto=automate,xy = zip(x,ypred))

@app.route('/classi', methods = ['GET','POST'])
def classi():
    x=request.form.get("classi")
    y=request.form.get("automate")
    # print(x,y)
    return render_template('fileupload.html')


@app.route('/select', methods = ['GET','POST'])
def select():
    x=request.form.get("select")
    if(x=="shape"):
        df=session["df"]
       
        df=pd.read_json(df)
        # print(":////////////",df.shape)
        y=df.shape
        return render_template('SecondPage.html', tup=str(y),flag=1)
        # return str(y)
    # if(x=="desc"):
    #     df=session["df"]
       
    #     df=pd.read_json(df)
        
    #     y=df.describe()
    #     print("://////////// describe",y)
    #     print(len(y))
    #     print(len(y.columns))
    #     for i i
    #     return render_template('SecondPage.html',table1=y, flag=2)
    if(x=="predict"):
        if(session["MLtype"]=="Classification"):
            return render_template('SecondPage.html',flag=3) 
        else:
            return render_template('SecondPage.html',flag=4)


    # print(x)
    # return x

if __name__ == '__main__':
   app.run(debug = True)