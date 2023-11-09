FROM python:3.10

WORKDIR /skymarket

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

COPY ./skymarket/. .

COPY .env .

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]