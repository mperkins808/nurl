from http.server import SimpleHTTPRequestHandler, HTTPServer
import socketserver
import os
from flask import Flask, jsonify, request 
import base64
import subprocess

def call_curl(curl):
    msg = curl #cant verify certs for some reason
    output = subprocess.check_output(msg, shell=True)
    return output

app = Flask(__name__)

@app.route('/cmd', methods=['POST'])
def curlEndpoint():
    body = request.json
    resp = call_curl(body["cmd"])
    return resp

@app.route('/healthy', methods=["GET"])
def healthy():
    return "200 OK"

if __name__ == '__main__':
    PORT = os.getenv('PYTHON_PORT')
    if PORT == None:
        PORT = 5000
    app.run(host="0.0.0.0",debug=True, port=PORT)