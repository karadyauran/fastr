FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN mkdir /authentication
WORKDIR /authentication

COPY ../requirements.txt /authentication/

RUN pip install -r requirements.txt

COPY . /authentication/

COPY ../settings /

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
