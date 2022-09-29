from bs4 import BeautifulSoup
import requests
import http

links = []
titles = []

def refresh():

    url = "https://phys.org/physics-news/"

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    for i in soup.find_all(class_="sorted-article"):
        for j in i.find_all(class_="news-link"):
            links.append(j["href"])

    for i in soup.find_all(class_="sorted-article"):
        for j in i.find_all(class_="news-link"):
            titles.append(j.text)
