from http.server import SimpleHTTPRequestHandler, HTTPServer
import socketserver
import os
from flask import Flask, jsonify, request 

# def call_curl(curl):
#     msg = curl + ' -k' #cant verify certs for some reason
#     os.system(msg)

# def main():
#     Handler = SimpleHTTPRequestHandler
#     PORT = os.getenv('PYTHON_PORT')
#     if PORT == None:
#         PORT = 5000
#     with socketserver.TCPServer(("", PORT), Handler) as httpd:
#         print("Serving on port ", PORT)
#         httpd.serve_forever()
#         print("mangos")
#         curl = 'curl https://www.google.com.au'
#         call_curl(curl)

# if __name__ == '__main__':
#     main()

app = Flask(__name__)

@app.route('/curl', methods=['POST'])
def curlEndpoint():
    print(request.data)
    return "i am hid"

if __name__ == '__main__':
    PORT = os.getenv('PYTHON_PORT')
    if PORT == None:
        PORT = 5000
    app.run(debug=True, port=PORT)