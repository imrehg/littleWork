from __future__ import division
import serial

from datetime import datetime
from time import sleep

serialPort = '/dev/ttyACM0'
baud = 115200
daymin, daymax = 0, 148
daystart, dayfinish = 8.5, 18.0

# Set up serial interface to litteWork
device = serial.Serial(serialPort, baud, timeout=1)

doBuzzer = True
buzzerByte = 255

def displayByte(deciTime):
    """ Turn decimal time into a byte value scaled by
    the day parameters (byt range, times)
    """
    if deciTime < daystart:
        return int(daymin)
    else:
        inrange = (deciTime - daystart) / (dayfinish - daystart)
        value = round( ( daymax * inrange ) + daymin )
        if value > 254:
            value = 254
        return int(value)

def sendTime(deciDate):
    global doBuzzer
    value = displayByte(deciDate)
    device.write([value]);
    if doBuzzer and (value >= daymax):
        doBuzzer = False
        device.write([buzzerByte])
    elif (not doBuzzer) and (value < daymin):
        doBuzzer = True

def timeNow():
    """ Calculate the decimal time of the day
    """
    d = datetime.now()
    h = d.hour + d.minute / 60.0 + d.second / 3600.0
    return h

while True:
    try:
        sendTime(timeNow())
        sleep(15)
    except KeyboardInterrupt:
        print('\nKeyboardinterrupt found!')
        print('Program Stopped Manually!')
        break

device.close()
