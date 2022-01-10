import os
import time

print("starting updating from git")

while True:
    time.sleep(0.2)
    rez = os.popen("git pull").read()
    if not "Already up to date" in rez:
        print("making an update")
        os.system("python3 -m mkdocs build")
