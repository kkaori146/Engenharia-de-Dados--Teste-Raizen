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

- dados coletados foram alterados e armazenados em formato csv na pasta "csv_brutos_pre_alterados", na subpasta csv_brsuto;

- os colabs utilizados com os arquivos do csv_bruto foram armazenados na pasta "Google_Colab_csv_bruto";

- cada tipo de derivado de petróleo foi concatenado e se encontra na pasta "csv_concatenacao";

- O csv do penúltimo tratamento está na pasta "Datasets_google_colab"; 

- o arquivo do google colab utilizado para o último tratamento e concatenação está armazenado na pasta "Google Colabs Utilizados";

- os datasets finais (tratados), estão armazenados na pasta "datasets_final"

<hr>

### Pipelines

- desenvolvimento do código foi realizado no google colab, o arquivo está armazenado na pasta "dataflow", subpasta colabs_pipes;

- os resultados das pipelines estão na subpasta "resultados_pipes";

- prints das pipelines foram retirados do dataflow (GCP)



