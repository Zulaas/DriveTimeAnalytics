BIN=venv/Scripts/

init:
	$(BIN)pip install -r requirements.txt

run:
	$(BIN)python sample/sample.py

test:
	$(BIN)pytest tests