import requests as rq
from time import sleep

while True:
    print(rq.get("https://webpin.onrender.com/").status_code)
    sleep(2)