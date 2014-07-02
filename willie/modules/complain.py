# coding=utf-8

from willie import module
import random

@module.commands('complain')
def complain(bot, trigger):
		complaint = trigger.group(2)
		if complaint == "" or complaint is None:
		        bot.say("Why you complaining about nuffin again?")
		if complaint == "" or complaint is None:
		        bot.say("Why you complaining about nuffin again?")
		else:
		        bot.say(random.choice(complains).decode('latin1') % complaint)


complains = ["STFU complaining about %s",
"I once saw %s steal candy from a baby",
"%s is totally worse than a boil on the end of your nose",
"%s ate all the cookies.",
"Are you still going on about %s",
"%s is banned in several countries",
"Mentioning %s before 9PM is illegal in Sudan",
"%s is the worst thing ever!",
"%s believes in global warming", 
"%s never gets a round of drinks", 
"%s smells like an old tent", 
"%s didn't do the washing up", 
"%s voted for UKIP", 
"%s starts eating without waiting for everyone else", 
"%s thinks Jeremy Beadle is funny.", 
"%s bought a £4.99 present in the £5 secret santa",
"%s lied on their tax return",
"%s art as loathsome as a toad",
"%s doesn't do a good deed everyday",
"%s Need I say more?",
"%s. I do desire we may be better strangers",
"%s. Though are a flesh-monger a fool and a coward",
"%s is the best of the cut-throats ",
"%s, I say to thee, a weasal hath noth such a deal of spleen as you are todd'd with",
"%s is Half A Bubble Off Of Plumb",
"%s went the full retard",
"%s is not batting on a full wicket ",
"%s prefers Emacs to vim."]
