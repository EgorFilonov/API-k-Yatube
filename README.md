### Финальный проект спринта: API для Yatube

### Описание

### API для Yatube

Функционал

Реализован API для публикации постов
Аутентификация по JWT-Токену 
Поддерживает методы GET, POST, PUT, PATCH, DELETE;
Предоставляет данные в формате JSON.

Установка и как запустить проект

1. Клонировать репозиторий 

```git clone https://github.com/Egor-FilonovLol/api-final-yatube.git```

2. Перейти в репозиторий 

```cd api-final-yatube```

3. Создать и активировать виртуальное окружение

```python -m venv venv```

```source Venv/Scripts/Activate```

4. Установить зависимости 

```pip install -r requirements.txt```

5. Перейти в репозиторий и выполнить миграции

```cd yatube_api ```

```python manage.py makemigrations ```

```python manage.py migrate```

6. Запустить проект
```python manage.py runserver```

### Примеры запросов

Аутентификация

1. Выполнить POST-запрос  к эндпоинту ```/api/v1/jwt/create/```  передать в него поле username и password

```
{
    "username": "egor",
    "password": "123"
}
```

2. Получить от API JWT-токен:
```
{
    "refresh": "xxxx",
    "access": "xxxx"
}
```
3. В поле access вернулся JWT-Токен. Если нужно выполнять запросы, то в таком случае, нужно передать его в Authorization: Bearer <токен>

4. Если нужно обновить токен, то мы должны использовать данные с поля refresh



### Результат POST-запроса ```/api/v1/posts/``` с auth-токеном для добавления групп пользователем: 

1. Пример запроса:
```
{
    "text": "Пост зарегистрированного пользователя."
}
```
2 Пример ответа:
```
{
    "id": 1,
    "author": "user",
    "text": "Пост зарегистрированного пользователя.",
    "pub_date": "2025-11-08T23:32:16.630214Z",
    "image": null,
    "group": null
}
```
