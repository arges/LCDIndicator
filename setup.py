#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(name='LCDIndicator',
      version='0.0.1',
      author='Chris J Arges',
      author_email='christopherarges@gmail.com',
      description='A program to display email count to an LCD',
      long_description='Displays number of unread emails to an LCD',

      packages = find_packages(),
      include_package_data = True,
      package_data = {
        '': ['*.txt', '*.rst'],
        'LCDIndicator': ['data/*.html', 'data/*.css'],
      },
      exclude_package_data = { '': ['README.md'] },
      scripts = ['bin/display-count'],
      
      keywords='python hardware',
      license='GPLv2',
      classifiers=['Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'License :: OSI Approved :: GNU Affero General Public License v2',
                   'Topic :: Hardware',
                  ],
                  
      install_requires = ['setuptools','pylint','configparser',\
                          'datetime','time', 'keyring'],
)
