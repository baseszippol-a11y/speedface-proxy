import os
from flask import Flask, request, jsonify
import requests
import datetime

app = Flask(__name__)

OUTSYSTEMS_API_URL = "https://personal-ejiszdmu.outsystemscloud.com/ASISTENCIA/rest/RESTAPI1/RESTAPIPOST"

@app.route("/receive/iclock/cdata", methods=["GET", "POST"])
def iclock():

    if request.method == "GET":
        return "OK"

    if request.method == "POST":

        raw_data = request.data.decode("utf-8").strip()
        lines = raw_data.split("\n")

        for line in lines:
            if line.strip() == "":
                continue

            parts = line.split()

            user_id = parts[0]
            fecha = parts[1]
            hora = parts[2]
            estado = parts[3]

            fecha_hora = f"{fecha} {hora}"

            data_outsystems = {
                "UserId": user_id,
                "PunchTime": fecha_hora,
                "Status": estado
            }

            print("Enviando a OutSystems:", data_outsystems)

            response = requests.post(
                OUTSYSTEMS_API_URL,
                json=data_outsystems
            )

            print("Respuesta OutSystems:", response.status_code)

        return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
