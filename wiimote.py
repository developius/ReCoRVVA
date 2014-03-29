#!/usr/bin/python
#---------------------------------------------------------------------------------------------------------+
#                                               wiimote.py                                                |
# Gets the data from a Wiimote and sends it via a Python socket to the ReCCoRVVA			          |
# (c) 2014 B. James (ben@fxapi.co.uk)                                                                     |
# Thanks to F. Anderson (finnian@fxapi.co.uk) for the use of his API                                      |
#---------------------------------------------------------------------------------------------------------+

#Thanks to the developers of the CWiid bluetooth library at http://abstrakraft.org/cwiid

import cwiid, time, recorvva # cwiid needs to be in the 'requirments' - xavbabe   Done - benji
#I know I could have done "from recorvva import *" but this way I do "recorvva." before everything, so I know where all
#the functions come from.

recorvva.connect() #connect to python socket 

button_delay = 0.25

print "Press 1 + 2 on your Wii Remote now ..."
time.sleep(1)

#try to connect to Wiimote
try:
  wm = cwiid.Wiimote()
except RuntimeError:
  print "Couldn't find wii remote"
  recorvva.close()
  quit() #Do you actually ever get a error? Say start it with Wiimote not near- xavbabe   Yes, a message 
  #from the quit() function and the "couldn't find wii remote" message.
    
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
       recorvva.send_msg("turn left")
       tilt_status = 'left'

  elif(accelerometer[1] < 110):
    if(tilt_status != 'right'):
      print 'turning right'
      recorvva.send_msg("turn right")
      tilt_status = 'right'

  elif(accelerometer[1] <= 130 & accelerometer[1] >= 110):
    if(tilt_status != 'neutral'):
      print 'steering straight'
      recorvva.send_msg("steer straight")
      tilt_status = 'neutral'

  # If Plus and Minus buttons pressed
  # together then rumble and quit.
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\nClosing connection ...'
    wm.rumble = 1
    time.sleep(1)
    wm.rumble = 0
    exit(wm)
    recorvva.send_msg("The PLUS and MINUS buttons on the wiimote have been pressed, about to close connection")
    recorvva.close()

  if (buttons & cwiid.BTN_LEFT):
    print 'down pressed'
    recorvva.send_msg("camera down")
    time.sleep(button_delay)

  if(buttons & cwiid.BTN_RIGHT):
    print 'up pressed'
    recorvva.send_msg("camera up ")
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_UP):
    print 'left pressed'
    recorvva.send_msg("camera left")
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_DOWN):
    print 'right pressed'
    recorvva.send_msg("camera right")
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    recorvva.send _msg("Go backwards")
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    recorvva.send _msg("go forwards")
    time.sleep(button_delay)
    
  if (buttons & cwiid.BTN_A):
    print 'Button A pressed'
    recorvva.send _msg("headlights")
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_B):
    print 'Button B pressed'
    recorvva.send _msg("stop")
    time.sleep(button_delay)
