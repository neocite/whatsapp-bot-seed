from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity


def echo(message, match):
    return TextMessageProtocolEntity("Echo: %s" % match.group("echo_message"), to=message.getFrom())


def ping(message, match):
    return TextMessageProtocolEntity("Pong!", to=message.getFrom())


def balance(message, match):
    return TextMessageProtocolEntity("Seu saldo e de 1200 reais. Continue pagando os seus boletos em dia!", to=message.getFrom())


def findCustomer(message, match):
    return TextMessageProtocolEntity("Bem vindo Fernando! Voce quer conquistar um Ar Condicionado Pinguino Silent na loja da Polishop, certo? responda /sim para confirmar", to=message.getFrom())


def optin(message, match):
    return TextMessageProtocolEntity("Vou te explicar os detalhes para voce conquistar o teu sonho...Vamos pedir para o vendedor te entregar 12 boletos no valor de 387,50 e se você conseguir paga-los em dia (eu sei que vai), la pela 6 parcela a Polishop te entrega o produto na sua casa. Responda /aceito para confirmar", to=message.getFrom())


def confirmed(message, match):
    return TextMessageProtocolEntity("Agora e pegar os boletos com o vendedor para conquistar o seu sonho. Pague os boletos em qualquer agencia bancaria ou loterica da sua cidade", to=message.getFrom())
