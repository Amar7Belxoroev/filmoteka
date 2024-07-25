<h1>Filmoteka</h1>
<h3>Сервис поиска информации о фильмах и актёрах</h3>
<hr>
<h3>Запуск и развертывание проекта</h3>
<p>Для запуска проекта, на компьютере должен быть установлен <a href="https://www.docker.com/">Docker</a> и <a href="https://docs.docker.com/compose/">docker-compose</a>.</p>
Добавьте в корневую директорию проекта файлы с переменными окружения: 
  <ul>
    <li>.env.dev | <b>Переменные окружения для локальной разработки</b></li>
    <li>.env.prod  | <b>Переменные окружения для production-сборок</b></li>
    <li>.env.prod.db  | <b>Переменные окружения баз данных для production-сборок</b></li>
  </ul>
<hr>
В файл <b>.env.dev</b> добавьте/измените следующие строки:
<pre>
FLASK_APP=app/__init__.py
FLASK_DEBUG=1
DATABASE_URL=postgresql://admin:admin@db:5432/filmoteka_db

SQL_HOST=postgres
SQL_PORT=5432
DATABASE=postgres

REDIS_PASSWORD=redis_admin
REDIS_USER=redis_admin
REDIS_USER_PASSWORD=redis_admin
</pre>

В файл <b>.env.prod</b> добавьте/измените следующие строки:
<pre>
FLASK_APP=app/__init__.py
FLASK_DEBUG=0

DATABASE_URL=postgresql://admin:admin@db:5432/filmoteka_prod_db
SQL_HOST=postgres
SQL_PORT=5432
DATABASE=postgres
</pre>

В файл <b>.env.prod.db</b> добавьте/измените следующие строки:
<pre>
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=filmoteka_prod_db

REDIS_PASSWORD=redis_admin
REDIS_USER=redis_admin
REDIS_USER_PASSWORD=redis_admin
</pre>
<hr>
<p>Для сборки и запуска Docker-контейнеров <b>development</b>-версии проекта, выполните следующие команды:</p>
<pre>
docker-compose down -v
docker-compose up -d --build
</pre>
<p>Для сборки и запуска Docker-контейнеров <b>production</b>-версии проекта, выполните следующие команды:</p>
<pre>
docker-compose down -v
docker-compose -f docker-compose.prod.yml up -d --build
</pre>
<hr>
<h3>Открытие веб-приложения в браузере</h3>
Чтобы открыть запущенное веб-приложение откройте в браузере следующий URL:
<pre>http://127.0.0.1:3005/</pre> 
