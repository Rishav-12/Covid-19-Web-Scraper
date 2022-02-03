from plyer import notification
import time
import requests
from bs4 import BeautifulSoup
import json

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

	URL = "https://www.worldometers.info/coronavirus/country/india/"
	try:
		r = requests.get(URL).text # Requesting some data from the given url
		soup = BeautifulSoup(r, 'html.parser')

		myData = soup.find_all('div')[5].text.strip() # Fetching all the required data
		x = myData.split('\n')

		while "" in x:
			x.remove("")

		data = []
		# Cleaning the data to filter out only the information which is needed
		data.extend(x[2].split(": "))
		for i in range(4, 10):
			data.append(x[i].strip())

		covid_data = {}

		# Building a dictionary
		covid_data["last updated"] = data[1]
		covid_data["cases"] = data[3]
		covid_data["deaths"] = data[5]
		covid_data["recovered"] = data[7]

		with open("covid_data.json", "w") as file:
			json.dump(covid_data, file)

		# contents = [data[i]+data[i+1] for i in range(0, 5, 2)]
		# print("\n".join(contents))
		# notifyMe("\n".join(contents)) # Display the information in the desired format

	except Exception:
		print("Something went wrong. Could not fetch data")
		# notifyMe("Something went wrong. Could not fetch data")
