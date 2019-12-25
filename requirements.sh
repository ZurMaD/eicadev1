#!/bin/sh
sudo apt update
sudo apt-get install python3-pip
sudo apt-get install python3-dev
sudo apt-get install libsdl2-dev libsdl2-ttf-dev libsdl2-image-dev libsdl2-mixer-dev

sudo python3 -m pip install -U pip

sudo pip3 install mysql-connector
sudo pip3 install kivy==1.11.1
sudo pip3 install kivymd==0.102.1
sudo pip3 install cython==0.20
sudo pip3 install pandas
sudo pip3 install numpy
sudo pip3 install bcrypt
sudo pip3 install matplotlib

sudo apt update
sudo apt install xclip
