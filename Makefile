setup:
	python3 -m venv env \
	pip install -r requirements.txt

activate:
	source env/bin/activate

db-shell:
	# docker-compose exec db /bin/bash -c "mysql --user=books-user --password=books-pwd books"
	docker-compose exec db /bin/bash -c "psql books books-user"
