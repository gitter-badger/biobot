from willie.module import commands
import datetime

@commands('igem_team')
def igem(bot, trigger):
  bot.say("London Biohackers' igem team page - http://igem.org/Team.cgi?id=1337")
  
  
  diff = (datetime.datetime(int(2014), int(10), int(30))
                - datetime.datetime.today())
  
  bot.say("there are "+str(diff.days) + " days, " + str(diff.seconds / 60 / 60)
                   + " hours and "
                   + str(diff.seconds / 60 - diff.seconds / 60 / 60 * 60)
                   + " minutes until ")
  bot.say("the iGem Jamboree. whoop de doo!")
  
  
  
  
