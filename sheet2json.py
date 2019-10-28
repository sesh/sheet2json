import requests
from flask import Flask, jsonify, make_response


app = Flask(__name__)


@app.route("/")
def home():
    return "Nothing to see here."


@app.route("/<string:sheet_id>/<int:sheet>")
def metaicon(sheet_id, sheet):
    sheet_url = f"https://spreadsheets.google.com/feeds/list/{sheet_id}/{sheet}/public/values?alt=json"
    response = requests.get(sheet_url)
    data = response.json()

    rows = []
    for entry in data["feed"]["entry"]:
        row = {}
        for k in entry:
            if k.startswith("gsx$"):
                title = k[4:]
                value = entry[k]["$t"]
                row[title] = value

        rows.append(row)

    return make_response(
        jsonify({"rows": rows}), 200, {"Access-Control-Allow-Origin": "*"}
    )
