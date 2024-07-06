include .env
export

install:
	@asdf install
	@poetry install

run: up
	@poetry run uvicorn workout_api.main:app --reload

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) poetry run alembic revision --autogenerate -m $(d)

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) poetry run alembic upgrade head

up-docker:
	@docker compose up -d

up: up-docker run-migrations