FROM python:3.10.9-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /home/eugene
COPY ./requirements.txt ./
RUN apt-get update && apt-get install -y git-lfs
RUN pip3 install -r requirements.txt
#RUN pip3 install jupyter
COPY . .
#EXPOSE 8000
#RUN cd rhyme_for_web/rhyme_for_web
#RUN pwd
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["python", "manage.py", "runserver", "localhost:8000"]
