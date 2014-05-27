from willie import module


@module.commands('complain')
def complain(bot, trigger):
		complaint = trigger.group(2)
		if complaint == "" or complaint is None:
		        bot.say("Why you complaining about nuffin again?")
		else:
		        bot.say("STFU complaining about "+complaint+"!")





