### Azure Blob Storage

## O que é o Blob Storage
O Azure Blob Storage é um serviço de armazenamento de objetos em nuvem da Microsoft. Sua função principal é armazenar de forma otimizada grandes quantidades de dados não estruturados, ou seja, dados que não possuem um formato ou modelo pré-definido, como arquivos de textos, imagens ou logs do sistema. Os usuários e clientes do sistema poderão ter acesso a esses objetos armazenados em qualquer lugar do mundo por meio do protocolo HTTP/HTTPS, sem a necessidade de estarem em uma mesma rede LAN para chegar até a porta do serviço.

## Por que foi escolhido
Ele foi escolhido para o projeto da CorpTech dada a sua capacidade de armazenar dados não estruturados, atuando como um repositório intermediário entre a API REST do JSM e o Azure SQL Database. Como o Azure SQL Database exige dados estruturados em tabelas, o Blob Storage resolve o problema de incompatibilidade de armazenamento inicial e particionando os dados diários. Garantindo assim que, em caso de falhas na transformação ou transferência para o banco de dados, esses arquivos originais não sejam perdidos.

## Alternativas 
Uma alternativa seria fazer a inserção desses dados diretamente no Azure SQL Database, sem a intermediação do Blob Storage. Porém, caso ocorra algum erro durante o processamento ou indisponibilidade do banco de dados antes da gravação, esses dados seriam perdidos sem potencial de recuperação. Tendo em vista esse alto risco de perda de dados e forte acoplamento, essa alternativa deve ser descartada.


## Referência:
[Azure Blob Storage](https://learn.microsoft.com/pt-br/azure/storage/blobs/storage-blobs-introduction)
