import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.filmweb.pl/ranking/film")

soup = BeautifulSoup(req.content, "html.parser")


def fetch_data():
    titles = [title.get_text() for title in soup.find_all(class_="rankingType__title")]
    rating = [rate.get_text() for rate in soup.find_all(class_="rankingType__rate--value")]
    rate_count = [" ".join(count.get_text().split()[0:2]) for count in soup.find_all(class_="rankingType__rate--count")]

    for i in range(0, len(titles)):
        print(" -> ".join((titles[i], rating[i], rate_count[i])))

fetch_data()







