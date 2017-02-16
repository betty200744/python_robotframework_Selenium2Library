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

    def get_comments(self):
        return self.data.get('comments')


def get_rss(url):
    r = requests.get(url)
    return r.content


def parse_rss(url):
    # title = re.compile('<title>(.*)</title>')
    # link = re.compile('<a href="(.*)">')
    data = {}
    soup = BeautifulSoup(get_rss(url), 'lxml')
    print soup
    title = soup.select('title')[0].contents[0]
    comments = soup.select('comments')[0].contents[0]
    data.update(title=title, comments=comments)
    return data


def get_topics_title():
    return HackerNews(parse_rss(hackernew_url)).get_title()

def get_topics_comments():
    return HackerNews(parse_rss(hackernew_url)).get_comments()


if __name__ == "__main__":
    a = HackerNews(parse_rss(hackernew_url))
    print a.get_comments()
    print a.get_title()



