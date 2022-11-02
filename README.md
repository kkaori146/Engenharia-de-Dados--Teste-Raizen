# Teste de Engenharia de Dados da empresa Raízen

<hr>

## Sites e links utilizados

- Fonte das Tabelas Dinâmicas

https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fwww.gov.br%2Fanp%2Fpt-br%2Fcentrais-de-conteudo%2Fdados-estatisticos%2Fde%2Fvdpb%2Fvendas-combustiveis-m3.xls&wdOrigin=BROWSELINK

- Teste Engenharia de Dados

https://github.com/raizen-analytics/data-engineering-test

<hr>

## Etapas

### Tratamento utilizando Pandas e PySpark

- coleta de dados das tabelas dinâmicas; 

- dados coletados foram armazenados em formato csv na pasta "arquivos_originais_csv";

- na pasta "concatenação", estão armazenados os dados concatenados para cada tipo de combustível com seu respectivo colab e arquivo csv. Assim como, o google colab do arquivo final;

- na pasta "dataset_final" está armazenado o csv final;

- na pasta G_Colab_Parquet, está armazenado o arquivo parquet para os derivados do petróleo;


<hr>

### Pipelines

- desenvolvimento do código foi realizado no google colab, o arquivo está armazenado na pasta "pipelines", subpasta apache beam;

- na pasta apache airflow, foi realizado o mesmo desafio da pasta apache beam, porém utilizando como ferramenta o airflow.





