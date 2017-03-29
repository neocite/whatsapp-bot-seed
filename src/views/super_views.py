# -*- coding: UTF-8 -*-
from utils.media_sender import UrlPrintSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random


class SuperViews():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [
            ("ola".lower(), self.help),
            ("olá".lower(), self.help),
            ("oi".lower(), self.help),
            ("^/about", self.about),
            ("^/roll", self.roll),
            ("/(?P<evenOrOdd>even|odd)$", self.even_or_odd),
        ]

    def about(self, message=None, match=None, to=None):
        self.url_print_sender.send_by_url(message.getFrom(), "https://github.com/joaoricardo000/whatsapp-bot-seed", ABOUT_TEXT)

    def roll(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("[%d]" % random.randint(1, 6), to=message.getFrom())

    def even_or_odd(self, message=None, match=None, to=None):
        is_odd = len(match.group("evenOrOdd")) % 2
        num = random.randint(1, 10)
        if (is_odd and num % 2) or (not is_odd and not num % 2):
            return TextMessageProtocolEntity("[%d]\nYou win." % num, to=message.getFrom())
        else:
            return TextMessageProtocolEntity("[%d]\nYou lose!" % num, to=message.getFrom())

    def help(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(HELP_TEXT, to=message.getFrom())


# HELP_TEXT = """ [HELP]
# - Commands
# /help - Show this message.
# /about - About
# /s(earch) - I'm lucky!
# /i(mage) - I'm lucky with image!
# /t(ts) - Text to speech.
# /(even)(odd) - Amazing game.
# /ping - Pong.
# /echo - Echo.
# /roll - Roll a dice.
#
# Automatic:
#     - Url (http://...) print screen.
#     - Image (jpeg, gif, png) download.
#     - Videos (mp4, webm) downloads.
#     - Youtube videos.
# """

HELP_TEXT = """
Bem vindo ao PoupeCompre, tudo bem?

No Poupe Compre você programa o valor da parcela que cabe no seu bolso.
Você pode parcelar em até 12 vezes no boleto e quando realizar a quitação total do plano,
recebe o produto.

E mais, para comprar não realizamos consulta ao Serasa/SPC e aprovação de crédito,
ou seja, não é necessário ter conta em banco,
cartão de crédito ou comprovação de renda.

Para isso preciso descobrir se você já começou algum cadastro com a gente...

Por favor, informe o seu CPF digitando apenas os NÚMEROS

"""

ABOUT_TEXT = """ [Whatsapp Bot Seed]
A small open source python framework to create a whatsapp bot, with regex-callback message routing.
https://github.com/joaoricardo000/whatsapp-bot-seed
"""
