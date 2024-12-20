FROM ubuntu:latest AS build

# Atualiza o sistema e instala o openssh-client
RUN apt-get update && apt-get install -y openssh-client

# Atualiza aplicações
# RUN apt-get upgrade

# install python3.12
RUN apt-get -y install python3.12
RUN apt-get -y install python3-pip
RUN apt-get -y install python3-virtualenv
RUN apt-get install -y sqlite3
RUN apt-get install -y git


# Cria o usuário gtd
RUN useradd -m gtd

# Configura o diretório home do usuário gtd
WORKDIR /home/gtd

# Gera a chave SSH
# RUN ssh-keygen -t rsa -b ed25519 -C "recursossauro@gmail.com"

# Copia a chave pública para o host (ajuste o caminho conforme necessário)
# COPY id_rsa.pub /home/gtd/.ssh/authorized_keys

# Define o usuário padrão para o container
USER gtd

RUN mkdir -p ~/.ssh && \
    ssh-keygen -t ed25519 -C "recursossauro@gmail.com" -f ~/.ssh/id_ED25519
    # Gemmini exemple
    # ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -q \
    # development environment
    # ssh-keygen -t ed25519 -C "recursossauro@gmail.com"
    # mix Gemini with development environment
    # ssh-keygen -t ed25519 -C "recursossauro@gmail.com" -f ~/.ssh/id_rsa -q \

# Copiar a aplicação gtd para /home/gtd/app
RUN mkdir /home/gtd/app

WORKDIR /home/gtd/app

# Copy app
COPY auth /home/gtd/app/auth
COPY accounts /home/gtd/app/accounts
COPY core /home/gtd/app/core
COPY gtd /home/gtd/app/gtd
COPY inbox /home/gtd/app/inbox
COPY tasks /home/gtd/app/tasks
COPY projects /home/gtd/app/projects
COPY templates /home/gtd/app/templates
COPY manage.py /home/gtd/app
COPY requirements.txt /home/gtd/app
# Nos próximos, essa linha deve estar comentada e ter makemigrations e migrate para gerar o bd
#COPY db.sqlite3 /home/gtd/app

EXPOSE 8000

RUN virtualenv .env
ENV PATH="/home/gtd/app/.env/bin:$PATH"

ENV PYTHONWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

RUN pip3 install -r requirements.txt

ENV DJANGO_SUPERUSER_USERNAME="recursos"
ENV DJANGO_SUPERUSER_EMAIL="recursossauro@gmail.com"
ENV DJANGO_SUPERUSER_PASSWORD="gnithcud"

 RUN python manage.py migrate
 RUN python manage.py createsuperuser --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL

# Comando para executar a aplicação
 CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

