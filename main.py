import os
from flask import Flask, request, jsonify
import requests
import datetime

app = Flask(__name__)

OUTSYSTEMS_API_URL = "https://personal-ejiszdmu.outsystemscloud.com/ASISTENCIA/rest/RESTAPI1/RESTAPIPOST"


@app.route("/receive/iclock/cdata", methods=["GET", "POST"])
def iclock():

    print("METHOD:", request.method)
    print("ARGS:", request.args)
    print("FORM:", request.form)
    print("DATA:", request.data)

    # El dispositivo primero hace GET (handshake)
    if request.method == "GET":
        return "OK"

    # Cuando hace POST, vienen los registros
    if request.method == "POST":

        raw_data = request.data.decode("utf-8")
        print("RAW DATA:", raw_data)

        # Aquí luego parsearemos los datos
        return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
