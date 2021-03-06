# -*- coding: UTF-8 -*-
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity


def echo(message, match):
    return TextMessageProtocolEntity("Echo: %s" % match.group("echo_message"), to=message.getFrom())


def ping(message, match):
    return TextMessageProtocolEntity("Pong!", to=message.getFrom())


def balance(message, match):
    return TextMessageProtocolEntity("Seu saldo e de R$ 1200 reais. Continue pagando os seus boletos em dia!", to=message.getFrom())


def findCustomer(message, match):
    return TextMessageProtocolEntity("Bem vindo Fernando! Você quer conquistar um Ar Condicionado Pinguino Silent na loja da Polishop, certo? responda sim para confirmar", to=message.getFrom())


def optin(message, match):
    return TextMessageProtocolEntity("Vou te explicar os detalhes para você conquistar o teu sonho...Vamos pedir para o vendedor te entregar 12 boletos no valor de R$ 387,50 e se você conseguir paga-lós em dia (eu sei que vai), lá pela 6º parcela a Polishop te entrega o produto na sua casa. Responda aceito para confirmar.", to=message.getFrom())


def confirmed(message, match):
    return TextMessageProtocolEntity("Agora é só pegar os boletos com o vendedor para começar a conquistar o seu sonho. Pague os boletos em qualquer agência bancária ou lotérica da sua cidade", to=message.getFrom())
