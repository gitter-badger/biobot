import willie




def complain(bot, trigger):

        bot.say("STFU complaining about "+trigger.group(2)+"!")


@module.commands('complain')

