#! /usr/bin/python
# -*- coding: utf8 -*-

# Import stuff we need
import os
import random

# Open the file
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__, 'quotes.txt'), 'r')

# Read the entire file and append each line to the array
quotes = []
for line in file:
    quotes.append(line.strip())
file.close()

# Generate random quote based on the amount of quotes we found
num = random.randint(0, len(quotes)-1)

# Change the motd-file
with open('/etc/motd', 'w+') as file:
    file.write('\n' + quotes[num] + '\n\n')
