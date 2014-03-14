#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#                                               wiimote.py                                                |
# Gets the data from a Wii mote and sends it via a Python socket to the ReCoRVVA
# (c) 2014 B. James (ben@fxapi.co.uk)                                                                     |
# Thanks to F. Anderson (finnian@fxapi.co.uk) for the use of his API                                      |
#---------------------------------------------------------------------------------------------------------+

# but where did you get cwiid from?!

import cwiid
import time

button_delay = 0.25

print "Press 1 + 2 on your Wii Remote now ..."
time.sleep(1)

#try to connect to Wiimote
try:
  wm = cwiid.Wiimote()
except RuntimeError:
  print "Couldn't find wii remote"
  quit()

#turn on led to show connected
wm.led = 1

#rumble for 1 second to show connected
wm.rumble = 1
time.sleep(1)
wm.rumble = 0




print 'Wii Remote connected...\n'
print 'Press some buttons!\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

#turn on reporting mode
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

tilt_status = 'right'#accelerometer reading is (0,0,0) first time through the while true.

while True:

  buttons = wm.state['buttons']
  accelerometer = wm.state['acc']

  #check whether the Wiimote is tilted to the right or left
  #accelerometer reading increases as Wiimote tilts left and decreases as it's tilting right. Neutral is 125.
  #print acceleromter
  if(accelerometer[1] > 130):
   if(tilt_status != 'left'):
     print 'turning left'
     tilt_status = 'left'

  elif(accelerometer[1] < 110):
    if(tilt_status != 'right'):
      print 'turning right'
      tilt_status = 'right'

  elif(accelerometer[1] <= 130 & accelerometer[1] >= 110):
    if(tilt_status != 'neutral'):
      print 'steering straight'
      tilt_status = 'neutral'

  # If Plus and Minus buttons pressed
  # together then rumble and quit.
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\nClosing connection ...'
    wm.rumble = 1
    time.sleep(1)
    wm.rumble = 0
    exit(wm)

  if (buttons & cwiid.BTN_LEFT):
    print 'Left pressed'
    time.sleep(button_delay)

  if(buttons & cwiid.BTN_RIGHT):
    print 'Right pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_UP):
    print 'Up pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_DOWN):
    print 'Down pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    time.sleep(button_delay)
    
  if (buttons & cwiid.BTN_A):
    print 'Button A pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_B):
    print 'Button B pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_HOME):
    print 'Home Button pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_MINUS):
    print 'Minus Button pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_PLUS):
    print 'Plus Button pressed'
    time.sleep(button_delay)
