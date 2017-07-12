#!/bin/bash

python record_gyro.py &
echo "recording video and accel data"
epochTime=$(date +%s)
raspivid -n -w 640 -h 480 --timeout 1800000 --segment 5000 --output "video $epochTime.h264" &
PICAM=$!
