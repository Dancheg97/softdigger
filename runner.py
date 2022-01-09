import os
import time

while True:
    time.sleep(60)
    os.system('git pull')
    os.system('python3 -m mkdocs build')
