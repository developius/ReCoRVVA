source
======

Source code for the ReCoRVVA robot. Also acts as a server.

Note: requires Python module 'termcolor' and python library "cwiid".
Download termcolour here: https://pypi.python.org/packages/source/t/termcolor/termcolor-1.1.0.tar.gz
Then run:
tar zxvf termcolor-1.1.0.tar.gz && cd termcolor-1.1.0/ && sudo ./setup.py build && sudo ./setup.py install

To install "cwiid" run "sudo apt-get install cwiid".

main.py -> handles all the scripts
comms.py -> handles communication through a Python socket
ping.py -> gets the ping and uses a module in comms.py to send it to who needs it
motors.py -> controls the motors
wiimote.py -> gets data from Wii remote and sends it to the Python socket
xbox.py -> gets the data from an Xbox controller and sends it to the Python socket
startstream.sh -> starts the camera stream
