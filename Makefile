serve:
	pipenv run python runserver.py

deploy:
	flyctl deploy

migrate:
	dbmate migrate