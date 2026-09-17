# Laboratório de estatística

## Nome
  Ian Raphael Sampaio Costa

## Matrícula

## Descrição

  Um laboratório de estatística onde todas as funções matemáticas foram implementadas do zero e podem ser testadas em tempo real com um data set real, além de serem automaticamente testadas contra as funções equivalentes de bibliotecas conhecidas.
  Para realização do projeto foi feita a utilização de IA para inspiração, Organização do projeto (roadmap), busca de informações (consulta a documentação) e correção de sintax pela falta de familiaridade com a linguagem python. Porém não foi copiado nenhum trecho de código gerado por IA.

### Data set
  
  O data set escolhido seria relacionado a ações do SMP500 porém por uma falta de dados categóricos, e por falta de tempo, utilizei o auxilio da IA para chegar no "UCI Bike Shareing Dataset" disponível em: https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset

### Instruções de execução

#### Flakes

  Para um ambiente completamente reproduzível foi usado, e é indicado o uso, do Nix Flakes

  Para executar o projeto com Nix Flakes, basta clonar o repositório

  git clone ...

  Entrar no diretório do projeto

  cd projeto

  Executar o comando nix develop

  nix develop

  O ambiente estará completamente configurado bastando agora rodar a aplicação 

#### Sem Flakes

  Sem o Flakes é necessário além de clonar o repositório e acessar o diretório

  git clone ...
  cd projeto

  É necessário criar um "virtual environment" manualmente e usar o pip para instalar todas as dependências

  python3 -m venv .venv
  source .venv/bin/activate
  python -m pip install --upgrade pip
  python -m pip install -r requirements.txt
  
### Funcionamento da aplicação

  adicionar gif

