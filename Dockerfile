FROM ubuntu:20.04

ENV TZ=America/Los_Angeles

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y python3-pip 


COPY requirements.txt ./

RUN pip3 --no-cache-dir install -r requirements.txt

COPY . .
EXPOSE 8501
CMD streamlit run run.py
