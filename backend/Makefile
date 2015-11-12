PYTHON ?= python

all:

test:
	$(PYTHON) manage.py test backend platal

clean:
	find -name '*.pyc' -delete
	find -name '__pycache__' -delete

install-deps:
	pip install -r requirements.txt

.PHONY: all test clean install-deps
