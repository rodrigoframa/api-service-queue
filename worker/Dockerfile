FROM python:3.6

LABEL maintainer 'Rodrigo Frazão Maia <rodrigo at rodrigoframa@gmail.com'

ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install freetds-dev -y

# Cria diretório onde vão ficar os arquivos do projeto
RUN mkdir /worker
# Define o diretório de trabalho
WORKDIR /worker
RUN pip install redis==2.10.5
# "Copia" arquivo requirements.txt para o diretorio
ADD ./requirements.txt /worker/
# Executa o pip
RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/local/bin/python"]