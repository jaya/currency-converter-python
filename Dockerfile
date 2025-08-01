FROM python:3.13.5-bookworm
LABEL authors="nutaro@protonmail.com"

RUN apt update -y
RUN apt upgrade -y
RUN apt install libpq-dev -y

WORKDIR /opt/app

ADD src/ .
ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt


EXPOSE 80
ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
