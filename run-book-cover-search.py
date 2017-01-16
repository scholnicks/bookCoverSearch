#!/usr/bin/python -B
# -*- coding: utf-8 -*-

from bookCoverSearch import bookCoverSearch

print bookCoverSearch('Cujo','Stephen King')
print bookCoverSearch(title='Cujo',author='Stephen King')
print bookCoverSearch('Not Cujo','Not Stephen King')
