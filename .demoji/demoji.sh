#!/bin/bash
wget "$1" -O "$2.png"
python3 demoji.py $2
rm "$2.png"
