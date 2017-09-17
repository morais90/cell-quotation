FROM ubuntu:latest
MAINTAINER Willian de Morais <williandmorais@gmail.com>

RUN apt-get update \
&& apt-get install -y \
    python3-pip \
    libtiff5-dev \
    libjpeg8-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    tcl8.6-dev \
&& pip3 install --upgrade pip

ADD . /code
WORKDIR /code

RUN make install