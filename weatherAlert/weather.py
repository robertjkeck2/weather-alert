import requests
import json


API_KEY = 'WUNDERGROUND_API_KEY'
FORECAST_HOURS = 8

class HourlyWeather(object):

	def __init__(self, locations):
		self.locations = locations
		self.base_url = 'http://api.wunderground.com/api/'

	def request_api(self, api_endpoint):
		url = '{0}{1}{2}{3}/{4}.json'.format(self.base_url, 
			API_KEY,
			api_endpoint, 
			self.locations[1],
			self.locations[0])
		respone = requests.get(url).json()
		return respone

	def hourly(self):
		api_endpoint = '/hourly/q/'
		response = self.request_api(api_endpoint)
		weather = []
		hours = []
		for i in range(0,FORECAST_HOURS):
			time = response["hourly_forecast"][i]["FCTTIME"]["civil"]
			condition = response["hourly_forecast"][i]["condition"]
			if i == 0:
				weather.append(condition)
				hours.append(time)
			else:
				prev_condition = response["hourly_forecast"][i-1]["condition"]
				prev_time = response["hourly_forecast"][i-1]["FCTTIME"]["civil"]
				if (condition != prev_condition):
					if i == 1:
						hours.append(time)
					else:
						hours.append(prev_time)
					weather.append(condition)
				elif (i == (FORECAST_HOURS - 1)):
					hours.append(time)
		
		forecast = []
		for j in range(0,len(hours) - 1):
			forecast.append('{} to {}'.format(hours[j], hours[j+1]))

		formatted_forecast = []
		for k in range(0,len(forecast)):
			formatted_forecast.append((forecast[k], weather[k]))
		
		return formatted_forecast
