test:
	docker-compose exec web python runtests.py

coverage:
	docker-compose exec web coverage run --source "./wagtail_meta_preview" runtests.py && coverage report && coverage html

format_code:
	docker-compose exec web black --exclude "/(\.eggs|\.git|\.hg|\.mypy_cache|\.nox|\.tox|\.venv|_build|buck-out|build|dist|migrations)/" ./
