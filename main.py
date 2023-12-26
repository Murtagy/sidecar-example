import requests
import os

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def perform_action():
    # proxy request to the sidecar
    address = os.environ['SIDECAR'] 
    rq = requests.get('http://'+address)
    print(rq.text)
    return rq.text

if __name__ == '__main__':
    app.run(port=80)

