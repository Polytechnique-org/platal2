PYTHON ?= python

all:

migrate:
	$(PYTHON) manage.py migrate
	$(PYTHON) manage.py migrate --database=platal1

test:
	$(PYTHON) manage.py test backend platal

clean:
	find -name '*.pyc' -delete
	find -name '__pycache__' -delete

install-deps:
	pip install -r requirements.txt

populatedb: migrate
	$(PYTHON) manage.py populatedb

.PHONY: all test clean install-deps migrate populatedb
