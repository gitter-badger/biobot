import os
import glob
import time
import calendar
import datetime

os.system('/sbin/modprobe w1-gpio')
os.system('/sbin/modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return str(get_timestamp()) + ", " + str(temp_c)

def get_timestamp():
	future = datetime.datetime.now()
	return calendar.timegm(future.utctimetuple())


with open("/home/biobot/app/bin/temp.dat", "a") as myfile:
	for i in range(1, 6):
		myfile.write(str(read_temp())+'\n')
		time.sleep(10)



