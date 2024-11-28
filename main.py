import requests
import json
from bs4 import BeautifulSoup
import aiohttp

class Twfemi():

    def __init__(self):
        self.html = self.GetTwfemiTweetHTML(self.GetTwfemiSite())
        self.titles = self.GetTwfemiTweetTitle(self.html)
        self.urls = self.GetTwfemiTweetURLs(self.html)

    def GetTwfemiSite(self):
        site = requests.get("https://togetter.com/t/%E3%83%84%E3%82%A4%E3%83%95%E3%82%A7%E3%83%9F")
        return site.text

    def GetTwfemiTweetHTML(self, site: str):
        soup=BeautifulSoup(site, "html.parser")
        html = soup.find('div', {'class', "left contents_main"})
        urls = html.find_all('span', {'class', "title"})
        return urls

    def GetTwfemiTweetTitle(self, urls):
        twt = []
        for u in urls:
            title = u.find('a')
            twt.append(title.get_text())
        return twt

    def GetTwfemiTweetURLs(self, urls):
        twt = []
        for u in urls:
            title = u.find('a')
            twt.append(title["href"])
        return twt
