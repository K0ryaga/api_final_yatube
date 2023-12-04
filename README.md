# Проект api_final_yatube

Описание: Проект api_final_yatube является RESTful API для управления и обмена данными в приложении. Он предоставляет возможности для создания, чтения, обновления и удаления различных ресурсов, такие как посты, комментарии и группы.

Задача: Проект api_final_yatube решает задачу предоставления гибкого и масштабируемого API для клиентского приложения. Он обеспечивает аутентификацию и авторизацию с использованием JWT-токенов, позволяет пользователям создавать и управлять своими данными, а также обеспечивает взаимодействие между пользователями через комментарии и подписки.

Установка:
1. Клонируйте репозиторий на локальную машину: `https://github.com/K0ryaga/api_final_yatube.git`
2. Перейдите в директорию проекта: `cd api_final_yatube`
3. Создайте и активируйте виртуальное окружение:
   - Создание: `python -m venv venv`
   - Активация (Windows): `venv\Scripts\activate`
   - Активация (macOS/Linux): `source venv/bin/activate`
4. Установите зависимости: `pip install -r requirements.txt`
5. Перейдите в директорию, где находится файл manage.py: `cd yatube_api`
6. Выполните миграции базы данных: `python manage.py migrate`
7. Запустите сервер разработки: `python manage.py runserver`

Примеры запросов к API:

1. Получение JWT-токена:
   - URL: `/api/v1/jwt/create/`
   - Метод: `POST`
   - Параметры запроса: `username`, `password`
   - Пример запроса:
     ```json
     {
       "username": "string",
       "password": "string"
     }
     ```
   - Пример ответа:
     ```json
     {
       "access": "string",
       "refresh": "string"
     }

2. Создание новой публикации:
   - URL: `/api/v1/posts/`
   - Метод: `POST`
   - Параметры запроса: `text`, `image`, `group`
   - Пример запроса:
     ```json
     {
      "text": "string",
      "image": "string",
      "group": 0
     } 
     ```
   - Пример ответа:
     ```json
     {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2019-08-24T14:15:22Z",
      "image": "string",
      "group": 0
     }

3. Обновление публикации:
   - URL: `/api/v1/posts/{post_id}/`
   - Метод: `PUT`
   - Параметры запроса: `post_id`, `text`, `image`, `group`
   - Пример запроса: `/api/v1/posts/1/`
     ```json
     {
      "text": "string",
      "image": "string",
      "group": 0
     } 
     ```
   - Пример ответа:
     ```json
     {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2019-08-24T14:15:22Z",
      "image": "string",
      "group": 0
     }
