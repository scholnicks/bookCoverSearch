from setuptools import setup

setup(
    name='bookCoverSearch',
    version='1.1.0',
    author='Steven Scholnick',
    author_email='scholnicks@gmail.com',
    description="Searches Google's book database and returns a URL for the book cover image",
    long_description="Searches Google's book database and returns a URL for the book cover image",
    license='MIT',
    keywords=['bookCoverSearch','book','cover','photo'],
    url='https://github.com/scholnicks/bookCoverSearch',
    download_url='https://github.com/scholnicks/bookCoverSearch',
    py_modules=['bookCoverSearch'],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License'
    ]
)
