FROM python:3.8-alpine

RUN apk update && apk add --no-cache bash py3-virtualenv
RUN mkdir /apps
#ADD phonebook.db /apps
ADD PhoneBookModel.py /apps
ADD requirements.txt /apps
ADD Service.py /apps
ADD start.sh /apps
ADD stop.sh /apps
ADD wsgi.py /apps
RUN rm -rf /tmp/* /var/cache/apk/*
WORKDIR /apps
EXPOSE 32000
RUN cd /apps && pip3 install --no-cache-dir -r requirements.txt
ENTRYPOINT ["sh","-C","start.sh"]
