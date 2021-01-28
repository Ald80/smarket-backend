# Gerenciador de Tarefas Backend

## Requerimentos:

* [Python](https://www.python.org/)
* [Django-Rest Framework](https://www.django-rest-framework.org)
* [django-cors-headers](https://pypi.org/project/django-cors-headers)
* [SQLite](https://www.sqlite.org/index.html)

## Instalação de ambiente:

Para instalar as dependências do projeto de maneira local sem comprometer as instaladas no sitema operacional, é necessário criar uma virtual environment, segue o [link](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) com as instruções

Para instalar as bibliotecas utilizadas no projeto execute o comando `pip install -r requirements.txt`

Para ativar as migrações necessárias para gerenciar o esquema de banco de dados execute o comando `python manage.py migrate` na pasta raiz do projeto

Para executar o projeto, execute o comando `python manage.py runserver` na pasta raiz do projeto
