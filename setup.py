# -*- coding: utf-8 -*-
"""
	python-common
	~~~~~

	:copyright: (c) 2014 by Muneeb Ali <http://muneebali.com>  
	:license: MIT, see LICENSE for more details.
"""

from setuptools import setup

setup(
	name='python-common',
	version='0.1.0',
	url='https://github.com/muneeb-ali/python-common',
	license='MIT',
	author='Muneeb Ali (@muneeb)',
	author_email='muneeb@dritte.org',
	description="Common functions that are often needed but don't really belong anywhere",
	packages=['common'],
	zip_safe=False,
	keywords = ['python', 'common', 'log', 'json'],
	classifiers=[
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
	],
)