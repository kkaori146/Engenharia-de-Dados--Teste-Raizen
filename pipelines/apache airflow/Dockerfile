# Base de Imagem

FROM apache/airflow:2.3.4-python3.8

# Criação do user root para gerenciamento de pacotes e uso de apt-get
USER root

# Instalação das dependências e ferramentas
# Update e sua instalação
RUN apt-get update
RUN apt-get install -y

# Instalação do libreoffice
RUN apt-get install libreoffice -y

# Criação do user airflow 
USER airflow

# Upgrade do pip
RUN pip install --upgrade pip

# Instalação do fastparquet
RUN pip install fastparquet