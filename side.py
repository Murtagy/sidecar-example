import os
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def perform_action():
    # For demonstration purposes, let's just print a message
    print("Sidecar: Performing the requested action")
    return "Action performed by sidecar"

if __name__ == '__main__':
    port = os.environ['PORT']
    app.run(port=port)

