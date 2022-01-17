.PHONY: all npm python

.DEFAULT: config

all:
	npm install
	npm update

	python -m venv api/venv
	api/venv/bin/pip install -q -r api/requirements.txt
	cd api && ./venv/bin/python3 __init__.py

python:
	python -m venv api/venv
	api/venv/bin/pip install -q -r api/requirements.txt
	cd api && ./venv/bin/python3 __init__.py
	@clear
	@echo -"Please go in /api and run Makefile for docs"


npm:
	npm install
	npm update