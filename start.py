import os
import time

time.sleep(0.5)
os.system("mkdir /media/root/disque_dure/ && sudo mount /dev/sda1 /media/root/disque_dure/")
os.system("mkdir /media/root/disque_dure1/ && sudo mount /dev/sda2 /media/root/disque_dure1/")

os.system("flask run --host 0.0.0.0 --port 5000")