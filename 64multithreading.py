# (09:05:03)

# multithreading : used to perform multiple tasks concurrently

import threading
import time

def walk_dog(first,last):
    time.sleep(6)
    print(f"You finished walking with {first}{last}")

def take_out_trash():
    time.sleep(4)
    print("You take out the trash")

def get_mail():
    time.sleep(2)
    print("You get the mail")

Chore1 = threading.Thread(target= walk_dog , args = ("Tommy","1"))
Chore1.start()
Chore2 = threading.Thread(target= take_out_trash)
Chore2.start()
Chore3 = threading.Thread(target= get_mail)
Chore3.start()

Chore1.join()# if join not used print executes
Chore2.join()
Chore3.join()

print("All chores are complete")