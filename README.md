# Teste de Engenharia de Dados da empresa Raízen

<hr/>

## Sites e links utilizados

- Fonte das Tabelas Dinâmicas

https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fwww.gov.br%2Fanp%2Fpt-br%2Fcentrais-de-conteudo%2Fdados-estatisticos%2Fde%2Fvdpb%2Fvendas-combustiveis-m3.xls&wdOrigin=BROWSELINK

- Teste Engenharia de Dados

https://github.com/raizen-analytics/data-engineering-test

<hr/>

## Etapas

### Tratamento utilizando Pandas e PySpark

- coleta de dados das tabelas dinâmicas; 

- dados coletados foram alterados e armazenados em formato csv na pasta "csv_brutos_pre_alterados", na subpasta csv_bruto;

- os colabs utilizados com os arquivos do csv_bruto foram armazenados na subpasta "Google_Colab_csv_bruto";

- cada tipo de derivado de petróleo foi concatenado e se encontra na pasta "csv_concatenacao";

- O csv do penúltimo tratamento está na pasta "Datasets_google_colab"; 

- o arquivo do google colab utilizado para o último tratamento e concatenação está armazenado na pasta "Google Colabs";

- os datasets finais (tratados), estão armazenados na pasta "datasets_final".

<hr/>

### Parquet

- os datasets finais foram convertidos do formato csv para parquet;

- os arquivos convertidos estão na pasta "parquet" na subpasta G_Colab_Parquet e os arquivos convertidos na mesma pasta.  

<hr/>

### Pipelines

- desenvolvimento do código foi realizado no google colab, o arquivo está armazenado na pasta "dataflow", subpasta colab_pipe;

- os resultados das pipelines (csv gerado e prints) criados no Google Cloud Platform estão na subpasta "resultados_pipes";

- dentro do arquivo "Pipelines_Dataflow", há diferentes tipos de pipelines desenvolvidas;

- A intenção foi criar duas pipelines que retornassem a quantidade do produto total, pelo estado e cada tipo de produto. Entretanto, alguns empecilhos, fizeram com que fossem gerados outros tipos de pipelines com diferentes informações (ver o arquivo "Pipelines_Dataflow"), afim de alcançar o objetivo.

  



