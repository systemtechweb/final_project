#!/usr/bin/env python4
import requests
from flask import Flask, render_template, request, url_for, redirect
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

mockResponse = {"forecasts":[{"day":"2024-06-27","sailing_condition_10":"rough","sailing_condition_11":"rough","sailing_condition_12":"rough","sailing_condition_13":"rough","sailing_condition_14":"rough","sailing_condition_15":"rough","sailing_condition_16":"rough","sailing_condition_7":"too-calm","sailing_condition_8":"rough","sailing_condition_9":"rough","temp_10":72.7,"temp_11":69.8,"temp_12":69.4,"temp_13":68.7,"temp_14":67.3,"temp_15":66.0,"temp_16":65.7,"temp_7":67.6,"temp_8":69.4,"temp_9":71.2},{"day":"2024-06-28","sailing_condition_10":"rough","sailing_condition_11":"rough","sailing_condition_12":"rough","sailing_condition_13":"rough","sailing_condition_14":"rough","sailing_condition_15":"rough","sailing_condition_16":"rough","sailing_condition_7":"rough","sailing_condition_8":"rough","sailing_condition_9":"rough","temp_10":73.2,"temp_11":70.7,"temp_12":70.0,"temp_13":68.5,"temp_14":67.3,"temp_15":66.4,"temp_16":65.5,"temp_7":67.1,"temp_8":69.6,"temp_9":71.6},{"day":"2024-06-29","sailing_condition_10":"too-calm","sailing_condition_11":"rough","sailing_condition_12":"rough","sailing_condition_13":"rough","sailing_condition_14":"rough","sailing_condition_15":"rough","sailing_condition_16":"rough","sailing_condition_7":"too-calm","sailing_condition_8":"too-calm","sailing_condition_9":"too-calm","temp_10":72.9,"temp_11":70.9,"temp_12":70.2,"temp_13":69.6,"temp_14":69.4,"temp_15":69.6,"temp_16":69.6,"temp_7":66.6,"temp_8":68.9,"temp_9":70.9},{"day":"2024-06-30","sailing_condition_10":"rough","sailing_condition_11":"rough","sailing_condition_12":"rough","sailing_condition_13":"rough","sailing_condition_14":"rough","sailing_condition_15":"rough","sailing_condition_16":"rough","sailing_condition_7":"too-calm","sailing_condition_8":"too-calm","sailing_condition_9":"too-calm","temp_10":77.4,"temp_11":69.8,"temp_12":70.5,"temp_13":71.4,"temp_14":72.1,"temp_15":72.9,"temp_16":73.6,"temp_7":71.2,"temp_8":74.1,"temp_9":76.3},{"day":"2024-07-01","sailing_condition_10":"rough","sailing_condition_11":"rough","sailing_condition_12":"rough","sailing_condition_13":"rough","sailing_condition_14":"rough","sailing_condition_15":"rough","sailing_condition_16":"rough","sailing_condition_7":"rough","sailing_condition_8":"rough","sailing_condition_9":"rough","temp_10":76.1,"temp_11":73.0,"temp_12":72.3,"temp_13":70.7,"temp_14":69.3,"temp_15":68.5,"temp_16":67.5,"temp_7":70.2,"temp_8":72.9,"temp_9":74.8}],"length":20,"location":"Los Angeles"}


metrics = PrometheusMetrics(app)

metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")

@app.route("/flask-prometheus-grafana-example/")
def hello():
    return jsonify(say_hello())
def say_hello():
    return {"message": "hello"}



@app.route("/")
def fr():
     return render_template("index.html")

@app.route("/health_check")
def health():
   return "OK"

@app.route("/metricsd")
def metrics():
  return "OK"

@app.route("/template")
def test():
   payload = mockResponse.json()
   return render_template("grid.html",city=payload.location, length=20 ) 
   return "You entered: " 


@app.route("/get_forecast", methods=["POST"])
def get_forecast():
    #https://svs-data-analyzer-35d8f53ed4b0.herokuapp.com/get_forecast
    print(request)
    print(request.form)
    headers = {
        'Content-Type': 'application/json',
    }    
    input_text = request.form['boat_length']
    input_city = request.form['city'] 
    body = {"city":input_city ,"length":input_text} 
    #response = requests.post('http://127.0.0.1:5000/get_forecast', json=body, headers=headers)
    response = requests.post('https://svs-data-analyzer-35d8f53ed4b0.herokuapp.com/get_forecast', json=body, headers=headers)
    #forecast_response = response.json()
    print(response)
    print(response.json())
    forecastArray = response.json()
    print('count')
    print(len(forecastArray['forecasts']))
    print(type(forecastArray['forecasts']))
    return render_template("grid.html",city=input_city, length=input_text, forecasts=forecastArray['forecasts'] )
    return "You entered: " + input_text + " " +input_city 

