#!/bin/sh

pkill -9 raspivid
pkill -9 python
gpio -g write 15 0
