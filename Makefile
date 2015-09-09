build:
	pip install -r requirements.txt

test:
	python -m unittest discover \
	  --start-directory=exercises --pattern="exercise*.py" --failfast
