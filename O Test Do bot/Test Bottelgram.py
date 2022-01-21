# 

import telebot

chave_api =" Sua Chave do bot telegram"

bot = telebot.TeleBot(chave_api)




def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
        Seja Bem vindo, Como posso ta ajudando ?

Escolha uma opção para continuar (Clique na Opção):
         /opcao1 Fazer um pedido
         /opcao2 Rede Social 
         /opcao3 Mandar um abraço pro M.M
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)




bot.polling()