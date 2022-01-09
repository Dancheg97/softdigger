import os
import time

while True:
    time.sleep(1)
    os.system('git pull')
    os.system('python3 -m mkdocs build')
