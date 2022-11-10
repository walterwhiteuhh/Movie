import random
import requests
from bs4 import BeautifulSoup

# crawl IMDB Top 250 and randomly select a movie

URL = 'http://www.imdb.com/chart/top'