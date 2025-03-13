#### Introdução

Atividade Realizada pelo Aluno Felipe Biava Favarin para a disciplina de Desenvolvimento Web II do bacharelado em Ciência da Computação no Instituto Federal Catarinense Campus Videira

#### Propósito

Criar um ToDo List usando HTML, Flask em Python, conectando com banco de dados SQLite e criando containers com Docker.
Temos a seguinte estrutura:

![image](https://github.com/user-attachments/assets/0b6d1ba5-b5a4-48d9-be42-6b780cc33c07)


Para acessar o repositório localmente faça:
´´´sh
git clone https://github.com/felipebfava/TodoListDockerAula.git
´´´

Abra-o em um editor de código de preferência (Visual Studio Code, etc.)

Você verá que o Arquivo AulaDevWebII_Felipe contém alguns arquivos docker.
Para iniciar o que foi definido no docker compose e não ter acesso ao terminal quando tiver em execução:
´´´sh
docker compose up --build
´´´
Ou, para executar e ter acesso ao terminal quando quiser:
´´´sh
docker compose up -d --build
´´´

Ao executar esses comandos entre em seu navegador e digite 'localhost' , assim, você verá a aplicação funcionando localmente.

#### Comandos para Containers

Visualizar os containers em execução.
´´´sh
docker ps
´´´

Exibe uso de recursos dos containers
´´´sh
docker stats
´´´

Mostra os status dos containers gerenciados pelo docker compose
´´´sh
docker compose ps
´´´

Quais portas do host estão mapeadas para o container nginx
´´´sh
docker port nginx
´´´

Para testar a comunicação dos containers app1 e nginx via requisição HTTP
´´´sh
docker compose exec nginx curl http://app1:5000
´´´

Para testar a comunicação dos containers app2 e nginx via requisição HTTP, com terminação /oi.
´´´sh
docker compose exec nginx curl http://app2:5001/oi
´´´

#### Parar Containers

Para o container app1.
´´´sh
docker compose stop app1
´´´

Para o container app2.
´´´sh
docker compose stop app2
´´´

Assim conseguimos testar a funcionalidade de backup do App3

#### Limpeza dos Containers

Para e remove todos os containers do docker compose
´´´sh
docker compose down
´´´

Remove todos os containers, imagens, redes e volumes não utilizados, limpando completamente o ambiente.
´´´sh
docker system prune -a
´´´
