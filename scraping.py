import numpy as np
import wikipedia
import unicodedata

import urllib2
import BeautifulSoup
import re


def getnextlinks(url):
    link = []
    req = urllib2.Request(url)
    req.add_header('User-agent', 'Mozilla/5.0 (Linux i686)')
    #soup = BeautifulSoup()
    response = urllib2.urlopen(req)
    # ,from_encoding=resp.info().get_param('charset'))
    soup = BeautifulSoup.BeautifulSoup(response)
    #text = soup.get_text()
    for url in soup.findAll('a', href=True):

        texttwo = unicodedata.normalize(
            'NFKD', url['href']).encode('ascii', 'ignore')

        link.append(texttwo[1:])
    return link[4:12]


#kr = getnextlinks('https://en.wikipedia.org/wiki/Generative_model')
