import willie

import commands

@willie.module.commands('fortune')
def fortune(bot, trigger):
   fortune = commands.getoutput('fortune')
   for line in fortune.rsplit("\n"):
      bot.say(line)



