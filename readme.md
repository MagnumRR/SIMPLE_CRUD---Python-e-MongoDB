# CRUD - Python e MongoDB
Projeto simples de CRUD, feito em linguagem Python utilizando como banco de dados (Não relacional), o MongoDB.

## Estrutura
    ├── 📁 pmongodb
    │   ├── crud.py
    │   └── main.py
    ├── 📁 tests
    ├── .gitignore
    ├── readme.md
    └── requirements.txt

## Utilização
    Este projeto utilizou:
    * Python 3.14.0

## Ambiente Virtual
    Criou-se um ambiente virtual ("venv") para instalação das bibliotecas.
    * Criando um ambiente virtual (windows):
        python -m venv venv (ou outro nome a sua escolha)
    * Ativando o ambiente virtual (Windows):
        venv/Scripts/activate   

## bibliotecas
    > requirements.txt
        * dnspython==2.8.0
        * pymongo==4.16.0
        * tabulate==0.9.0

## Particularidades
    1. Assim como os outros bancos de dados, o MongoDB utiliza alguns parâmetros para sua conexão, como foi a necessidade de instalar a biblioteca "pymongo" e utilizar seu módulo: "MongoClient", que recebe apenas 2 parÂmetros: O host e a porta.

    2. A estrutura do banco de dados MongoDB segue a similaridade do arquivo "json" para criação de coleções e documentos, na forma de listas e dicionários.

    3. Na funcionalidade "excluir()" utilizou-se uma lógica para atualizar algum item do documento ou todos eles, de forma que, se o usuário não quisesse atualizar determinado item bastaria "saltar" (dar um Enter).        

## Clonar este projeto
    https://github.com/MagnumRR/SIMPLE_CRUD---Python-e-MongoDB.git

## Execução
    * main.py 

## Autor
    Magnum Ribeiro Rodrigues dos Santos