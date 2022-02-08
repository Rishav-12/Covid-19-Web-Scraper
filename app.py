from fastapi import FastAPI

from scraper import scrape

app = FastAPI()


@app.get("/")
def home():
	data = scrape()

	if data is not None:
		return data
	return {"Data": "Network Error"}
