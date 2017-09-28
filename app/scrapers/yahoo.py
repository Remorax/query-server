from __future__ import print_function
import os, json, sys
from generalized import Scraper

class Yahoo(Scraper):
    """Scrapper class for Yahoo"""
    def __init__(self):
        self.url = 'https://search.yahoo.com/search'
        self.defaultStart = 1
        self.startKey = 'b'

    @classmethod
    def parseResponse(self, soup):
        """ Parse response and returns the urls

            Returns: urls (list)
                    [[Tile1,url1], [Title2, url2],..]
        """
        urls = []
        for h in soup.findAll('h3', attrs={'class': 'title'}):
            t = h.findAll('a', attrs={'class': ' ac-algo fz-l ac-21th lh-24'})
            for y in t:
                r = y.get('href')
                f = r.split('RU=')
                e = f[-1].split('/RK=0')
                u = e[0].replace('%3a', ':').replace('%2f', '/').replace('%28', '(').replace('%29', ')').replace('%3f',
                                                                                                                 '?').replace(
                    '%3d', '=').replace('%26', '&').replace('%29', ')').replace('%26', "'").replace('%21', '!').replace(
                    '%23', '$').replace('%40', '[').replace('%5b', ']')
                urls.append({'title': y.getText(),
                             'link': u})

        return urls