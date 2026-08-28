# ADR-01: [Escolha do Serviço de Nuvem]

**Status:** [Aceito]  |  **Data:** [AAAA-MM-DD]  |  **Autores:** Bruno Deud, Bruno Deud, Pedro Alves.

## Contexto

Necessidade de armazenar dados não estruturados.

## Decisão

Ele foi escolhido para o projeto da CorpTech dada a sua capacidade de armazenar dados não estruturados, atuando como um repositório intermediário entre a API REST do JSM e o Azure SQL Database. Como o Azure SQL Database exige dados estruturados em tabelas, o Blob Storage resolve o problema de incompatibilidade de armazenamento inicial e particionando os dados diários. Garantindo assim que, em caso de falhas na transformação ou transferência para o banco de dados, esses arquivos originais não sejam perdidos.

## Consequências

Recuperação de arquivos em caso de falhas de tranferencia ou transformação.


## Alternativas rejeitadas

Uma alternativa seria fazer a inserção desses dados diretamente no Azure SQL Database, sem a intermediação do Blob Storage. Porém, caso ocorra algum erro durante o processamento ou indisponibilidade do banco de dados antes da gravação, esses dados seriam perdidos sem potencial de recuperação. Tendo em vista esse alto risco de perda de dados e forte acoplamento, essa alternativa deve ser descartada.


## Links

[Azure Blob Storage](https://learn.microsoft.com/pt-br/azure/storage/blobs/storage-blobs-introduction)
