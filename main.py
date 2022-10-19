from flask import Flask, request, render_template
import requests

app = Flask(__name__)

url = "https://api.openweathermap.org/data/2.5/weather?q="


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uri = request.form.get("weatherName")
        fullUrl = (
            url + uri + "&appid=51018b60257b50207fc63de7c53af5e1&units=metric&lang=tr"
        )
        data = requests.get(fullUrl)
        response = data.json()
        return render_template("weather.html", weather=response)
    else:
        return render_template("weather.html")


app.run(debug=True, host="0.0.0.0", port=81)
