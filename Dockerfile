FROM ubuntu:latest

# Atualiza o sistema e instala o openssh-client
RUN apt-get update && apt-get install -y openssh-client

# Atualiza aplicações
RUN apt-get upgrade

# Cria o usuário gtd
RUN useradd -m gtd

# Configura o diretório home do usuário gtd
WORKDIR /home/gtd

# Gera a chave SSH
RUN ssh-keygen -t rsa -b ed25519 -C "recursossauro@gmail.com"

# Copia a chave pública para o host (ajuste o caminho conforme necessário)
COPY id_rsa.pub /home/gtd/.ssh/authorized_keys

# Define o usuário padrão para o container
USER gtd