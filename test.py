from app import app
import os
import unittest
import app
from unittest.mock import Mock, MagicMock

mockForecast={"forecasts":[{"day":"2024-06-27","sailing_condition_10":"rough","sailing_condition_11":"too-calm","sailing_condition_12":"too-calm","sailing_condition_13":"too-calm","sailing_condition_14":"rough","sailing_condition_15":"rough","sailing_condition_16":"rough","sailing_condition_7":"rough","sailing_condition_8":"rough","sailing_condition_9":"rough","temp_10":86.2,"temp_11":86.2,"temp_12":86.9,"temp_13":87.6,"temp_14":88.0,"temp_15":87.8,"temp_16":86.4,"temp_7":81.7,"temp_8":82.8,"temp_9":84.6},{"day":"2024-06-28","sailing_condition_10":"rough","sailing_condition_11":"rough","sailing_condition_12":"rough","sailing_condition_13":"rough","sailing_condition_14":"rough","sailing_condition_15":"rough","sailing_condition_16":"rough","sailing_condition_7":"rough","sailing_condition_8":"rough","sailing_condition_9":"rough","temp_10":86.5,"temp_11":79.7,"temp_12":80.8,"temp_13":81.7,"temp_14":82.6,"temp_15":86.5,"temp_16":83.7,"temp_7":82.9,"temp_8":83.8,"temp_9":85.1},{"day":"2024-06-29","sailing_condition_10":"rough","sailing_condition_11":"rough","sailing_condition_12":"rough","sailing_condition_13":"rough","sailing_condition_14":"rough","sailing_condition_15":"rough","sailing_condition_16":"rough","sailing_condition_7":"rough","sailing_condition_8":"rough","sailing_condition_9":"rough","temp_10":86.4,"temp_11":85.3,"temp_12":80.6,"temp_13":81.7,"temp_14":82.6,"temp_15":86.5,"temp_16":86.5,"temp_7":84.6,"temp_8":84.7,"temp_9":85.3},{"day":"2024-06-30","sailing_condition_10":"rough","sailing_condition_11":"rough","sailing_condition_12":"rough","sailing_condition_13":"rough","sailing_condition_14":"rough","sailing_condition_15":"rough","sailing_condition_16":"rough","sailing_condition_7":"rough","sailing_condition_8":"rough","sailing_condition_9":"rough","temp_10":86.5,"temp_11":85.8,"temp_12":81.1,"temp_13":82.0,"temp_14":82.9,"temp_15":83.7,"temp_16":83.8,"temp_7":84.2,"temp_8":85.1,"temp_9":85.8},{"day":"2024-07-01","sailing_condition_10":"rough","sailing_condition_11":"rough","sailing_condition_12":"too-calm","sailing_condition_13":"too-calm","sailing_condition_14":"too-calm","sailing_condition_15":"rough","sailing_condition_16":"rough","sailing_condition_7":"rough","sailing_condition_8":"rough","sailing_condition_9":"rough","temp_10":87.6,"temp_11":81.3,"temp_12":83.5,"temp_13":90.0,"temp_14":91.0,"temp_15":91.2,"temp_16":90.7,"temp_7":81.5,"temp_8":83.5,"temp_9":85.5}],"length":20,"location":"Houston"}


class TestStringMethods(unittest.TestCase):
   
   def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        mock = Mock()  
        mock.app.health.return_value = "NOPE"


   def test_health(self):
     rv = self.app.get('/health_check')
     self.assertEqual(rv.get_data(as_text=True), 'OK')
   

  #intgration test
   def test_get_forecast(self):
     app.get_forecast = Mock()
     app.get_forecast.return_value = mockForecast
     out = app.get_forecast()
     forecastArray = out
     self.assertEqual(len(forecastArray['forecasts']),5)

   def test_healthz(self):
     rv = self.app.get('https://yahoo.com')
     self.assertEqual(rv.get_data(as_text=True), 'OK')
