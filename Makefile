test:
	pytest -v

ship:
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing

dev:
	gulp --cwd biography/staticapp/

database:
	dropdb biography --if-exists
	createdb biography
