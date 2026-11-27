
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "MJ License Server is running"


@app.route("/verify", methods=["POST"])
def verify():
    data = request.get_json(silent=True) or {}

    license_key = data.get("license_key")
    device_id = data.get("device_id")

    if not license_key or not device_id:
        return jsonify({
            "status": "error",
            "message": "Missing license_key or device_id"
        }), 400

    return jsonify({
        "status": "pending",
        "message": "License verification is not configured yet"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
