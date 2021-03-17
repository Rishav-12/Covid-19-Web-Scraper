from plyer import notification
import time
import requests
from bs4 import BeautifulSoup

def notifyMe(message): # Function which notifies us every 3 hours
	while True:
		notification.notify(title = "COVID-19 Updates India",
							message = message,
							app_icon = "covid.ico",
							timeout = 10)
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
		for i in range(4, 10):
			data.append(x[i].strip()) # Cleaning the data to filter out only the information which is needed

		contents = [data[i]+data[i+1] for i in range(0, 5, 2)]
		notifyMe("\n".join(contents)) # Display the information in the desired format

	except:
		notifyMe("Something went wrong. Could not fetch data")
