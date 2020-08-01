test:
	python runtests.py

coverage:
	coverage run --source "./wagtail_meta_preview" runtests.py && coverage report && coverage html

format_code:
	black --exclude "/(\.eggs|\.git|\.hg|\.mypy_cache|\.nox|\.tox|\.venv|_build|buck-out|build|dist|migrations)/" ./
