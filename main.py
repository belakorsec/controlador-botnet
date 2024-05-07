# Import libraries
import flask

# Define variables
PORT = 5000
METHODS = ["GET"]
app = flask.Flask(__name__)


# Define the route
@app.route("/", methods=METHOD)
def send_data():
    return {
        "total_requests": input_data,
        "concurrent_requests": 10,
        "method": "GET",
        "target_url": "https://www.hola.com",
        "wait_time": 5,
        "timeout": 30,
    }


# Run the app
if __name__ == "__main__":
    app.run(port=PORT)
