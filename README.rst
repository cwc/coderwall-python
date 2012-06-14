=========
coderwall
=========

A Python module for accessing user data at http://coderwall.com

Installation
------------

This module is available in the `Python Package Index <http://pypi.python.org/pypi/coderwall>`_ and can be installed easily with ``pip`` or ``easy_install``:: 

	pip install coderwall

Usage
-----

All functionality is accessed through the ``CoderWall`` class::

	>>> from coderwall import CoderWall
	>>> cwc = CoderWall('cwc')
	>>> cwc.name
	u'Cameron Currie'
	>>> cwc.location
	u'Austin, TX'
	>>> cwc.endorsements
	0
	>>> cwc.badges
	[Charity: Fork and commit to someone's open source project in need, 
	Python: Would you expect anything less? Have at least one original repo 
	where Python is the dominant language, T-Rex: Have at least one original 
	repo where C is the dominant language]
