import json
import requests

from conditions import CONDITIONS


class Alert(object):

	def __init__(self, weather, location):
		self.weather = weather
		self.location = location

	def check_weather(self):
		for hour in self.weather:
			for condition in CONDITIONS:
				if hour[1] == condition:
					self.alert_message(hour)

	def alert_message(self, hour):
		msg = "{0} from {1} in {2}".format(hour[1], hour[0], self.location[0])
		self.send_alert(msg)

	def send_alert(self, msg):
		webhook_url = 'PATH/TO/SLACK/INCOMING/WEBHOOK/URL'
		payload = {
			"username": "Midwest Weather Bot",
			'icon_emoji': ":umbrella:",
			"text": msg
		}

		response = requests.post(webhook_url, json=payload)
