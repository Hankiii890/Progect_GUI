## Реализовать GUI интерфейс CRUD операций для моделей:
ContentType
User
Group
Permission

### Последовательность запуска проекта:

1. В рабочей директории Project_desctop билдим наше приложение. (dokcer-compose build)


2. Затем подымаем наше приложение (docker-compose up)


3. В новом терминале подключаемся к оболочке нашего контейнера с помощью команды (docker exec -it project_desktop-web-1 /bin/bash)


4. После 3 пункта, переходим в директорию mysite нашего контейнера (cd mysite)


5. По классике запускаем наше Django приложенеи (python manage.py runserver)


6. Переходим на указанный порт и приступаем к работе.
