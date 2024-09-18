from flask import Flask,render_template
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


@app.route('/h1')
def fun4():
    a='welcome'
    return render_template("index.html",a=a)
@app.route('/first')
def fun5():
    return render_template("first.html")


@app.route('/second')
def fun6():
    return render_template("second.html")



@app.route('/third')
def fun7():
    return render_template("third.html")
app.run()