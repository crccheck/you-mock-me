build:
	pip install -r requirements.txt

test:
	PYTHONPATH=shims \
	python -m unittest discover \
	  --start-directory=exercises --pattern="exercise*.py" --failfast

test/%:
	PYTHONPATH=shims \
	python -m unittest exercises/exercise_$*.py || \
	  (echo "Excercise $* does not exist" && exit 1)
