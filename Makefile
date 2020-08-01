test:
	python runtests.py
	coverage --source "./wagtail_meta_preview" runtests.py

format_code:
	black --exclude "/(\.eggs|\.git|\.hg|\.mypy_cache|\.nox|\.tox|\.venv|_build|buck-out|build|dist|migrations)/" ./
