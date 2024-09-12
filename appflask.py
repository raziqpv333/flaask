from flask import Flask
app=Flask(__name__)

@app.route('/')
def fun1():
    return "haaai"

@app.route('/hello/<a>')
def fun2(a):
    return 'hai'  +a

@app.route('/data/<int:b>/<int:c>/<int:d>')    
def fun3(b,c,d):
    return 'print laargest number' >b>c>d
app.run()