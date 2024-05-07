import flask

app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def send_data():
    input_data = int(input("Total requests: "))
    data = {
        "total_requests": input_data,
        "concurrent_requests": 10,
        "method": "GET",
        "target_url": "https://www.hola.com",
        "wait_time": 5,
        "timeout": 30,
    }
    return data


if __name__ == "__main__":
    app.run(port=5000)
