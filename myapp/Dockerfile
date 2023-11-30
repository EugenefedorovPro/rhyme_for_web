FROM python:3.10.9-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /home/eugene
COPY requirements.txt .
RUN apt-get update && apt-get install -y git-lfs
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
COPY . .
COPY entrypoint.sh .
ENTRYPOINT ["sh", "entrypoint.sh"]
