FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY settings /app/settings/
COPY payment /app/

CMD ["python", "/app/payment/manage.py", "runserver", "0.0.0.0:8005"]
