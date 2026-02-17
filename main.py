import os
from flask import Flask, request, jsonify
import requests
import datetime

app = Flask(__name__)

OUTSYSTEMS_API_URL = "https://personal-ejiszdmu.outsystemscloud.com/ASISTENCIA/rest/RESTAPI1/RESTAPIPOSTBIO"

@app.route("/iClockAPI/cdata", methods=["POST"])
def receive():
    try:
        data = request.get_json()
        timestamp = datetime.datetime.now().isoformat()
        with open("logs.txt", "a") as f:
            f.write(f"{timestamp} - Recibido: {data}\n")
        response = requests.post(OUTSYSTEMS_API_URL, json=data)
        with open("logs.txt", "a") as f:
            f.write(f"{timestamp} - Enviado a OutSystems: {response.status_code}\n")
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        with open("logs.txt", "a") as f:
            f.write(f"{datetime.datetime.now().isoformat()} - ERROR: {str(e)}\n")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render asigna un puerto automáticamente
    app.run(host="0.0.0.0", port=port)
