# Uso da imagem oficial do Airflow 
FROM apache/airflow:2.4.2

# Definindo o diretório do projeto
WORKDIR /app

# Cópia do conteúdo do diretório dentro no container no /app
ADD ./app /app/

# Cópia dos requerimentos para dentro do container no /etc
COPY ./requirements.txt /etc

# Instalando os pacotes necessários dentro do arquivo requeriments.txt
RUN pip install -r /etc/requeriments.txt
RUN pip install fastparquet

# Expondo a porta 8080
EXPOSE 8080

# Executar app.py when o container iniciar
CMD ["airflow", "app.py"]