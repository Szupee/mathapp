FROM python:3.8-slim-buster

RUN apt-get update
RUN apt-get -y install git
RUN git clone https://github.com/Szupee/mathapp.git
RUN pip3 install flask

CMD ["python3" , "mathapp/backend-2.py"]