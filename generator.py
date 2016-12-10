#!/usr/bin/env python3

from random import shuffle

teams = []

with open('teams.txt', 'r') as f, open('rankings.txt', 'w') as r:
     teams = [i.strip() for i in f.readlines()]
     shuffle(teams)
     shuffle(teams)
     shuffle(teams)
     shuffle(teams)
     for team in teams:
         r.write("{}\n".format(team))
