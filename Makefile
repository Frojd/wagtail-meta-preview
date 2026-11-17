test:
	docker-compose exec web python runtests.py

coverage:
	docker-compose exec web coverage run --source "./wagtail_meta_preview" runtests.py && coverage report && coverage html

lint:
	uv run ruff check .

format_code:
	uv run ruff format .
