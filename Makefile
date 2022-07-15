.PHONY: migrate
migrate:
	@echo "Migrating database..."
	python manage.py migrate --noinput

.PHONY: run
run: migrate collectstatic clean
	@echo "Running server..."
	python3 manage.py runserver 0.0.0.0:8005

.PHONY: run_worker
run_worker:
	python manage.py run_huey -k process -w 3

.PHONY: collectstatic
collectstatic:
	@echo "Copying collectstatic files..."
	python manage.py collectstatic --noinput

.PHONY: clean
clean:
	@echo -n "Clear temp files..."
	@rm -rf `find . -name __pycache__`
	@rm -rf `find . -type f -name '*.py[co]' `
	@rm -rf `find . -type f -name '*~' `
	@rm -rf `find . -type f -name '.*~' `
	@rm -rf `find . -type f -name '@*' `
	@rm -rf `find . -type f -name '#*#' `
	@rm -rf `find . -type f -name '*.orig' `
	@rm -rf `find . -type f -name '*.rej' `
	@rm -rf .coverage
	@rm -rf coverage.html
	@rm -rf coverage.xml
	@rm -rf htmlcov
	@rm -rf build
	@rm -rf cover
	@rm -rf .install-deps
	@rm -rf *.egg-info
	@rm -rf .pytest_cache
	@rm -rf dist

.PHONY: help
help:
	@echo -n "Common make targets"
	@echo ":"
	@cat Makefile | sed -n '/^\.PHONY: / h; /\(^\t@*echo\|^\t:\)/ {H; x; /PHONY/ s/.PHONY: \(.*\)\n.*"\(.*\)"/  make \1\t\2/p; d; x}'| sort -k2,2 |expand -t 20