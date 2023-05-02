from fastapi import FastAPI, Path

from scraper import scrape

app = FastAPI()


@app.get("/{country_name}")
def home(country_name: str | None = None):
	"""
	country_name: The name of the country you want to search
	"""
	data = scrape(country_name)

	if data is not None:
		return data
	return {"Data": "Network Error"}
