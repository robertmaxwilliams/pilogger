#!/bin/bash

python record_gyro.py &
echo "recording video and accel data"
epochTime=$(date +%s)
raspivid -n -w 640 -h 480 --timeout 1800000 --segment 60000 --output "video%d.h264" &
PICAM=$!
