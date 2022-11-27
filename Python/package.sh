#!/bin/bash

# Pacchetti da installare

sudo apt-get install pip
pip3 install pygame
pip3 install pygame --version
pip3 install pandas
pip3 install ffpyplayer
pip3 install pymediainfo

# Se è un sistema linux
sudo apt-get update -y
sudo apt-get install -y libmediainfo-dev