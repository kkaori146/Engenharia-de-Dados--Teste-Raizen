# Teste de Engenharia de Dados da empresa Raízen

## Sites e links utilizados

- ANP

https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/vendas-de-derivados-de-petroleo-e-biocombustiveis

- Teste Engenharia de Dados

https://github.com/raizen-analytics/data-engineering-test

## Objetivos



## Ferramentas

<div align="center">
<p float="left">
  <img src="https://user-images.githubusercontent.com/83531935/205040367-8781dd2d-9327-401a-b77d-7aaa008e2a44.png" width="120" margin-botton="1000" />
  <img src="https://user-images.githubusercontent.com/83531935/202240028-cd1716fe-dfd5-4484-a9c1-9422da702468.png" width="380" /> 
  <img src="https://user-images.githubusercontent.com/83531935/202240030-59908174-d35d-4a4f-aeb8-9622420886f9.png" width="200" />
  <img src="https://user-images.githubusercontent.com/83531935/202240035-8d3d3582-b222-472d-baa8-1ed9551f2b0e.png" width="180" />
</p>
</div>


## APACHE BEAM

### Etapas

### Tratamento utilizando Pandas e PySpark

- coleta de dados das tabelas dinâmicas; 

- dados coletados foram armazenados em formato csv na pasta "arquivos_originais_csv";

- concatenação dos datasets e tratamento (pasta "concatenação")

- os datasets finais foram armazenados em formato csv e parquet, respectivamente nas pastas: "dataset_final" e "parquet".


### Pipelines

- os dados solicitados pelo desafio foram desenvolvidos primeiramente utilizando a ferramenta apache beam (pasta "pipelines");

<hr/>

## APACHE AIRFLOW

### Etapas

- extração dos dados via url;

- tratamento;

- armazenamento em formato parquet e csv;

- criação dos datasets contendo as informações solicitadas.

### Pipelines

- na pasta "apache beam" estão armazenados todos os materiais de apoio utilizados assim como os arquivos gerados e desenvolvidos para completar o desafio-teste. 

## Resultados

### APACHE BEAM

### Visão Geral dos Resultados

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/205038513-3de52c96-da80-4d65-bf08-3689e4bac620.png" width=1000px > </div>

### APACHE AIRFLOW

### Dependências

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/205038512-6b0fd8a5-d857-4c9e-8975-cb1ceae0127e.png" width=1000px > </div>

### Visão da Tabela Geral

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/205038508-9f583585-18a0-40dd-9a57-61b457abd491.png" width=700px > </div>

### Visão Geral da Tabela com dados de UF, Produto e Volume Total dos Derivados e do Óleo Diesel

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/205038504-1369761d-d023-4f33-8738-9b9449f3490c.png" width=700px > </div>

<br>
<br>
<hr/>

<div align="right"><p>Ano de 2022</p></div>







