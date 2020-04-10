# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/4/10
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

import random, time

def getNumber():
    return random.randint(1, 10)

class Hare:
    def __init__(self, pos = 1):
        self.pos = pos
        self.race()

    def sleep(self):
        self.pos += 0

    def bigleap(self):
        self.pos +=9

    def severeSlip(self):
        self.pos -= 12
        self.pos = 1 if self.pos < 1 else self.pos

    def smallJump(self):
        self.pos += 1

    def slightSlip(self):
        self.pos -= 2
        self.pos = 1 if self.pos < 1 else self.pos

    def race(self):
        n = getNumber()

        if n == 1 or n ==2:
            self.sleep()
        elif n == 3 or n == 4:
            self.bigleap()
        elif n == 5:
            self.severeSlip()
        elif n == 6 or n == 7 or n == 8:
            self.smallJump()
        else:
            self.slightSlip()

class Tortoise:
    def __init__(self, pos = 1):
        self.pos = pos
        self.race()

    def fastCrawl(self):
        self.pos += 3

    def slip(self):
        self.pos -= 6
        self.pos = 1 if self.pos < 1 else self.pos

    def slowCrawl(self):
        self.pos += 1

    def race(self):
        n = getNumber()

        if n >= 1 and n <= 5:
            self.fastCrawl()
        elif n <= 7:
            self.slip()
        else:
            self.slowCrawl()

def main():
    SIZE = 70
    rabbit = Hare()
    turtle = Tortoise()
    position = [" "] * SIZE
    #print(position)
    while rabbit.pos < SIZE and turtle.pos <SIZE:
        rabbit.race()
        turtle.race()

        if rabbit.pos != turtle.pos:
            position[rabbit.pos] = "H"
            position[turtle.pos] = "T"
        else:
            position[rabbit.pos] = "OUCH!!"
        print(position)

        time.sleep(0.2)
        position = [" "] * SIZE

    print("Congratulations! ")
    if rabbit.pos > turtle.pos:
        print("Rabbit is the winner!")

    elif rabbit.pos < turtle.pos:
        print("Tortoise is the winner!")

    else:
        print("They both reached the endpoint at the same time!")

if __name__ == "__main__":
    main()
    #to be further improved later