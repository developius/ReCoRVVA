ReCoRVVA Server
======

Source code for the ReCoRVVA robot. Also acts as a server.

Note: requires Python module 'termcolor'.
Download termcolour here: https://pypi.python.org/packages/source/t/termcolor/termcolor-1.1.0.tar.gz
Then run:
tar zxvf termcolor-1.1.0.tar.gz && cd termcolor-1.1.0/ && sudo ./setup.py build && sudo ./setup.py install

main.py -> handles all the scripts
comms.py -> handles communication through a Python socket
sensors.py -> gets the ping/temperature/humidity and uses a module in comms.py to send it to whoever wants it
motors.py -> controls the motors
startstream.sh -> starts the camera stream
