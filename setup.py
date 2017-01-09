import sys
from setuptools import setup

from docopt import __version__

setup(
    name='bookCoverSearch',
    version=__version__,
    requires='requests',
    author='Steven Scholnick',
    author_email='scholnicks@gmail.com',
    description="Searches Google's book database and returns a URL for the book cover image",
    license='MIT',
    keywords='bookCoverSearch',
    url='http://scholnick.net/bookCoverSearch',
    py_modules=['bookCoverSearch'],
    long_description="Searches Google's book database and returns a URL for the book cover image",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License'
    ]
)
