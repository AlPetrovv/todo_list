# Разворачивание

1. `git clone https://github.com/AlPetrovv/todo_list.git`   
2. Создать env файлы по шаблонам в директориях `backend/app_envs` и `docker_compose/envs`.
3. `make run` если используем docker compose
Если используем IDE для запуска, необходимо:
   1. нужно установить рабочую директорию backend/core
   2. установить python 3.11
   3. установить poetry
   4. создать виртуальное окружение `poetry env use 3.11`
   5. установить зависимости `poetry install`
   6. установить статические файлы `python manage.py collectstatic`
   7. выполнить миграции `python manage.py migrate`
   8. запустить проект  `python manage.py runserver 0.0.0.0:8000`
4. проверить что всё завелось

## Дополнительно 
Если на пк запущен postgres, нужно его отключить или поменять порт для postgres в docker-compose
Если ипользуем postgres локально(не в docker), нужно сменить Database host на localhost.
