"""
bookCoverSearch takes a book title and single author and returns a link to the book's cover photo. which is returned as a CoverPhoto object. Currently
only GoogleAPI is searched.

(c) Steve Scholnick <scholnicks@gmail.com>
MIT License see https://scholnick.net/license.txt
"""

import requests
import re
from urllib.parse import quote

__all__           = ['bookCoverSearch','CoverPhoto']
GOOGLE_SEARCH_URL = 'https://www.googleapis.com/books/v1/volumes?q="{0}"+inauthor:{1}&printType=books'


class CoverPhoto(object):
    '''Holds the link to the cover photo or an error'''
    def __init__(self,url=None,error=None):
        self.url   = url
        self.error = error

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.__dict__)

NO_MATCHES = CoverPhoto(error="Unable to find any matches")


def canonicalForm(s):
    '''Cleans a string by removing all non-word characters'''
    return "" if not s else re.sub(r'\s*','',s).lower().strip()


def bookCoverSearch(title=None,author=None):
    '''Searches for a book's cover based on a title and a single author'''
    url = GOOGLE_SEARCH_URL.format(quote(title),quote(author))
    data = requests.get(url).json()

    if 'items' not in data:
        return NO_MATCHES

    for item in data["items"]:
        volumeInfo = item['volumeInfo']
        if canonicalForm(title) == canonicalForm(volumeInfo['title']):
            for a in volumeInfo['authors']:
                if canonicalForm(author) == canonicalForm(a):          # found our match
                    if 'imageLinks' not in volumeInfo:
                        return CoverPhoto(error="No image links found")

                    if 'thumbnail' in volumeInfo['imageLinks']:
                        return CoverPhoto(url=re.sub(r'&edge=curl','',volumeInfo['imageLinks']['thumbnail']))
                    else:
                        return CoverPhoto(error="No thumbnail link found")

    return NO_MATCHES
