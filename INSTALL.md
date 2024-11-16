# Разворачивание

1. `git clone https://github.com/AlPetrovv/todo_list.git`   
2. Создать env файлы по шаблонам в директориях `backend/app_envs` и `docker_compose/envs`
3. `make run` если используем docker compose, если не используем - нужно создать и выполнить миграции + статик файлы.
4. проверить что всё завелось

## Дополнительно 
Если на пк запущен postgres, нужно его отключить или поменять порт для postgres в docker-compose
