from willie import module

import os
import glob
import time
import calendar
import datetime


@module.commands('incubator')
def incubator(bot, trigger):
	output=os.popen("tail -1 /home/biobot/app/bin/temp.dat").read().split(", ")
	ts_epoch = int(output[0])
	ts = datetime.datetime.fromtimestamp(ts_epoch).strftime('%H:%M:%S')
	
	
	bot.say("The temp of the incubator at "+ ts +" is "+output[1].rstrip()+" degrees C")




