#!/bin/bash

python record_gyro.py &
echo "recording video and accel data"
raspivid --width 640 --height 360 --framerate 24 --bitrate 750000 --qp 20 --timeout $((30*60*1000)) --segment $((60*1000)) --output video%(%s)T\n.h264
echo "thirty mins is up, stop record"

