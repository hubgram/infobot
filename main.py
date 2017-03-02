import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import telebot
from telebot import types
import json
import os
import config
import requests as req

bot = telebot.TeleBot(config.token)
@bot.message_handler(commands=['start'])
def start(m):
    cid = m.chat.id
    markup = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton("Naji Team \xf0\x9f\x91\xa5", url="https://telegram.me/Naji_team")
    markup.add(a)
    b = types.InlineKeyboardButton("Developer \xf0\x9f\x98\xbc", url="https://telegram.me/I_Naji")
    markup.add(b)
    nn = types.InlineKeyboardButton("Inline Mode \xe2\x86\xa9", switch_inline_query='')
    markup.add(nn)
    ret_msg = bot.send_message(cid, "`Hello I'm INFO bot \nYou can get Your ID and other information of a message by me.`\n_ To get Your ID >>  _/id\n_ More usages >>  _/help", disable_notification=True, parse_mode="Markdown", reply_markup=markup)
    assert ret_msg.message_id

@bot.message_handler(commands=['help'])
def welcome(m):
    cid = m.chat.id
    markup = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton("Naji Team \xf0\x9f\x91\xa5", url="https://telegram.me/Naji_team")
    markup.add(a)
    b = types.InlineKeyboardButton("Developer \xf0\x9f\x98\xbc", url="https://telegram.me/I_Naji")
    markup.add(b)
    nn = types.InlineKeyboardButton("Inline Mode \xe2\x86\xa9", switch_inline_query='')
    markup.add(nn)
    ret_msg = bot.send_message(cid, "*Get your id by this command : */id\n*Alos you can use of these commands: *\n /me* or */info\n* Send Your feedback : *\n/feedback` [msg]`\n* Inline mod : *\n`type `@Info\_ProBot\n`then select Info`\n\n_ To Contact >>  _/contact\n_ About Me and  MyDeveloper >>  _/about\n\n* Bot version 0.89*", disable_notification=True, parse_mode="Markdown", reply_markup=markup)
    assert ret_msg.message_id

@bot.message_handler(commands=['info', 'me'])
def id(m):      
    cid = m.chat.id
    usr = m.chat.username
    f = m.chat.first_name
    l = m.chat.last_name
    d = m.date
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("\xF0\x9F\x98\x8A Naji Team \xF0\x9F\x98\x8A", url="https://telegram.me/Naji_team"))
    bot.send_chat_action(cid, "typing")
    bot.reply_to(m, "<b>Your ID</b> : {}\n <b>Your Username</b> : @{} \n <b>Your First Name</b> : {}\n <b>Your Last Name</b> : {}\n <b>Msg data</b> : {}".format(cid,usr,f,l,d), parse_mode="HTML", reply_markup=markup)

@bot.message_handler(commands=['contact'])
def c(m):
    uid = m.chat.id
    bot.send_chat_action(uid, 'typing')
    bot.send_contact(uid, phone_number="+98 938 287 2429", first_name="Naji")


@bot.message_handler(commands=['about'])
def p(m):
    uid = m.chat.id
    markup = types.InlineKeyboardMarkup()
    v = types.InlineKeyboardButton('\xF0\x9F\x91\xA5 Thank you to Your choise. \xF0\x9F\x91\xA5', url='https://telegram.me/Info_ProBot')
    a = types.InlineKeyboardButton('Naji', url='https://telegram.me/i_naji')
    ch = types.InlineKeyboardButton('Channel', url='https://telegram.me/Naji_Team')
    git = types.InlineKeyboardButton('Github', url='https://github.com/I-Naji')
    markup.add(v)
    markup.add(a)
    markup.add(ch, git)
    bot.send_chat_action(uid, 'typing')
    bot.send_photo(uid, open('Naji.jpg'), caption="we are #2", reply_markup=markup)

@bot.message_handler(commands=['id', 'myid','ids'])
def test_handler(m):
    f = m.from_user.first_name
    l = m.from_user.last_name
    cid = m.from_user.id
    bot.send_message(cid, "<code>Your Name :</code>\n{} {} \n\n <code>Your ID :\n</code> {}".format(f,l,cid), parse_mode="HTML")
bot.polling(True)
