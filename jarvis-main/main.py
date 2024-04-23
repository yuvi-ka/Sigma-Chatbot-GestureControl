import os
import eel

from engine.features import *
from engine.command import *

def start():
    playAssistantSound()



    eel.init(f'{os.path.dirname(os.path.realpath(__file__))}/www')

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)
 