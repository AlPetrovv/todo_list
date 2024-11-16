DC = docker compose
EXEC = docker exec -it
MANAGE_PY = python manage.py

APP_CONTAINER = todo_list-django
POSTGRES_CONTAINER = todo_list-db

APP_SERVICE = django
POSTGRES_SERVICE = postgres

DOCKER_COMPOSE_FILE = docker_compose/docker-compose.yaml
ENV = --env-file=docker_compose/envs/dc_file.env

.PHONY: run
run: stop
	${DC} -f ${DOCKER_COMPOSE_FILE} ${ENV} up  --build

.PHONY: stop
stop:
	${DC} -f ${DOCKER_COMPOSE_FILE} ${ENV} down

.PHONY: run-app
run-app:
	${DC} -f ${DOCKER_COMPOSE_FILE} ${ENV} up --build ${APP_SERVICE} -d

.PHONY: run-db
run-db: stop-db
	${DC} -f ${DOCKER_COMPOSE_FILE} ${ENV} up  ${POSTGRES_SERVICE} -d

.PHONY: stop-db
stop-db:
	${DC} -f ${DOCKER_COMPOSE_FILE} ${ENV} stop ${POSTGRES_SERVICE}

.PHONY: migrate
migrate:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} migrate

.PHONY: migrations
migrations:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} makemigrations

.PHONY: create-superuser
create-superuser:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} createsuperuser

.PHONY: sh
sh:
	${EXEC} ${APP_CONTAINER} sh

