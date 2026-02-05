from flask import Flask

import time

app = Flask(__name__)

@app.route("/")

def home():

    time.sleep(2)  # artificial latency

    return "Hello from AWS AIOps Demo"

@app.route("/crash")

def crash():

    while True:

        pass  # CPU spike

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)

