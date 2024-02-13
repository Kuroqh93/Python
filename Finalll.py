from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
def randomJoke():
    jokes=['боїшся стрибати з парашутом? - да - срибай без нього)))','-за кордоном – О, Боже, тут яма є… – В Україні – О, Боже, тут дорога є…','ату у нас сьогодні в школі скорочені батьківські збори.- Що значить скорочені?– Ти, я і директор']
    return random.choice(jokes)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def Anekdot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Joke {randomJoke()}')




app = ApplicationBuilder().token("6887867681:AAGgOfHkMXhzpehlokJPWsE6qj4BZ2MUFLs").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("Joke", Anekdot))

app.run_polling()