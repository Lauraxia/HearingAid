import pyqrcode
import socket
import subprocess
import shlex
import webbrowser
import os

os.chdir(os.path.dirname(__file__))
print(os.getcwd())

ip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
print(ip)
qr = pyqrcode.create(ip)
qr.png(os.getcwd() + '//qr.png', scale=12)
from subprocess import call
startcall = "pactl load-module module-simple-protocol-tcp rate=48000 format=s16le channels=2 source=alsa_output.pci-0000_00_1b.0.analog-stereo.monitor record=true port=8001 listen=" + ip;
call(shlex.split(startcall))

webbrowser.open('file://' + os.getcwd() + "//deployqr.html") #os.path.realpath("deployqr.html"))
