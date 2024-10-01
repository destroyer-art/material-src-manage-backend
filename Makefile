## Rule ##

run:
	uvicorn app.main:app --host 0.0.0.0 --port 4000 --reload

format:
	black .
	ruff check . --fix