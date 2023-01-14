import telebot
import openai

def reply(first_chat):
	openai.api_key=<API TOKEN OPENAI>
	engines = openai.Engine.list()
	input_data=openai.Completion.create(
  	model="text-davinci-003",
  	prompt=first_chat,
  	max_tokens=500,
  	temperature=0
	)
	return input_data['choices'][0]['text']



bot=telebot.TeleBot(<API TOKEN TELEGRAM BOT>)
print('program started')

@bot.message_handler(func=lambda message: True)




def reply_msg(message):
    print(message.chat)
    username=message.chat.first_name
    user_id=message.chat.id
    first_chat=message.text

    if first_chat=='Hi' or first_chat=='Hey' or first_chat=='Hello' or first_chat=='/start':
    	bot.send_message(user_id,'Hello!')

    else:
    	bot.send_message(user_id,reply(first_chat))


bot.infinity_polling()
