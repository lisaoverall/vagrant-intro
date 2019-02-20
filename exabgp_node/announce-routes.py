#!/usr/bin/env python3
 
from __future__ import print_function
 
from sys import stdout
from time import sleep
 
messages = [
    'TODO',
    'TODOTWO',
]
 
sleep(5)
 
#Iterate through messages
while True:
    for message in messages:
        stdout.write(message + '\n')
        stdout.flush()
        sleep(1)
