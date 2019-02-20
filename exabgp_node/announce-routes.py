#!/usr/bin/env python3
 
from __future__ import print_function
 
from sys import stdout
from time import sleep
 
messages = [
    'announce route 100.10.0.0/24 next-hop self',
    'announce route 200.20.0.0/24 next-hop self',
]
 
sleep(5)
 
#Iterate through messages
while True:
    for message in messages:
        stdout.write(message + '\n')
        stdout.flush()
        sleep(1)
