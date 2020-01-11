

def str_finder(lst):
    result = []
    no_string = []
    for i in lst:
        if type(i) == str:
            result.append(str(i))
        else:
            no_string.append(i)
    if len(lst) == len(no_string):  # checks if list is now empty or not
        print(None)
    else:
        print(result)


def fah_to_cel_converter(degrees):
    celsius = (5/9)*(degrees-32)
    print(round(celsius, 2))


import csv, codecs
from urllib.request import urlopen


def sum_revenue():
    total = 0
    rev = []
    nrev = []
    url = 'https://drive.google.com/uc?export=download&id=1hiPTLgU69boF72-uY8qSytIfrDXVqU_V'
    response = urlopen(url)
    cr = csv.reader(codecs.iterdecode(response, 'utf-8'))
    for row in cr:
        '''print(row)'''
        rev.append(row[1])  # adds the average daily revenue of each shop to the rev list
    rev.pop(0)  # removes the column header
    for n in rev:
        nrev.append(int(n))
    print(nrev)
    for i in nrev:
        total = total + i
    print(total)
    comp_add = sum(nrev)
    if comp_add == total:  # checks if sum matches the value obtained using the built-in function.
        print((comp_add, True))
    else:
        print((comp_add, False))


def prime_num_finder(num):
    prime = []
    kprime = []
    if -1 <= num <= 1:  # integers -1, 0, and 1 are not prime numbers
        print(None)
    else:
        if abs(num) > 1:
            for i in range(2, abs(num)+1):
                if (i % 2 != 0 or i == 2)and(i % 3 != 0 or i == 3)and(i % 5 != 0 or i == 5)and(i % 7 != 0 or i == 7):
                    prime.append(int(i))  # for the above line it means 2,3,5,7 are prime but their multiples are not
            for p in prime:
                if p*p in prime:
                    prime.remove(p*p)
            if num < -1:  # checking for negative integers as well and their negative primes
                for n in prime:
                    kprime.append(-n)
                print(kprime)
            else:
                print(prime)


from random import randint
import matplotlib.pyplot as plt
import numpy as np


def game(players):
    while players > 4 or players < 2:
        print("Minimum number of players must be 2 And Maximum must be 4")
        return

    scores = [0, 0, 0, 0]
    i = 1
    turns = 0
    turn_score = [[0, 0, 0, 0]]
    max_score = max(scores)

    while max_score < 23:
        while i <= players:  # ensures every player has a roll in a turn
            dice = randint(1, 6)
            scores[i-1] += dice
            if scores[i-1] > 23:
                scores[i-1] = 0
            i += 1

        i = 1
        turns += 1  # ensures the turns continues
        turn_score.append(scores[:])  # passes scores of each turn by value not by reference
        max_score = max(scores)

    print(turn_score)
    print(scores)
    if scores.count(23) == 1:
        print(f"Player {scores.index(max_score) + 1} Wins by {max_score} points after {turns} turns")
    else:
        for i in range(players):
            if scores[i] == 23:  # checks if multiple players had max scores
                print(f"Player {i + 1} Wins by {max_score} points after {turns} turns")

    turns += 1

    x = np.arange(0, turns)

    p1 = []
    p2 = []
    p3 = []
    p4 = []

    n = 0
    while n < turns:  # places respective scores in respective player list
        p1.insert(n, turn_score[n][0])
        p2.insert(n, turn_score[n][1])
        p3.insert(n, turn_score[n][2])
        p4.insert(n, turn_score[n][3])
        n += 1

    plt.plot(x, p1, label="Player 1")
    plt.plot(x, p2, label="Player 2")
    plt.plot(x, p3, label="Player 3")
    plt.plot(x, p4, label="Player 4")

    plt.xlabel("Turns")
    plt.ylabel("Points")

    plt.title("Dice Game")
    plt.legend()
    plt.show()


from random import uniform
from math import *
import matplotlib.pyplot as plt


def my_particle(n):
    while n <= 1 or n >= 10000:
        print("Minimum moves must be 2 and maximum must be 9999")
        return
    moves = [[0, 0]]
    for i in range(n):
        x = uniform(0, 20)
        y = uniform(0, 20)
        moves.append([x, y])
    print(moves)
    dist = sqrt(((moves[0][0]-moves[-1][0])**2 + (moves[0][1]-moves[-1][1])**2))
    print("The distance between start and end point is ", dist)

    x = []
    y = []

    i = 0
    while i <= n:
        x.append(moves[i][0])
        y.append(moves[i][1])
        i += 1

    plt.plot(x[0], y[0], marker="o")
    plt.text(x[0], y[0], "Starting Point")
    plt.plot(x, y, marker="o")
    plt.plot(x[-1], y[-1], marker="o")
    plt.text(x[-1], y[-1], "Ending Point")

    plt.show()

# first I imported all the modules I would need(random.uniform, math, matplotlib)
# since the user has a limit of moves I created a short while loop to check the range
# I made the starting point always (0,0) and the environment of movement 20units by 20 units
# Create a 2d list which will contain all the [x,y] list/points of every move
# for every move create a loop to randomise the x and y coordinate within the barrier set
# add every move to the moves list and calculate distance using math module and first and last points
# now for the graph put all x coordinates in a list as well as all y
# use a while loop and increment to append all moves
# this is useful so that when you plot method of plt you have all y values against x values
# set your preferred marker and text then show output
