Тестовое задание DevOps

Что это
Веб-приложение, которое говорит "Hello from Effective Mobile!" через Nginx.

Как запустить
bash

# 1. Установите Docker и Docker Compose

# 2. Клонируйте проект

# 3. Выполните:

docker-compose up -d

Как проверить
bash
curl http://localhost:80/
Должно показать: Hello from Effective Mobile!

Из чего состоит
text
1. Backend (Python) - слушает порт 8080 внутри Docker
2. Nginx - слушает порт 80, пересылает запросы в backend
3. Docker Compose - запускает оба контейнера
Файлы
backend/app.py - Python сервер

backend/Dockerfile - образ для Python

nginx/nginx.conf - настройки Nginx

docker-compose.yml - запуск всего вместе

Особенности
Backend не виден снаружи (только внутри Docker)

Nginx единственный доступен на порту 80

Всё в Docker-контейнерах

Остановить
bash
docker-compose down
Всё просто: запустил, проверил, работает.
