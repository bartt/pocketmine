FROM phusion/baseimage:latest
MAINTAINER Bart Teeuwisse <bart@thecodemill.biz>

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get -y install m4 automake autoconf make gcc libtool curl

RUN mkdir /pocketmine
RUN cd /pocketmine && curl -sL http://cdn.pocketmine.net/installer.sh | bash -s -
ADD server.properties /pocketmine/

VOLUME /pocketmine
WORKDIR /pocketmine

EXPOSE 19132

CMD ["./start.sh"]