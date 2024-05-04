from flask import Flask, Response

app = Flask(__name__)


@app.route("/")
def prueba():
    data = {
        "signal": False,
        "payload": {
            "total_requests": 90,
            "concurrent_requests": 10,
            "method": "GET",
            "target_url": "http://hola.com",
            "wait_time": 5,
            "timeout": 30,
        },
    }
    return data


if __name__ == "__main__":
    app.run(port=5000)
