# Проект yamdb_final на удалённом сервере
Основан на групповом проекте YaMDb доступный по ссылке [https://github.com/JediMode/api_yamdb].
Реализовал workflows, позволяющие существенно сократить и упростить разработку приложения, выявление ошибок и их устранение. Worflows настроены на соответствие кода PEP8, заранее прописанным тестам, создание и пуш образа на Docker Hub, деплой проекта в главную ветку и оповещение о статусе в телеграм-бот.
Проект разработан с использованием удалённого сервера на ОС Linux, в качестве репозитория для образа выбрал свой Docker Hub.

# Стек технологий
- Python 3.7
- Django 2.2.16
- Linux 5.4.0
- Ubuntu 20.04.4
- Gunicorn 20.0.4
- Nginx 1.18.0
- Docker Engine 20.10.17
- Docker-compose 3.3
- PosgreSQL 14.4

# Как запустить проект
Для начала на сервере остановите службу nginx, введите команду:
```
 sudo systemctl stop nginx
```
Установите docker:
```
sudo apt install docker.io
```
Теперь установите docker-compose, c этим вам поможет официальная документация по ссылке:
https://docs.docker.com/compose/install/

Скачайте проект и перейдите в yamdb_final/infra/, затем скопируйте себе на сервер docker-compose.yaml и директорию nginx. На сервере запустите docker-compose командой:
```
    docker-compose up -d --build
```
Теперь в контейнере web нужно выполнить миграции, создать суперпользователя и собрать статику. Выполните по очереди команды:
```
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
    docker-compose exec web python manage.py collectstatic --no-input
``` 
---
- Страница проекта доступна по адресу: http://158.160.7.15/
- Админка проекта: http://158.160.7.15/admin/login/?next=/admin/
- Документация redoc: http://158.160.7.15/redoc/
