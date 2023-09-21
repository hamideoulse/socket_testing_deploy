FROM python:3

WORKDIR /app

COPY ./server.py .

EXPOSE 1024

CMD ["python3", "server.py"]