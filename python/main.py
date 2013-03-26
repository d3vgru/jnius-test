from jnius import autoclass
from jnius import cast
from threading import Thread
from time import sleep

PythonActivity = autoclass('org.renpy.android.PythonActivity')

def loop():
    while 1:
        PythonActivity.log('tick')
        sleep(5)

if __name__ == '__main__':
    exit_exception = None
    if exit_exception:
        raise exit_exception
    PythonActivity.log('hello')
    thread = Thread(target=loop)
    thread.start()
    PythonActivity.log('thread started')
    