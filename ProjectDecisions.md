# Decisões de projeto

Obs.: Esse documento, por facilidades de comunicação será escrito em português.

## Bibliotecas
Seria simples utilizarmos somente a biblioteca `httpx` para as requisições assíncronas necessárias ao projeto, mas a API
da APILayer que usamos para consultar os valores das moedas e, a partir deles, efetuarmos a conversão, não possui 
cotação para ETH solicitado no projeto. 

Após investir bastante tempo para sanar essa lacuana encontramos a biblioteca `aioetherscan` e a API da Etherscan que
trabalha especificamente com ETH e, com isso, sanamos o problema de não encontrar cotação para essa criptomoeda.

Usar a biblioteca Dynaconf foi uma opção para podermos gerir, a partir do [Twelve Factors App](https://12factor.net/) e
mantermos as configurações de ambiente no próprio ambiente.

Por fim, o uso do fastAPI como framework web se deu pelo fato do mesmo ter suporte para desenvolvimento assíncrono e
usar o que há de mais recente na linguagem Python com type annotations. Além, claro, de já nos fornecer, uma maneira 
simples e prática de termos uma documentação Swagger da API.

## Desenvolvimento futuro
Temos clara consciência que nessa primeira versão do projeto não foram escritos testes. Algo que deveria ter sido feito,
mas o problema de encontramos uma forma de conseguir a contação do ETH exigiu um investimento de tempo maior do que era
esperado, mas estamos cientes da necessidade de cobrirmos com testes o projeto, algo que podemos e iremos fazer.

Outra questão bem complexa é que os testes em aplicações assíncronas são mais complexas, como utilizmaos a biblioteca
`httpx` para as requisições, foi necessário investirmos um tempo para encontrar uma biblioteca que nos fornecesse mocks
das requisições feitas para as APIs externas, para evitar que os testes consumam o limite de requisições que a conta 
possui. Encontramos a bilbioteca [respex](https://github.com/lundberg/respx) que nos auxilia nisso, mas não houve 
tempo hábil para testá-la e, também, para implementar os testes.

Temos em mente, ainda, implmentar o uso da lib [locust](https://locust.io/) para testes de carga, que nos proporcionará
uma avaliação do comportamento da API em variados cenários de uso da mesam.

No mais, podemos dizer que foi uma experiência gratificante desenvolver esse projeto. Sabendo haver muito que melhorar.