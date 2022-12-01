from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
import pandas as pd
import datetime as dt
import requests
import os

os.system('pip install fastparquet')

#Função para extrair dados:
def extrair_dados_derivados():
    url = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/vdpb/vendas-derivados-petroleo-e-etanol/vendas-derivados-petroleo-etanol-m3-1990-2022.csv"
    x = requests.get(url) 
    open('dados_brutos/vendas-derivados-petroleo-etanol-m3-1990-2022.csv', 'wb').write(x.content) 
  
# Função de leitura e tratamento:
def tratamento():
    dfpetrol = pd.read_csv('dados_brutos/vendas-derivados-petroleo-etanol-m3-1990-2022.csv', sep=";")
  
  # Adição da coluna unit

    dfpetrol['unit'] = 'm3'

  # Criação da coluna "created_at"

    dfpetrol['created_at'] = dt.datetime.now()

  # Troca do formato string por numérico na coluna meses

    dfpetrol['MÊS'].replace([
        'JAN',
        'FEV',
        'MAR',
        'ABR',
        'MAI',
        'JUN',
        'JUL',
        'AGO',
        'SET',
        'OUT',
        'NOV',
        'DEZ'],
        ['01',
        '02',
        '03',
        '04',
        '05',
        '06',
        '07',
        '08',
        '09',
        '10',
        '11',
        '12'], inplace=True)

    # Renomeando as colunas

    dfpetrol.rename(columns={"UNIDADE DA FEDERAÇÃO": "uf", "PRODUTO": "product", "VENDAS": "volume" }, inplace=True)
    
    # Replace dos nomes dos estados

    dfpetrol['uf'].replace([
        'ACRE',
        'ALAGOAS',
        'AMAPÁ',
        'AMAZONAS',
        'BAHIA',
        'CEARÁ',
        'DISTRITO FEDERAL',
        'ESPÍRITO SANTO',
        'GOIÁS',
        'MARANHÃO',
        'MATO GROSSO',
        'MATO GROSSO DO SUL',
        'MINAS GERAIS',
        'PARANÁ',
        'PARAÍBA',
        'PARÁ',
        'PERNAMBUCO',
        'PIAUÍ',
        'RIO DE JANEIRO',
        'RIO GRANDE DO NORTE',
        'RIO GRANDE DO SUL',
        'RONDÔNIA',
        'RORAIMA',
        'SANTA CATARINA',
        'SERGIPE',
        'SÃO PAULO',
        'TOCANTINS'],
        ['AC',
        'AL',
        'AP',
        'AM',
        'BA',
        'CE',
        'DF',
        'ES',
        'GO',
        'MA',
        'MT',
        'MS',
        'MG',
        'PR',
        'PB',
        'PA',
        'PE',
        'PI',
        'RJ',
        'RN',
        'RS',
        'RO',
        'RR',
        'SC',
        'SE',
        'SP',
        'TO'], inplace=True)

    # Concatenando os dados das colunas ANO e Mês

    dfpetrol['year_month'] = dfpetrol['ANO'].map(str) + '-' + dfpetrol['MÊS'].map(str)
    
    # Organização das colunas

    dfpetrol = dfpetrol[[
        'year_month',
        'uf',
        'product',
        'unit',
        'volume',
        'created_at'
    ]]

    # Definindo atributo na coluna year_month

    dfpetrol['year_month'] = pd.to_datetime(dfpetrol['year_month'])

    # Replace de vírgula por ponto

    dfpetrol['volume'] = dfpetrol['volume'].str.replace(",",".")
    
    # Definindo os tipos de colunas

    dfpetrol['volume'] = dfpetrol['volume'].astype(float)

    return dfpetrol

# Função de exportação em formato csv e parquet

def exportacao_dados(**kwargs):
    ti=kwargs['ti']
    dfpetrol = ti.xcom_pull(task_ids='tratamento')
    
  # Conversão do dataset em arquivos csv e parquet
  
    dfpetrol.to_csv('dados_tratados/derivados_petrol.csv',index=False)
    dfpetrol.to_parquet('dados_tratados/derivados_petrol.parquet', index=False)

# Produção geral de acordo com o produto (derivados)

def total_producao_derivados():
    dfparquet = pd.read_parquet('dados_tratados/derivados_petrol.parquet', engine='fastparquet')
  
  # Volume total dos derivados de petroleo vendidos para todos os estados 

    dfparquet = dfparquet.groupby(['uf','product']) ['volume'].sum().reset_index() 
  
  # Armazenamento em formato parquet dentro da subpasta derivados
    dfparquet.to_csv('dados_tratados/derivados/prod_regional_derivados.csv',index=False)
    dfparquet.to_parquet('dados_tratados/derivados/prod_regional_derivados.parquet',index=False)
   

# Produção geral de acordo com o produto (diesel)

def total_producao_diesel():
    dfderivados = pd.read_parquet('dados_tratados/derivados/prod_regional_derivados.parquet', engine='fastparquet')

    # Volume total de ÓLEO DIESEL vendido para os estados 

    dfdiesel = dfderivados[dfderivados['product'] == 'ÓLEO DIESEL']

  # Armazenamento em formato parquet dentro da subpasta diesel
    dfdiesel.to_parquet('dados_tratados/diesel/prod_regional_diesel.parquet',index=False)
    dfdiesel.to_csv('dados_tratados/diesel/prod_regional_diesel.csv',index=False)




# Definindo alguns argumentos básicos
default_args = {
    'owner':'kkaori146',
    'start_date': datetime(2022,11,29),
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':1,
    'retry_delay': timedelta(minutes=1)
}

# Instanciando a DAG:
with DAG(
    'raizen',
    max_active_runs=2,
    schedule_interval="@daily",
    catchup = True,
    default_args = default_args) as dag:
    

  extrair_dados_derivados = PythonOperator(
      task_id = 'extrair_dados_derivados',
      python_callable = extrair_dados_derivados
  )

  tratamento = PythonOperator(
    task_id = "tratamento",
    python_callable= tratamento
  )

  exportacao_dados = PythonOperator(
    task_id = 'exportacao_dados',
    provide_context = True,
    python_callable=exportacao_dados
  )

  total_producao_derivados = PythonOperator(
    task_id = 'total_producao_derivados',
    python_callable=total_producao_derivados
  )

  total_producao_diesel = PythonOperator(
    task_id = 'total_producao_diesel',
    python_callable=total_producao_diesel
  )



  
  
extrair_dados_derivados >> tratamento >> exportacao_dados >> total_producao_derivados >> total_producao_diesel 