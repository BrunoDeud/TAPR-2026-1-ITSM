# ADR-X003: [Título da decisão]

**Status:** Aceito  |  **Data:** [AAAA-MM-DD]  |  **Autores:** Bruno Deud, Pedro Alves, Reidner Fausto.

## Contexto

Necessidade da Criação de um aplicativo robusto com pouco orçamento, e de manter a aplicação sempre atualizada e rodando.

## Decisão

O Azure Functions foi escolhido porque consegue resolver problemas de processamento eficiente e escalável. No caso da CorpTechele o azure Functions resolve o problema de lidar com grandes volumes de dados e tarefas repetitivas,garantindo que tudo seja processado rapidamente e apenas quando for necessário.

## Consequências

Melhor controle sobre grande volume de dados.
Cumpre com o orçamento baixo.


## Alternativas rejeitadas

Uma alternativa ao Azure Functions seria o AWS Lambda, da Amazon Web Services, mas ele foi descartado porque oprojeto já utiliza o ecossistema da Microsoft, o que acaba facilita a integração e também reduz a complexidade.

## Links

[Azure Functions](https://learn.microsoft.com/pt-br/azure/azure-functions/functions-overview)
