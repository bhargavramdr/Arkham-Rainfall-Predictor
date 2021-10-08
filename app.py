from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)

model = pickle.load(open("models/model.pkl", "rb"))


@app.route("/", methods=['Get'])
def Home():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':

        Location = request.form['Location']
        if(Location == 'Albury'):
            Location = float(2)
        elif(Location == 'BadgerysCreek'):
            Location = float(4)
        elif(Location == 'Cobar'):
            Location = float(10)
        elif(Location == 'CoffsHarbour'):
            Location = float(11)
        elif(Location == 'Moree'):
            Location = float(21)
        elif(Location == 'Newcastle'):
            Location = float(24)
        elif(Location == 'NorahHead'):
            Location = float(26)
        elif(Location == 'NorfolkIsland'):
            Location = float(27)
        elif(Location == 'Penrith'):
            Location = float(30)
        elif(Location == 'Richmond'):
            Location = float(34)
        elif(Location == 'Sydney'):
            Location = float(37)
        elif(Location == 'SydneyAirport'):
            Location = float(38)
        elif(Location == 'WaggaWagga'):
            Location = float(42)
        elif(Location == 'Williamtown'):
            Location = float(45)
        elif(Location == 'Wollongong'):
            Location = float(47)
        elif(Location == 'Canberra'):
            Location = float(9)
        elif(Location == 'Tuggeranong'):
            Location = float(40)
        elif(Location == 'MountGinini'):
            Location = float(23)
        elif(Location == 'Ballarat'):
            Location = float(5)
        elif(Location == 'Bendigo'):
            Location = float(6)
        elif(Location == 'Sale'):
            Location = float(35)
        elif(Location == 'MelbourneAirport'):
            Location = float(9)
        elif(Location == 'Melbourne'):
            Location = float(40)
        elif(Location == 'Mildura'):
            Location = float(23)
        elif(Location == 'Nhil'):
            Location = float(5)
        elif(Location == 'Portland'):
            Location = float(6)
        elif(Location == 'Watsonia'):
            Location = float(35)

        MinTemp = float(request.form['MinTemp'])
        MaxTemp = float(request.form['MaxTemp'])

        Sunshine = float(request.form['Sunshine'])

        WindGustDir = request.form['WindGustDir']
        if(WindGustDir == 'North'):
            WindGustDir = float(10)
        elif(WindGustDir == 'South'):
            WindGustDir = float(5)
        elif(WindGustDir == 'East'):
            WindGustDir = float(2)
        elif(WindGustDir == 'West'):
            WindGustDir = float(13)
        elif(WindGustDir == 'NE'):
            WindGustDir = float(4)
        elif(WindGustDir == 'NW'):
            WindGustDir = float(0)
        elif(WindGustDir == 'SE'):
            WindGustDir = float(7)
        elif(WindGustDir == 'SW'):
            WindGustDir = float(3)
        elif(WindGustDir == 'WNW'):
            WindGustDir = float(14)
        elif(WindGustDir == 'WSW'):
            WindGustDir = float(15)
        elif(WindGustDir == 'NNW'):
            WindGustDir = float(12)
        elif(WindGustDir == 'NNE'):
            WindGustDir = float(8)
        elif(WindGustDir == 'ENE'):
            WindGustDir = float(6)
        elif(WindGustDir == 'SSE'):
            WindGustDir = float(9)
        elif(WindGustDir == 'ESE'):
            WindGustDir = float(11)
        elif(WindGustDir == 'SSW'):
            WindGustDir = float(1)

        WindGustSpeed = float(request.form['WindGustSpeed'])

        WindDir9am = request.form['WindDir9am']
        if(WindDir9am == 'North'):
            WindDir9am = float(10)
        elif(WindDir9am == 'South'):
            WindDir9am = float(5)
        elif(WindDir9am == 'East'):
            WindDir9am = float(2)
        elif(WindDir9am == 'West'):
            WindDir9am = float(13)
        elif(WindDir9am == 'NE'):
            WindDir9am = float(4)
        elif(WindDir9am == 'NW'):
            WindDir9am = float(0)
        elif(WindDir9am == 'SE'):
            WindDir9am = float(7)
        elif(WindDir9am == 'SW'):
            WindDir9am = float(3)
        elif(WindDir9am == 'WNW'):
            WindDir9am = float(14)
        elif(WindDir9am == 'WSW'):
            WindDir9am = float(15)
        elif(WindDir9am == 'NNW'):
            WindDir9am = float(12)
        elif(WindDir9am == 'NNE'):
            WindDir9am = float(8)
        elif(WindDir9am == 'ENE'):
            WindDir9am = float(6)
        elif(WindDir9am == 'SSE'):
            WindDir9am = float(9)
        elif(WindDir9am == 'ESE'):
            WindDir9am = float(11)
        elif(WindDir9am == 'SSW'):
            WindDir9am = float(1)

        WindDir3pm = request.form['WindDir3pm']
        if(WindDir3pm == 'North'):
            WindDir3pm = float(10)
        elif(WindDir3pm == 'South'):
            WindDir3pmm = float(5)
        elif(WindDir3pm == 'East'):
            WindDir3pm = float(2)
        elif(WindDir3pm == 'West'):
            WindDir3pm = float(13)
        elif(WindDir3pm == 'NE'):
            WindDir3pm = float(4)
        elif(WindDir3pm == 'NW'):
            WindDir3pm = float(0)
        elif(WindDir3pm == 'SE'):
            WindDir3pm = float(7)
        elif(WindDir3pm == 'SW'):
            WindDir3pm = float(3)
        elif(WindDir3pm == 'WNW'):
            WindDir3pm = float(14)
        elif(WindDir3pm == 'WSW'):
            WindDir3pm = float(15)
        elif(WindDir3pm == 'NNW'):
            WindDir3pm = float(12)
        elif(WindDir3pm == 'NNE'):
            WindDir3pm = float(8)
        elif(WindDir3pm == 'ENE'):
            WindDir3pm = float(6)
        elif(WindDir3pm == 'SSE'):
            WindDir3pm = float(9)
        elif(WindDir3pm == 'ESE'):
            WindDir3pm = float(11)
        elif(WindDir3pm == 'SSW'):
            WindDir3pm = float(1)

        WindSpeed9am = float(request.form['WindSpeed9am'])

        WindSpeed3pm = float(request.form['WindSpeed3pm'])
        Humidity9am = float(request.form['Humidity9am'])
        Humidity3pm = float(request.form['Humidity3pm'])

        Cloud3pm = float(request.form['Cloud3pm'])
        Temp9am = float(request.form['Temp9am'])
        Temp3pm = float(request.form['Temp3pm'])

        Par = np.array([[Location, MinTemp, MaxTemp, Sunshine, WindGustDir,
                       WindGustSpeed, WindDir9am, WindDir3pm, WindSpeed9am, WindSpeed3pm, Humidity9am,
                         Humidity3pm, Cloud3pm, Temp9am, Temp3pm]])

        prediction = model.predict(Par)

        if prediction == float(0):
            return render_template('index.html', prediction_texts="There won't be rain tomorrow")
            # return "Something is wrong"
        else:
            return render_template('index.html', prediction_text="There's a high chance of rain tomorrow")
            # return "Something is wrong_1"
    else:
        # return "Something is not right"
        return render_template('index.html')


# @app.route("/submit")
# def submit():
#     if request.method == "POST":
#         name = request.form["username"]

#     return render_template("submit.html", n=name)


if __name__ == "__main__":
    app.run(debug=True)
