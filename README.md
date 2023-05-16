## Conway's Game of Life

Este é um código em Python que implementa o jogo da vida de Conway, uma simulação de autômatos celulares desenvolvida pelo matemático John Conway. O jogo da vida consiste em um tabuleiro bidimensional composto por células que podem estar vivas ou mortas. O estado das células evolui de acordo com regras simples, criando padrões complexos e interessantes ao longo do tempo.

Este projeto foi desenvolvido com o objetivo de aprender Python e, por isso, apresenta programação básica. Ele serve como uma introdução ao jogo da vida e à manipulação de matrizes em Python.



## Regras do Jogo da Vida

As regras do jogo da vida são as seguintes:

1. Qualquer célula viva com menos de dois vizinhos vivos morre, por falta de população.
2. Qualquer célula viva com mais de três vizinhos vivos morre, por superpopulação.
3. Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva, por reprodução.
4. Qualquer célula viva com dois ou três vizinhos vivos continua viva na próxima geração.

## Funcionalidades

O código implementa as seguintes funcionalidades:

1. Inicialização do tabuleiro com células vivas e mortas.
2. Evolução do tabuleiro a cada geração, de acordo com as regras do jogo da vida.
3. Visualização do tabuleiro em cada geração, mostrando o estado atual das células.
4. Opção para definir a velocidade de reprodução.

## TODO

Necessitam-se serem implementados:

1. Inicialização do tabuleiro com células vivas e mortas atraves de inputs dos usuários.
2. Adicionar as funcionalidades de: Pause, Avançar Geração, Auto e Stop.
3. Melhorar a interface do usuario.
4. Otimizações em geral.

## Como usar

1. Certifique-se de ter o Python instalado no seu sistema.
2. Faça o download ou clone este repositório em seu computador.
3. Navegue até o diretório onde o código está localizado.
4. Abra um terminal ou prompt de comando nesse diretório.
5. Execute o seguinte comando para iniciar o jogo da vida:

```
python main.py
```

## Licença
Este projeto é licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
[MIT License](./LICENSE)

