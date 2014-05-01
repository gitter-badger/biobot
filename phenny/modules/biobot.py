import os
import glob
import time
import calendar
import datetime


def incubator(phenny, input):
	output=os.popen("tail -1 /home/biobot/app/bin/temp.dat").read().split(", ")
	ts_epoch = int(output[0])
	ts = datetime.datetime.fromtimestamp(ts_epoch).strftime('%H:%M:%S')
	
	
	phenny.say("The temp of the incubator at "+ ts +" is "+output[1].rstrip()+" degrees C")


incubator.commands = ['incubator']
incubator.priority = 'medium'

def complain(phenny, input):

        phenny.say("STFU complaining about "+input.group(2)+"!")


complain.commands = ['complain']
complain.priority = 'medium'

