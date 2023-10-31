from flask import Flask,render_template,request,redirect,url_for,session
#from flask_mysqldb import MySQL
import MySQLdb
import MySQLdb.cursors
import re
#importing modules above

app = Flask(__name__)

#mysql = MySQLdb(app)

@app.route('/')

#@app.route('/login',methods = ['GET','POST'])

def main():
    return render_template('index.html')
if __name__ == '__main__':
    app.run()

@app.route('/books')
def booklisting():
    return render_template('books.html')

    





