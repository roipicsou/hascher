import os
import time

time.sleep(2)
os.system("mkdir /media/root/disque_dure/")
os.system("sudo mount /dev/sda1 /media/root/disque_dure/")
os.system("mkdir /media/root/disque_dure1/")
os.system("sudo mount /dev/sda2 /media/root/disque_dure1/")

os.system("flask run --host 0.0.0.0 --port 5000")