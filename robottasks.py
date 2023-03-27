from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    event_type = data["event_type"]
    if event_type in ["process run", "Step run", "assistant run", "Robot run agent"]:
        # Replace "ITS_Enable" with the name of your assistant robot
        robot_name = "ITS_Enable"
        response = requests.post(f"https://api.robocorp.com/start-run/{robot_name}", json=data)
        if response.status_code == 200:
            return "Robot run started."
        else:
            return f"Failed to start robot run. Error: {response.text}", 500
    else:
        return f"Unsupported event type: {event_type}", 400

if __name__ == "__main__":
    app.run(host='0.0.0.0')
