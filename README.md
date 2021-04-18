bookCoverSearch
===============

bookCoverSearch takes a book title and single author and returns a link to the book's cover photo. which is returned as a CoverPhoto object. Currently
only [GoogleAPI](https://developers.google.com/books/docs/v1/using) is searched.

```python
from bookCoverSearch import bookCoverSearch

print(bookCoverSearch('Cujo','Stephen King'))
# {'url': u'http://books.google.com/books/content?id=YrQACwAAQBAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api', 'error': None}

print(bookCoverSearch(title='Cujo',author='Stephen King'))
# {'url': u'http://books.google.com/books/content?id=YrQACwAAQBAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api', 'error': None}

print(bookCoverSearch('Not Cujo','Not Stephen King'))
# {'url': None, 'error': 'Unable to find any matches'}
```

&copy; Steve Scholnick <scholnicks@gmail.com>
