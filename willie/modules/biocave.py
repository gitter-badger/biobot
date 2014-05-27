from willie import module


@module.commands('fucking')
def fucking(bot, trigger):
		complaint = trigger.group(2)
		if complaint == "" or complaint is None:
			bot.say("Why you complaining about nuffin again?")
		else:
			bot.say("jeebuz that "+complaint+" really makes me mad!")





