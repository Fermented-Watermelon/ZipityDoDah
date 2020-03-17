from flask import Flask, request, abort, render_template, flash, send_file
from flask import redirect, request, jsonify, url_for, make_response
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload():
    isthisFile=request.files.get('file')
    isthisFile.save("./"+isthisFile.filename)
    print("file saved")
    return("FUCKYOOOU")


@app.route('/')
def runweb():
    return render_template("index.html")

if __name__ == '__main__':
    
    app.run(port='80',debug=True)