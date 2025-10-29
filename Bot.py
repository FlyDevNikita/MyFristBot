import telegram, telegram.ext

with open("user.txt","w") as file:
	pass

async def start(update: telegram.Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE): #страт
	
	await update.message.reply_text("hello world!😎")


async def help(update: telegram.Update,context: telegram.ext): #хелп
	await update.message.reply_text("команды! - searchнайти собеседника     stop - остоновить поиск🚫 ")
username = []

	
async def search(update: telegram.Update,context: telegram.ext): #сеарч
	await update.message.reply_text("ищу тебе собесендника🌐")
	useretot = update.effective_user.username
	if useretot not in username:
		   username.append(str(useretot))
		   
		   with open("user.txt","a") as file:
		   	file.write(useretot + "/n")

	print(username)
	
	if len(username) == 1:
			pass
			#username.append("user")
	

	else:
		print(f"я нашел тебе собеседника!{username}")
		await update.message.reply_text(f"я нашел тебе собеседника!{username}")
		username.clear()

		
async def stop(update: telegram.Update,context: telegram.ext):
	username.clear()
	await update.message.reply_text("поиск был остановлен!")
	print(username)
	

 
app = telegram.ext.ApplicationBuilder().token(" tocken").build()


app.add_handler(telegram.ext.CommandHandler("help",help))

app.add_handler(telegram.ext.CommandHandler("start",start))

app.add_handler(telegram.ext.CommandHandler("search",search))

app.add_handler(telegram.ext.CommandHandler("stop",stop))

app.run_polling()
