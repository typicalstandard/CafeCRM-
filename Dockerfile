# Установка рабочей директории внутри контейнера
WORKDIR /CafeCRM

# Клонирование репозитория с GitHub в рабочую директорию
RUN git clone https://github.com/typicalstandard/CafeCRM-.git .

WORKDIR /CafeCRM/cafe_management
# Установка зависимостей из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Применение миграций
RUN python manage.py makemigrations orders
RUN python manage.py makemigrations menu
RUN python manage.py migrate

# Заполнение базы данных данными из скрипта
RUN python populate_db.py

# Запуск сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
