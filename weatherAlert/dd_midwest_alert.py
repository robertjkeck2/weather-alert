from weather import HourlyWeather
from alert import Alert


locations = [
	("Indianapolis", "IN"),
	("Columbus", "OH"),
	("Seattle", "WA"),
	("Bellevue", "WA"),
	("Denver", "CO"),
	("Boulder", "CO"),
	("Minneapolis", "MN"),
	("Chicago", "IL")
]

for location in locations:
	forecast = HourlyWeather(location)
	weather = forecast.hourly() 

	alarm = Alert(weather, location)
	alarm.check_weather()