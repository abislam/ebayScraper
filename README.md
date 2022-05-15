# ebayScraper
Basic frontend to show firestore data pulling from ebay.
**This project does not follow proper measures for securely using API keys.**
The goal of this project is to show how a fully automated webscraping function could be implemented using the Google Cloud Platform and Firestore Database.

## Blueprint

- Created a Python web scraping function with the BeautifulSoup library that pulls listing information from Ebay. The item of choice is the "RTX 3080". [main.py](main.py)
- Function was then transferred over to a Google Cloud Function.
- The Google Cloud Function was then scheduled to run every 10 minutes using the Google Cloud Scheduler.
- All the data is sent to a Firestore Database.
- [The data is shown off in a basic frontend html page](index.html) which is hosted on Github Pages.
