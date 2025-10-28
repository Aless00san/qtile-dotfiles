#!/bin/bash

# Disable built-in touchpad (optional)
xinput disable 9

# Gracefully close all open widgets
eww close-all
sleep 0.3

# Kill any leftover eww daemons
pkill -9 eww
sleep 0.3

# Clean cache/state (optional but helps prevent ghost windows)
rm -rf ~/.cache/eww ~/.local/share/eww

# Start a fresh eww daemon
eww daemon
sleep 0.5  # give it a moment to initialize

# Open desired widgets
eww open top_clock
eww open hotzone

# Start system tray applets
nm-applet &
blueman-applet &

# Apply GTK theme
export GTK_THEME=Arc-Dark
