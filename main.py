# Simple Weather App to Fetch Weather And Display the Result
from flask import Flask,render_template
import requests
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField


class data_city(FlaskForm):
    city=StringField('Enter the City Name')
    submit=SubmitField('Enter')

# API for Weather
URL='https://api.openweathermap.org/data/2.5/weather?'
API_KEY='3a52b9af65a66f3bfeaf3be464debfdb'

app  = Flask(__name__)
app.config['SECRET_KEY']='SECRET_KEY'

# Main Page
@app.route('/',methods=['GET','POST'])
def Home():
    form = data_city()
    return render_template('index.html',form=form)

# Result Page
@app.route('/weather',methods=['GET','POST'])
def weather():
    form = data_city()
    city_data = form.city.data
    response = requests.get(f'{URL}&appid={API_KEY}&q={city_data}')
    data = response.json()
    kelvin_temp = data['main']['temp']
    celsius_temp = kelvin_temp - 273.15
    celsius_temp_1=round(celsius_temp, 2)
    return render_template('weather.html',data=data,celsius_temp=celsius_temp_1)


if __name__=='__main__':
    app.run(debug=True)