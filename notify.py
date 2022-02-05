from plyer import notification
import time

from scraper import scrape

def notifyMe(message): # Function which notifies us every 3 hours
	while True:
		notification.notify(
			title = "COVID-19 Updates India",
			message = message,
			app_icon = "covid.ico",
			timeout = 10
			)

		time.sleep(3*60*60)

if __name__ == "__main__":
	json_data = scrape()

	if json_data is not None:
		content = f'''
		Total Cases: {json_data["cases"]}
		Deaths: {json_data["deaths"]}
		Recovered: {json_data["recovered"]}
		'''
		notifyMe(content)
	else:
		notifyMe("Something went wrong. Could not fetch data")
