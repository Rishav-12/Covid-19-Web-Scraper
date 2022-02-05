import requests
from bs4 import BeautifulSoup
import json

def scrape():

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

		return covid_data

	except Exception:
		return None

if __name__ == "__main__":
	covid_data = scrape()

	if covid_data is not None:
		print("Fetched data...dumping to file")
		with open("covid_data.json", "w") as file:
			json.dump(covid_data, file)
	else:
		print("Something went wrong. Could not fetch data")
