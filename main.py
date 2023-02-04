from http.server import SimpleHTTPRequestHandler, HTTPServer
import socketserver
import os
from flask import Flask, jsonify, request, send_file 
import base64
import subprocess

def call_curl(curl):
    msg = curl #cant verify certs for some reason
    output = subprocess.check_output(msg, shell=True)
    return output

app = Flask(__name__)

# API
@app.route('/cmd', methods=['POST'])
def curlEndpoint():
    print("Received command request")
    print("running command '" + request.json["cmd"] + "'")
    body = request.json
    resp = call_curl(body["cmd"])
    return resp

@app.route('/healthy', methods=["GET"])
def healthy():
    return '200 OK'

# HTML
@app.route('/', methods=['GET'])
def main():
    print("returning main page")
    return send_file('index.html')


if __name__ == '__main__':
    PORT = os.getenv('PYTHON_PORT')
    if PORT == None:
        PORT = 5000
    app.run(host="0.0.0.0",debug=True, port=PORT)