build:
	pip install -r requirements.txt

test:
	python -m unittest discover -v --start-directory=exercises --pattern="exercise*.py"
