# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/4/10
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

import random, time


def getNumber():
    return random.randint(1, 10)


class Hare:
    def __init__(self, pos=1):
        self.pos = pos

    def sleep(self):
        pass

    def bigleap(self):
        self.pos += 9

    def severeSlip(self):
        self.pos -= 12
        if self.pos < 1:
            self.pos = 1

    def smallJump(self):
        self.pos += 1

    def slightSlip(self):
        self.pos -= 2
        if self.pos < 1:
            self.pos = 1

    def race(self):
        n = getNumber()

        if n == 1 or n == 2:
            self.sleep()
        elif n == 3 or n == 4:
            self.bigleap()
        elif n == 5:
            self.severeSlip()
        elif n <= 8:
            self.smallJump()
        else:
            self.slightSlip()


class Tortoise:
    def __init__(self, pos=1):
        self.pos = pos

    def fastCrawl(self):
        self.pos += 3

    def slip(self):
        self.pos -= 6
        if self.pos < 1:
            self.pos = 1

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

    while rabbit.pos < SIZE and turtle.pos < SIZE:
        rabbit.race()
        turtle.race()
        pos = max(SIZE, rabbit.pos, turtle.pos) + 1
        position = [" "] * pos

        if rabbit.pos != turtle.pos:
            position[rabbit.pos] = "H"
            position[turtle.pos] = "T"
        else:
            position[rabbit.pos] = "OUCH!!"

        for c in position:
            print(c, end="")
        print()

        time.sleep(0.2)

    print("Congratulations! ")
    if rabbit.pos > turtle.pos:
        print("Rabbit is the winner!")

    elif rabbit.pos < turtle.pos:
        print("Tortoise is the winner!")

    else:
        print("They both reached the endpoint at the same time!")


if __name__ == "__main__":
    main()
# This program is a translation of its c++ version which you may find in another folder.
