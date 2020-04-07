all: run

test:
	python3 -m doctest outbreak.py

run: test
	python3 outbreak.py

clean:
	rm -rf __pycache__
