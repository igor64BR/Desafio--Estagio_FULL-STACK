Olá! Meu nome é Igor Baiocco

Este projeto é um desafio para o processo seletivo para estágio na IndustriALL, cujo devo desenvolver uma aplicação WEB
e uma API RESTful para o cadastro de eventos e registro via JSON, respectivamente. 

Decidi utilizar o Django REST Framework pois já tenho prática com a linguagem Python, mas em um futuro próximo, irei 
aprender outras frameworks, como REACT.

COMO UTILIZAR:
    
    
        Antes de qualquer coisa, rode os comandos "python manage.py makemigrations" e, em seguida, "python manage.py 
    migrate", isto garantirá que não há nenhuma configuração dos modelos pendentes. 
    Em Seguida, rode "python manage.py runserver".

    Como criar um super usuário:
        Abra o terminal de comando e, com o Python instalado na sua máquina, rode o comando "python manage.py 
    createsuperuser" e insira suas credenciais (o email é opcional). Este será seu usuário para acessar a área 
    administrativa e é o usuário com todas as permissões possíveis.
    Feito isso, acesse https://localhost:8000/admin e entre com as credenciais que criou para seu super usuário.
    
    Criando um Token:
        Nesta aplicação, para maior praticidade com ferramentas como Postman ou Insomnia, é possível criar um token de 
    acesso para seu usuário; desta forma, basta inserir a chave no header da ferramenta e já estará autenticado
    
    Acessando as URLs:
        No arquivo urls.py em "eventos", estão todas as uris genéricas, tais como as de acesso para a área 
    administrativa, raíz da aplicação WEB ou à raíz da API REST;
        Já no arquivo de mesmo nome em "socializei", estão os endpoints configurados pelas routers e uris.

EVENTOS:

    Neste diretório, estão localizadas todas as funções globais das aplicações, tais como configurações e rotas 
    genéricas

SOCIALIZEI:

    Já aqui, encontram-se todos as características para o funcionamento da API e aplicação web, como os templates, 
    campos dos formulários, endpoints e uris.