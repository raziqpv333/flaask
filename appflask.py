from flask import Flask,render_template,request
app=Flask(__name__)


import sqlite3
# connection=sqlite3.connect('data.db')
# connection.execute('create table datatable(name text,place text,age int,id int)')


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


@app.route('/form',methods=['POST','GET'])
def fun8():
    if request.method=='POST':
        name=request.form['name']
        id=int (request.form['id'])
        place=request.form['place']
        age=int (request.form['age'])
        connection=sqlite3.connect('data.db')
        connection.execute("insert into datatable(name,place,id,age)values(?,?,?,?)",(name,place,id,age))
        connection.commit()



    return render_template("form.html")

@app.route('/display')
def fun9():
    connection=sqlite3.connect('data.db')
    data=connection.execute("select * from datatable")
    return render_template("display.html",data=data)




@app.route('/update/<id>',methods=['POST','GET'])
def fun10(id):
    connection=sqlite3.connect('data.db')
    data=connection.execute("select * from datatable where id=?",(id,))
    if  request.method=='POST':
        name=request.form['name']
        place=request.form['place']
        age=int(request.form['age'])
        connection.execute("update datatable set name=?,age=?,place=? where id=?",(name,age,place,id))
        connection.commit()
    return render_template("update.html",data=data)  





@app.route('/delete')
def fun11():
    connection=sqlite3.connect('data.db')
    connection.execute("delete from datatable whre id=?",(id,))
    connection.commit()
    return render_template("display.html")      
app.run()