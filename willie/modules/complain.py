import willie




def complain(bot, trigger):
        complaint = input.group(2)
        if complaint == "":
                phenny.say("Why you complaining about nuffin again?")
        else:
                phenny.say("STFU complaining about "+complaint+"!")



@module.commands('complain')

