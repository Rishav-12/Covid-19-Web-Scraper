# Covid-19-Web-Scraper
Scrape Covid-19 related data from a website

### Updates
This is now a consumable API

### Requirements
Check the [requirements.txt](https://github.com/Rishav-12/Covid-19-Web-Scraper/blob/master/requirements.txt) file

### Description
* There are 3 python files

* [scraper.py](https://github.com/Rishav-12/Covid-19-Web-Scraper/blob/master/scraper.py) has a helper function that scrapes the website https://www.worldometers.info/coronavirus/ to collect information about a given country's covid data, then returns it as a dictionary

* [notify.py](https://github.com/Rishav-12/Covid-19-Web-Scraper/blob/master/notify.py) uses the scraped data and sends a desktop notification to the user

* [app.py](https://github.com/Rishav-12/Covid-19-Web-Scraper/blob/master/app.py) serves the scraped data in the form of an API

* I set the country to India, but you can change that to any country

### Usage
* You can run scraper.py to write the data to a json file
* Or run the notify.py file if you want to send desktop notification updates with the data
* Or maybe use the API to do API stuff

#### Running the API locally
```bash
pip install -r requirements.txt
```

to install dependencies
```bash
uvicorn app:app --reload
```

to run the API server
