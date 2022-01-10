import os
import time

while True:
    time.sleep(60)
    os.system("git pull")
    rez = os.system("git status -uno")
    if rez is not 0:
        os.system("python3 -m mkdocs build")
