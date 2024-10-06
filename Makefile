migrate: migrations
	python3 manage.py migrate

migrations:
	python3 manage.py makemigrations

populate: csu

csu:
	python3 manage.py csu

run:
	python3 manage.py runserver