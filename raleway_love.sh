#!/bin/sh

#
# Start Raleway_love!
#

sleep  4 && conky -b -c ~/.config/conky/raleway_love/conky/raleway_love__cpu.conf &
sleep  6 && conky -b -c ~/.config/conky/raleway_love/conky/raleway_love__net.conf &
sleep  8 && conky -b -c ~/.config/conky/raleway_love/conky/raleway_love__disk.conf &
sleep 10 && conky -b -c ~/.config/conky/raleway_love/conky/raleway_love__text.conf &
sleep 12 && conky -b -c ~/.config/conky/raleway_love/conky/raleway_love__date.conf &
sleep 14 && conky -b -c ~/.config/conky/raleway_love/conky/raleway_love__rate.conf & disown
