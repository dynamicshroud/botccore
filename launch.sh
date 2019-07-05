#!/bin/bash
# Node script

CONFIG=config.py

if [ -e $CONFIG ]; then
    echo "[*] Using config file"
    python3 node.py
else
    echo "[!] No config file, using default"
    echo "HOST = '127.0.0.1'; " >> $CONFIG
    echo "PORT = 51515" >> $CONFIG
    python3 node.py
fi