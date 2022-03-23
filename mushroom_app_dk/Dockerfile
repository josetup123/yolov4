FROM ubuntu:latest
WORKDIR /app
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3.8 \
    python3-pip

COPY requirements.txt requirements.txt
COPY yolov4 yolov4

RUN apt update && apt install 
RUN apt-get install -y wget

RUN dpkg --configure -a
RUN apt install libopencv-dev -y
RUN apt install libopencv-dev -y
RUN apt install -y git
RUN apt install unzip -y
RUN apt install vim -y


RUN pip3 install -r requirements.txt


RUN pip install opencv-python
RUN pip install opencv-contrib-python



EXPOSE 8501/tcp

