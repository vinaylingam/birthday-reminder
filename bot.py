# Bot UserName : @RemindOnBirthdaysBot

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import time
import KEYS
import os

PORT = int(os.environ.get('PORT', 5000))

updater = Updater(token=KEYS.token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename = "logs.txt")

def start(update, context):
    logging.info("---"*50)
    logging.info(update)
    logging.info(str(update.message.chat_id)+", Name: "+update.message.from_user.first_name+", Command Handled: Start")
    if update.message.chat_id != KEYS.admin :
        context.bot.send_message(chat_id=KEYS.admin,text="Bot is contacted by {0}({1}), id = {2}".format(update.message.from_user.first_name,update.message.from_user.username,update.message.chat_id))
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello {}".format(update.message.from_user.first_name)+" Welcome to Birthday Remainder bot. U will never miss wishing someone on their birthday with my help.\ncheck /help for more commands.")

def add(update, context):
    logging.info("---"*50)
    logging.info(update)
    logging.info(str(update.message.chat_id)+", Name: "+update.message.from_user.first_name+", Command Handled: add")
    if update.message.chat_id != KEYS.admin :
        context.bot.send_message(chat_id=KEYS.admin,text="Bot is contacted by {0}({1}), id = {2}".format(update.message.from_user.first_name,update.message.from_user.username,update.message.chat_id))
    # take parameters and add into database
    context.bot.send_message(chat_id=update.message.chat_id, text="This command is WIP")

def list(update, context):
    logging.info("---"*50)
    logging.info(update)
    logging.info(str(update.message.chat_id)+", Name: "+update.message.from_user.first_name+", Command Handled: list")
    if update.message.chat_id != KEYS.admin :
        context.bot.send_message(chat_id=KEYS.admin,text="Bot is contacted by {0}({1}), id = {2}".format(update.message.from_user.first_name,update.message.from_user.username,update.message.chat_id))
    #pull out all the birthdays added by this user
    context.bot.send_message(chat_id=update.message.chat_id, text="This command is WIP")

def help(update, context):
    print("help..")
    logging.info("---"*50)
    logging.info(update)
    logging.info(str(update.message.chat_id)+", Name: "+update.message.from_user.first_name+", Command Handled: help")
    if update.message.chat_id != KEYS.admin :
        context.bot.send_message(chat_id=KEYS.admin,text="Bot is contacted by {0}({1}), id = {2}".format(update.message.from_user.first_name,update.message.from_user.username,update.message.chat_id))
    msg = "These commands are available as for V1.0.0\n"
    msg += "/add - add a birthday to reminder. command structure /add {name} {dd/mm/yyyy]}\n"
    msg += "/list - show the existing reminders\n"
    msg += "Upcoming commands -\n /search - to search from the list with filters like name, month, year.\n"
    msg += "/remove - to remove a reminder with id\n"
    msg += "WIP(Work In Progress)\n"
    context.bot.send_message(chat_id=update.message.chat_id, text=msg)

def textHandler(update, context):
    logging.info("---"*50)
    logging.info(update)
    logging.info(str(update.message.chat_id)+", free text handled")
    if update.message.chat_id != KEYS.admin :
        context.bot.send_message(chat_id=KEYS.admin,text="Bot is contacted by {0}({1}), id = {2}".format(update.message.from_user.first_name,update.message.from_user.username,update.message.chat_id))
    context.bot.send_message(chat_id=update.message.chat_id, text="see /help available commands")


start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help',help)
addd_handler = CommandHandler('add',add)
list_handler = CommandHandler('list',list)
text_handler = MessageHandler(Filters.text, textHandler)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(addd_handler)
dispatcher.add_handler(list_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(text_handler)

updater.start_polling() # uncomment to use in local via API
# updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN.token) # uncomment to use via WEBHOOK
# updater.bot.setWebhook('https://birthday-remainders.herokuapp.com/' + TOKEN.token) # uncomment to use via WEBHOOK
