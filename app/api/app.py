import requests

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def weather_dashboard():
    return render_template('home.html')


@app.route('/results', methods=['POST'])
def render_results():
    zip_code = request.form['zipCode']

    api_key = '1ed60846df30dbb4908a0067ab18a9a6'
    data = get_weather_results(zip_code, api_key)
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]

    return render_template('results.html',
                           location=location, temp=temp,
                           feels_like=feels_like, weather=weather)


def get_weather_results(zip_code, api_key):
    api_url = "http://api.openweathermap.org/" \
              "data/2.5/weather?q={}&units=imperial&appid={}".format(zip_code, api_key)
    r = requests.get(api_url)
    return r.json()


if __name__ == '__main__':
    app.run()