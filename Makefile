.PHONY: config

.DEFAULT: config

config:
	npm install
	npm update

	python -m venv api/venv
	api/venv/bin/pip install -q -r api/requirements.txt
	cd api && ( ./venv/bin/python3 __init__.py || ./venv/Lib/python.exe __init__.py)




