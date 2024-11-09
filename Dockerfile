FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

CMD ["pytest", "--browser", "ch", "--url", "http://localhost:8080", "--remote", "--bv", "127.0"]