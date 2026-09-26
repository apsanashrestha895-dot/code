import random
from datetime import datetime
import pygame
import zoneinfo

pygame.init()
screen = pygame.display.set_mode((800,600))
#correct_no = int(input("enter a number:"))
now = datetime.now()
now_date = datetime.now(zoneinfo("asia/kathmandu"))
print(now_date)

for i in range(1,101):
    random.randint = int(input("enter a number:"))
    print(random.randint)
    prrint(i)
    if i == random.randint:
        print("you won")
        break
    else:
            print("you loose")
