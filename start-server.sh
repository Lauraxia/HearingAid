#!/bin/bash
pactl load-module module-simple-protocol-tcp rate=48000 format=s16le channels=2 source=alsa_output.pci-0000_00_1b.0.analog-stereo.monitor record=true port=8001 listen=100.64.84.67
