#FROM 
#FROM centos/python-36-centos7

#COPY . /app

#WORKDIR /app

#CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "80", "--reload"]


FROM python:3.8-slim

COPY . /tarefa

WORKDIR /tarefa

RUN pip install fastapi uvicorn

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "80", "--reload"]

