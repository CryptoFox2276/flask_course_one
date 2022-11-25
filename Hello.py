from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/aadmin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

if __name__ == '__main__':
    app.run()
    