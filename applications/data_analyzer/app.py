from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
<h1> Data Analizer </h1>
'''
