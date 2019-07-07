all: clean build run

clean: python3 src/clean.py

build: # compile to binary (if you use interpreter, then do not implement it)

run: python3 src/scraper.py