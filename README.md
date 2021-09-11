Olá! Meu nome é Igor Baiocco

Este projeto é um desafio para o processo seletivo para estágio na IndustriALL, cujo devo desenvolver uma aplicação WEB
e uma API RESTful para o cadastro de eventos e registro via JSON, respectivamente. 

Decidi utilizar o Django REST Framework pois já tenho prática com a linguagem Python, mas em um futuro próximo, irei 
aprender outras frameworks, como REACT.

COMO UTILIZAR:
    
    
        Antes de qualquer coisa, instale os itens solicitados no arquivo 'requirements.txt' utilizando o pip e, em 
    seguida, rode os comandos "python manage.py makemigrations" e, em seguida, "python manage.py 
    migrate", isto garantirá que não há nenhuma configuração dos modelos pendentes. 
    Em Seguida, rode "python manage.py runserver".
    
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