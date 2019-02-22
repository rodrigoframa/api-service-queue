FROM python:3.6-alpine

LABEL maintainer 'Rodrigo Frazão Maia <rodrigo at rodrigoframa@gmail.com'

ENV PYTHONUNBUFFERED 1
RUN pip install redis==2.10.5

ENTRYPOINT ["/usr/local/bin/python"]