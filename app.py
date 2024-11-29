from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "4f7087ef99c031d46269daca88d8de92"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    city = request.form.get("city")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "latitude": data["coord"]["lat"],
            "longitude": data["coord"]["lon"]
        }
        return render_template("index.html", weather=weather_data)
    else:
        error = "Ciudad no encontrada. Inténtalo de nuevo."
        return render_template("index.html", error=error)

@app.route("/cv.html")
def cv():
    return render_template("cv.html")

if __name__ == "__main__":
    app.run(debug=True)
