migrate: migrations
	python3 manage.py migrate

migrations:
	python3 manage.py makemigrations

dumpdata:
	python3 manage.py dumpdata users.payment > payment.json
	python3 manage.py dumpdata materials > materials.json

loaddata:
	python3 manage.py loaddata materials.json
	python3 manage.py loaddata payment.json


populate: csu

csu:
	python3 manage.py csu

run:
	python3 manage.py runserver