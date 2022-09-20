# Teste de Engenharia de Dados da empresa Raízen

<hr/>

## Sites e links utilizados

#### Fonte das Tabelas Dinâmicas

https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fwww.gov.br%2Fanp%2Fpt-br%2Fcentrais-de-conteudo%2Fdados-estatisticos%2Fde%2Fvdpb%2Fvendas-combustiveis-m3.xls&wdOrigin=BROWSELINK

#### Teste Engenharia de Dados

https://github.com/raizen-analytics/data-engineering-test

<hr/>

## Etapas

### Tratamento utilizando Pandas e PySpark

- coleta de dados das tabelas dinâmicas; 

- dados coletados foram alterados e armazenados em formato csv na pasta "arquivos_originais_csv";

- cada produto foi concatenado de acordo com seu tipo e os google colabs armazenados na pasta "concatenação" ---> subpasta "colabs_concat_produtos";

- cada produto após concatenado (por estado), foi armazenado na pasta "concatenação" --> subpasta "csv_concatenacao";

- o colab "ANP_Concat.ipynb", foi utilizado na última concatenação e tratamento e o dataset gerado ("dataset_derivados_pandas"), está armazenado na pasta "concatenação";

- na pasta dataset_final está armazenado o dataset tratado;

<hr/>

### Parquet

- o dataset final foi convertido do formato csv para parquet;

- na pasta "parquet", foi armazenado o colab (subpasta "G_Colab_Parquet") e o dataset em formato parquet ("derivados_petrol.parquet");

<hr/>

### Pipelines

- desenvolvimento do código foi realizado no google colab, o arquivo está armazenado na pasta "pipeline";

- foi criado duas pipelines em relação ao estado por produto e volume total do derivado. O mesmo foi feito para o diesel.



