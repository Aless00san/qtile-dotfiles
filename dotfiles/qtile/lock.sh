#!/bin/bash

CLEAR='#ffffff22'
WHITE='ffffffff'

i3lock --image=/home/alesan/Descargas/a_lockscreen.png \
	   --insidever-color=$CLEAR     \
	   --inside-color=$CLEAR        \
	   --blur 8 \
       --color=00000099 \
       --clock \
       --time-str="%H:%M" \
       --time-pos="250:h/2-60" \
       --time-size=150 \
       --time-color=$WHITE \
       --time-font="0xProto Nerd Font" \
       --date-str="%A, %B %d" \
       --date-pos="250:h/2+40" \
       --verif-pos="w/2:h-65" \
       --verif-color=$WHITE \
       --date-size=35 \
       --date-color=$WHITE \
       --date-font="0xProto Nerd Font" \
       --verif-font="0xProto Nerd Font" \
       --wrong-color=$WHITE \
       --wrong-pos="w/2:h-65" \
       --wrong-font="0xProto Nerd Font" \
       --wrong-text="Access Denied" \
       --verif-text="" \
       --noinput-text="" \
       --time-align=1 \
       --date-align=1 \
       --pass-media-keys
