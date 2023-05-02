# Covid-19-Web-Scraper
An API that serves Covid-19 related data

### Requirements
Check the [requirements.txt](https://github.com/Rishav-12/Covid-19-Web-Scraper/blob/master/requirements.txt) file

### Description
Country-specific data scraped from https://www.worldometers.info/coronavirus/

### Usage
* Run scraper.py to write the data to a json file
* Use the API to serve the data at a URL

#### Running the API locally
```bash
pip install -r requirements.txt
```

to install dependencies
```bash
uvicorn src.main:app --reload
```

to run the API server
