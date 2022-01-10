import os
import time

while True:
    time.sleep(0.2)
    os.system("git pull &> /dev/null")
    rez = os.system("git status -uno &> /dev/null")
    if rez is not 0:
        print("making an update")
        os.system("python3 -m mkdocs build")
