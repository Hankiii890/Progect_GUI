FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=mysite.settings

COPY . .

CMD ["python", "mysite/manage.py", "runserver", "0.0.0.0:8000"]
