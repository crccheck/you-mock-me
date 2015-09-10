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


cheat:
	PYTHONPATH=shims \
	python -m unittest discover \
	  --start-directory=solutions --pattern="exercise*.py" --failfast

cheat/%:
	PYTHONPATH=shims \
	python -m unittest solutions/exercise_$*.py || \
	  (echo "Excercise $* does not exist" && exit 1)

.PHONY: exercises
exercises:
	@rm -rf exercises/*
	@${MAKE} -s $(subst solutions,exercises,$(wildcard solutions/*.py))

exercises/%:
	echo $@
	cat solutions/$* | python sanitize.py > $@
