
FROM python:3.8-slim

COPY . /codigo

WORKDIR /codigo

RUN pip install fastapi uvicorn
RUN pip install pandas
RUN pip install sklearn

CMD ["uvicorn", "main:app","--host", "127.0.0.1", "--port", "8080", "--reload"]

