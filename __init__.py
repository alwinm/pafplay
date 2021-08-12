import os

import random
import time
import sys


filenames = os.listdir('.')

for filename in filenames:
    if os.path.isdir(filename):
        filenames += [filename + '/' + thing for thing in os.listdir(filename)]






while True:
    random.shuffle(filenames)
    for filename in filenames:
        if os.path.isdir(filename):
            continue
        time.sleep(1)
        
        command = 'afplay {}'.format(filename.replace(' ',"\ ").replace('(','\('))
        print(command)
        result = os.system(command)
        if result == 2:
            print('Ctrl-C was called',result)
            sys.exit(0)

