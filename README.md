Projeto para Matéria de Estrutura de Dados Universidade Braz Cubas
Professora: Andrea Ono Sakai
Membros: Eduardo Felipe Braga, Gabriel José C. Pereira, Eduardo Gabriel S.C

TICKFLOW
**1 - Conceito Do Projeto.**
O TickFlow é uma aplicação web em Python para gerenciar a venda de ingressos para shows de forma justa e eficiente. Utiliza Lista, Fila e Pilha implementadas manualmente para exibir eventos, controlar a ordem de compra e permitir desfazer ações.

**2 - Sistema.**
O Sistema de Ingressos é uma aplicação web desenvolvida em Python com o objetivo de gerenciar a venda de entradas para shows e eventos de forma organizada, justa e eficiente. O sistema permite que usuários visualizem o catálogo de eventos disponíveis, entrem em uma fila de compra respeitando a ordem de chegada, adquiram ingressos e gerenciem suas ações com a possibilidade de desfazê-las. 

Internamente, o sistema utiliza três estruturas de dados fundamentais: Lista, Fila e Pilha  implementadas manualmente, além de algoritmos de ordenação para organizar os eventos por diferentes critérios.

O sistema de ingressos tem como objetivo gerenciar a venda de entradas para shows e eventos de forma organizada e direta. Ele permite que usuários visualizem os eventos disponíveis, entrem em uma fila de compra, adquiram ingressos e gerenciem suas ações dentro do sistema.

*2.2 - Aplicação das Estruturas*
*Lista*
A lista armazena os objetos do tipo Evento, cada um contendo: nome do evento, artista, data e horário, local, preço do ingresso, número total de ingressos disponíveis. É a estrutura central do catálogo de eventos do sistema. 

*Fila*
São enfileirados objetos do tipo Usuário aguardando compra, contendo: ID do usuário, nome, o evento de interesse e o momento de entrada na fila (timestamp). Cada posição na fila representa um usuário aguardando sua vez para realizar a compra do ingresso.


*Pilha*
São empilhados objetos do tipo Ação, cada um representando uma operação realizada pelo usuário: seleção de evento, escolha de quantidade de ingressos, aplicação de filtro ou confirmação de compra. Cada ação registra o tipo da operação e o estado anterior do sistema antes dela.


**3. Executando o Sistema.**

