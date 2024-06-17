FROM python:3

WORKDIR /usr/src/app
COPY . /usr/src/app/

RUN apt update -y

RUN pip install -r requirements.txt

EXPOSE 9876

CMD [ "python3" , "app.py"]