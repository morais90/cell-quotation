install:
	pip3 install -r requirements.txt

test:
	python3 manage.py test -v2 tests
