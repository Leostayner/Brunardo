---
title: Camada Física -  APS 8 - Modulação Digital
author: Leonardo Medeiros e Bruna Kimura - leonardopm3@al.insper.edu.br e brunamk@al.insper.edu.br
date: Outubro - 2017
---


# Projeto 3 - Modulação Digital- Camada Fisica
Esse propjeto consiste em implementar uma conexão entre dois computadores utilizando o protocolo uart.

## Protocolo Uart
O protocolo uart é representado pelo seguinte modelo:

![Img 1](doc/image1.png)

O processo inicia com o envio constante do sinal high(1) que indica o estado inicial do sistema e serve como forma de conecção entre os dois computadores. O inicio da recepção de dados ocorre ao receber um start bit, ou seja um bit 0 (Low). Logo em seguida, começa o envio dos dados(payload) a partir do bits menos significativo, em seguida se envia o bit de paridade, que é utilizado para detectar erros na transmissâo, para finalizar o envio desse packote o stopbit é transmitido, um bit de valor 1 que retorna para o estado inicial de conecção.

## Resultado WaveForms
Conforme definido no codigo, deve-se conectar o pino 7* do analog discovery no pino TX1 do arduino e também algum dos pinos de terra do analog no terra do arduino (gnd), a fim de analisar os dados enviados graficamente so wav forms. Foi obtido o seguinte grafico.

![Img 1](doc/image2.PNG)

Em que pode-se verificar a estrutura em uart dos dados recebidos:
Sinal inicial (1)
start bit (0)
payload(10100110)         =  fafpakfpkafpakspf
paridade (1)
stop bit (0)


## Descrição Do Codigo

### Tx
#### Calculo de paridade

Para calcular a paridade foi somado cada bit do dado recebido, verificando se a soma era impar ou par, e retornando o valor de paridade 
1 caso par, e 0 caso impar. 
	
#### Envia Start Bit

Escreve no pino tx o valor 1;
	
#### Envia Payload

#### Envia Paridade

#### Envia Stop Bit


# Rx

#### Calculo de Paridade

#### Confirma Start BIT

#### Recebe Dados

#### Recebe Paridade

#### Recebe Stop Bit  








