.PHONY: up down run test format setup

up:
	docker-compose up -d 

down:
	docker-compose down

run:
	PYTHONPATH=. python week3/sales_pipeline.py

test:
	PYTHONPATH=. pytest week3/tests/test_sales_pipeline.py -v

format:
	black .
	flake8 --exclude=.git,__pycache__ .

setup:
	PYTHONPATH=. python week2/create_schema.py
	PYTHONPATH=. python week2/load_data.py

