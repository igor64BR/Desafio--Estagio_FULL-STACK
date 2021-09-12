# "Socializei!" - Desafio para Estágio Full-Stack
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/igor64BR/Desafio--Estagio_FULL-STACK/blob/main/LICENSE) 

# Sobre o Projeto:

Este projeto é um desafio para o processo seletivo para estágio na **IndustriALL**, cujo objetivo é desenvolver uma 
**aplicação WEB** e uma **API RESTful** para o cadastro de eventos e registro via JSON, respectivamente. 

Decidi utilizar o **Django REST Framework**, pois trabalha com o método MTV - Model, View, Template - e consegue trabalhar 
de modo escalável, ou seja, é passível de processar o crescimento de sua estrutura e de número de usuários de forma 
estável, além de também poder trabalhar usando cache e múltiplos db de backup. Além disso, por se tratar de uma frame-
work programada em Python, toda sua otimização de código da linguagem é replicada no Django.

## Layout da aplicação WEB:
![WEB](https://github.com/igor64BR/Desafio--Estagio_FULL-STACK/blob/main/assets/Screenshot%20from%202021-09-11%2023-01-30.png) 

## Layout da API RESTful
![API REST](https://github.com/igor64BR/Desafio--Estagio_FULL-STACK/blob/main/assets/Screenshot%20from%202021-09-11%2023-02-38.png)

# Ferramentas Utilizadas:

## Back-end
- Python
    - Django
    - Django Rest Framework

## Front-End
- HTML
- CSS
- JavaScript
- Bootstrap

## Banco de dados:
- SQLite3


# COMO UTILIZAR:
Pré-requisitos: https://github.com/igor64BR/Desafio--Estagio_FULL-STACK/blob/main/requirements.txt

```bash
# Baixe o arquivo do link na raiz do projeto

# Dentro do diretório raiz do projeto
pip install -r requirements.txt

# Faça as migrations
python manage.py makemigrations
python manage.py migrate

# Caso não o arquivo db.sqlite3 não esteja no projeto:
  ## Faça as migrations e crie o db
  python manage.py migrate --run-sncdb

  ## Crie as credenciais do super usuário
  python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver

# Acesse a aplicação WEB:
http://localhost:8000/

# Acesse a API em sua primeira versão (V1)
http://localhost:8000/api/v1/  # As Endpoints estão listadas em 'url.py' no diretório 'socializei'
```

## Obs.:
```bash
Para inserir os dados, modificá-los ou deletá-los dentro da API, o usuário deve estar logado na área de administração ou
inserir o token de usuário no header da API:
Para a permissão via token, deve-se entrar na uri '/admin/', logando com o super usuário criado e, na seção de token, 
criar um novo para o seu usuário 
```

# Autor

Igor Baiocco Rodrigues

Linkedin: https://www.linkedin.com/in/igor-baiocco/
GitHub: https://github.com/igor64BR
