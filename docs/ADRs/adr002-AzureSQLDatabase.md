# ADR-002: [Escolha do Banco de Dados]

**Status:** [Aceito]  |  **Data:** [AAAA-MM-DD]  |  **Autores:** Bruno Deud, Reidner Fausto, Pedro Alves.

## Contexto

Necessidade de um melhor armazenamento de dados e melhoria da usabilidade do sistema.
## Decisão

Foi escolhido pela sua capacidade de armazenar tabelas relacionais com chamados, analistas, categorias, SLAs, métricas calculadas e histórico de status. Ele resolve justamente esse problema de armazenamento da CorpTech, por ser relacional, facilita a interação com o dashboard.

## Consequências

Resolve problemas de armazenamento da aplicação

Facilita a interação com o dashboard.

## Alternativas rejeitadas

  Poderiam utilizar um banco de dados não relacional convencional. Foi descartado devido à natureza do projeto, por possuir diferentes tipos de dados, tornou-se necessária a utilização de um banco de dados que exigisse e repassasse a formatação ideal para o dashboard.

## Links

[Azure SQL Database](https://learn.microsoft.com/pt-br/azure/storage/blobs/storage-blobs-introduction)