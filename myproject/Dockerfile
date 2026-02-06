# Используем легкий образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Запрещаем Python писать .pyc файлы и буферизировать вывод (чтобы видеть логи сразу)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости системы (если нужны для определенных пакетов)
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код проекта внутрь контейнера
COPY . .

# Собираем статику (если нужно, раскомментируй)
# RUN python manage.py collectstatic --noinput

# Команда запуска через Gunicorn
# 'attendance_system' — это название папки, где лежит settings.py (вижу его в manage.py на скриншоте)
CMD ["gunicorn", "attendance_system.wsgi:application", "--bind", "0.0.0.0:8000"]