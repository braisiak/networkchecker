from flask import Flask, render_template, url_for
import socket
from requests import get
import subprocess

app = Flask(__name__)

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('https://api.ipify.org').text

@app.route('/')
def index():
    return render_template('index.html', variable = local_ip, variable2 = public_ip)

@app.route('/login/')
def signIn():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)