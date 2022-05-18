from flask import render_template, redirect, url_for, flash ,request
import requests
import urllib3

from post.weathers import City
from . import weather
from app import db



@weather.route('/weather', methods=['GET', 'POST'])
def city_weather():



    
        if request.method == 'POST':
            new_city = request.form.get('city')

        if new_city:
            new_city_obj = City(name=new_city)

            db.session.add(new_city_obj)
            db.session.commit()
            

        weather_data = []
        cities = City.query.all()
        for city in cities:

                r = requests.get(urllib3.format(city.name)).json()

                weather = {
                    'city' : city.name,
                    'temperature' : r['main']['temp'],
                    'description' : r['weather'][0]['description'],
                    'icon' : r['weather'][0]['icon'],
                }

                weather_data.append(weather)


        return render_template('weather.html', weather_data=weather_data) 
