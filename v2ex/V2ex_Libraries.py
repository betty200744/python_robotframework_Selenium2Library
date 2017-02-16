#TODO need add get summury from Hacker News
#TODO https://news.ycombinator.com/rss

from bs4 import BeautifulSoup
import requests
import re


hackernew_url = 'https://news.ycombinator.com/rss'

class HackerNews():
    def __init__(self,data):
        self.data = data

    def get_title(self):
        return self.data.get('title')

    def get_link(self):
        return self.data.get('link')


def get_rss(url):
    r = requests.get(url)
    return r.content


def parse_rss(url):
    # title = re.compile('<title>(.*)</title>')
    # link = re.compile('<a href="(.*)">')
    data = {}
    soup = BeautifulSoup(get_rss(url), 'lxml')
    title = soup.find_all('title')
    link = soup.find_all('link')
    data.update(title=title[0], link=link[0])
    return data


def get_topics_title():
    return HackerNews(parse_rss(hackernew_url)).get_title()

def get_topics_link():
    return HackerNews(parse_rss(hackernew_url)).get_link()


if __name__ == "__main__":
    print HackerNews(parse_rss(hackernew_url)).get_title()
