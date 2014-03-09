#!/bin/bash

#---------------------------------------------------------------------------------------------------------+
#                                               startstream.sh                                            |
# (c) 2014 F. Anderson (finnian@fxapi.co.uk)                                                              |
#---------------------------------------------------------------------------------------------------------+

sudo killall motion
trap '{ echo "Stream stopped!" ; exit 1; }' INT
echo -e "\ncd-ing to the dir..."
cd /home/finnian/mjpg-streamer-code-182/mjpg-streamer
echo -e "\nMaking /tmp/stream..."
mkdir /tmp/stream
echo -e "\nStarting raspistill..."
raspistill --nopreview -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 &> /dev/null &

echo -e "\nStarting stream on http://fxapi:8080. Direct stream is on fxapi:8080/?action=stream\n"
LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -i "input_file.so -f /tmp/stream -n pic.jpg" -o "output_http.so -w /usr/local/www" &>/dev/null &
