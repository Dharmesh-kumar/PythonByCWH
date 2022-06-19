#Healthy Programmer
from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file, stopper):
     mixer.init()
     mixer.music.load(file)
     mixer.music.play()
     while True:
         a= input().lower()
         if a == stopper:
             mixer.music.stop()
             break

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3""stop")
    init_water = time()
    init_eyes = time()
    init_excercise= time()
    watersecs = 40 *60
    exsecs = 30*60
    eyessecs = 45* 60  #seconds

    while True:
        if time() - init_water > watersecs:
            print("Water drinking time. Enter 'drank' to stop the alarm.")
            musiconloop("water.mp3","drank")
            init_water = time()
            log_now("Drank water at")

        if time() - init_excercise > exsecs:
            print("Water Excercise time . Enter 'done' to stop the alarm.")
            musiconloop("water.mp3","drank")
            init_excercise = time()
            log_now("Excercise at")

        if time() - init_eyes > eyessecs:
            print("Eyes massage time . Enter 'done' to stop the alarm.")
            musiconloop("water.mp3", "done")
            init_eyes = time()
            log_now("eyes relaxed at")