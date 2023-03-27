from flask import Flask, request, abort
import requests
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = json.loads(request.data)
        event = data['event']
        print(event)
        return 'success', 200
    else:
        abort(400)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
