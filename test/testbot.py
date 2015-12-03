#-*-encoding:utf-8-*-
'''
Created on 2015年12月3日

@author: chris
'''
import telebot
import ConfigParser

cfg = ConfigParser.SafeConfigParser()
with open('../settings.cfg','r') as cfgfile:
    cfg.readfp(cfgfile)
token = cfg.get('token','token')
print token
bot = telebot.TeleBot(cfg)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
    
if __name__ == '__main__':
    bot.polling()
    