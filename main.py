# Import libraries
import flask

# Define variables
PORT = 5000
METHODS = ["GET"]
app = flask.Flask(__name__)


# Define the route
@app.route("/", methods=METHODS)
def send_data():
    return {
        "total_requests": 90000,
        "concurrent_requests": 1000,
        "method": "GET",
        "target_url": "https://www.hola.com",
        "wait_time": 5,
        "timeout": 30,
    }
