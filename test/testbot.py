#-*-encoding:utf-8-*-
'''
Created on 2015年12月3日

@author: chris
'''
import telebot
import ConfigParser
from telebot import types

cfg = ConfigParser.SafeConfigParser()
with open('../settings.cfg','r') as cfgfile:
    cfg.readfp(cfgfile)
token = cfg.get('token','token')
print token
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['googlefor'])
def search_test(message):
    markup = types.ForceReply(selective=False)
    print message.text
    bot.send_message(message.chat.id,'send me words to search:', reply_markup=markup)
    

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print message


    
if __name__ == '__main__':
    bot.polling()
    