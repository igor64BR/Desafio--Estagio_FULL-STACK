Olá! Meu nome é Igor Baiocco

Este projeto é um desafio para o processo seletivo para estágio na IndustriALL, cujo devo desenvolver uma aplicação WEB
e uma API RESTful para o cadastro de eventos e registro via JSON, respectivamente. 

Decidi utilizar o Django REST Framework, pois trabalha com o método MTV - Model, View, Template - e consegue trabalhar 
de modo escalável, ou seja, é passível de processar o crescimento de sua estrutura e de número de usuários de forma 
estável, além de também poder trabalhar usando cache e múltiplos db de backup. Além disso, por se tratar de uma frame-
work programada em Python, toda sua otimização de código da linguagem é replicada no Django.

COMO UTILIZAR:
    
    
        Antes de qualquer coisa, instale os itens solicitados no arquivo 'requirements.txt' utilizando o pip - caso o 
    comando 'pip -r install requirements.txt' não funcione, instale manualmente inserindo as linhas em sequencia no 
    terminal com o comando 'pip install (nome1) (nome2) ...' - e, em seguida, rode os comandos "python manage.py 
    makemigrations" e, em seguida, "python manage.py migrate". Isso garantirá que não há nenhuma configuração dos 
    modelos pendentes. Em Seguida, rode "python manage.py runserver". E pronto! O projeto já está rodando e basta 
    acessá-lo em http://localhost:8000/.

        OBS.: Caso não haja um arquivo db.sqlite3, rode o comando 'python manage.py migrate --run-syncdb. Dessa forma, 
    o Data Base irá ser criado e configurado adequadamente.
    
    Acessando as URLs:
        No arquivo urls.py em "eventos", estão todas as uris genéricas, tais como as de acesso para a área 
    administrativa, raíz da aplicação WEB ou à raíz da API REST;
        Já no arquivo de mesmo nome no diretório "socializei", estão os endpoints configurados pelas routers e uris.
    Com eles, é possível acessar todo o conteúdo da API e gerenciar os dados por ela.

EVENTOS:

    Neste diretório, estão localizadas todas as funções globais das aplicações, tais como as configurações dos projeto, 
    app e ferramenta e rotas genéricas. Também é neste diretório, em settings.py que estão presentes os dados de acesso 
    à tela do administrador - http:localhost:8000/admin/ - e o token de autenticação já criado para a efetivação das 
    ações na API.

SOCIALIZEI:

        Já aqui, encontram-se todos as características para o funcionamento da API e aplicação WEB, como os templates, 
    campos dos formulários, endpoints e URIs. Na pasta 'API' estão localizadas todas as configurações para o 
    funcionamento da API, tais como as Views, os serializadores - tradutores python para JSON ou XML, por exemplo, e 
    vice-e-versa - que permite a manipulação de dados através dos ENDPOINTS da API.

        A pasta migrations é responsável pelo histórico de mudanças nos models, que, por sua vez, modelam o DB para 
    receber e enviar os dados.


Para mais dúvidas de funcionamento do projeto, envie um email para igor64br@gmail.com.
Linkedin: https://www.linkedin.com/in/igor-baiocco/
GitHub: https://github.com/igor64BR

Mais uma vez, muito obrigado pela sua atenção.

Igor Baiocco Rodrigues
