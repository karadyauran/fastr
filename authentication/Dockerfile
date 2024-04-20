FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY settings /app/settings/
COPY authentication /app/

CMD ["python", "/app/authentication/manage.py", "runserver", "0.0.0.0:8000"]
