test:
	docker compose exec web python runtests.py --shuffle

coverage:
	docker compose exec web sh -c "coverage run runtests.py --shuffle && coverage html --fail-under=0 && coverage report"

lint:
	uv run ruff check .

format_code:
	uv run ruff format .
