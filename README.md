# Weather Alert
Using Wunderground API to alert of inclement weather conditions

##Purpose
weatherAlert sends an alert via slack notification when non-standard weather events are occurring in a specified locale. The alert is useful in proactive notification of rain/snow/thunderstorms to plan for the conditions ahead of time.  Run with a cronjob, this currently notifies of weather three times throughout the day.

##Instructions
1. Edit 'dd_midwest_alert.py' file to update the 'locations' list to include desired locales.
2. Go to https://[your-slack-domain].slack.com/apps/manage/custom-integrations and click on Incoming Webhooks.
3. Click add configuration to create a new incoming webhook.
4. Choose a channel to notify with the weather updates and copy the webhook url.
5. Edit 'alert.py' file to update the 'webhook_url' string to the copied webhook url.
6. Go to https://www.wunderground.com/weather/api/ and create an account to get an API key.
7. Edit 'weather.py' file to update the 'API_KEY' string to the API key received from Wunderground.
8. Set up cronjob to run 'dd_midwest_alert.py' every 6 hours.
9. Check the slack channel chosen in step 4 for weather notifications.

##Possible Usage
- Change operational metrics for companies that have fluctuations due to poor weather
- Decide what to wear when you go out that evening without having to check a weather app
- Notify a operations team of weather in other areas of the country so they can plan accordingly
