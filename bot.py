from config import * #token
import telebot #api de telegram

#instalacion del bot telegram
bot = telebot.TeleBot(TELEGRAM_TOKEN)


#comando /start
@bot.message_handler(commands=["start", "iniciar"])
def cmd_start(message):
	"""da la bienbenida al usuario"""
	bot.reply_to(message, "hola aaaa")

#responde a texto que no son comandos
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
	"""gestion del mensaje """
bot.send_message(message.chat.id, "hola de nuevo")

#main ######################
if __name__ == '__main__':
	print('iniciando bot')
	bot.infinity_polling()
	print('fin')
	
	
