#!/usr/bin/env python3
# Calculation of leads/feeds and gear setups for "ОТ-4" lathe
# by Yuriy Skvortsov; yuriy.skvortsov@gmail.com; 2017

K0 = 1/3

Kletter = {'Б':1, 'А':2, 'Г': 4, 'В':8, 'П': None}
Knumber = {1:1, 2:5/4, 3:7/5, 4:3/2, 5:8/5, 6:7/4}
Kbox0 = 1/6

Kscrew = 6
Kfeed = 6/5

Gears = [38,43,45,48,50,54,55,60,70,72,75,79]

def Kbox(letter, number):
    return (Kletter[letter] * Knumber[number] * Kbox0) if Kletter[letter] else 1

def lead(G1,G2,G3,G4, letter, number, screw):
    Kg = G1 / G4 * ((G3 / G2) if (G2 and G3) else 1)
    Kb = Kbox(letter, number)
    Kf = Kscrew if screw else Kfeed
    return round(K0 * Kg * Kb * Kf, 7)

def equals_in_list(lst):
    for i1 in range(len(lst)-1):
        for i2 in range(i1+1, len(lst)):
            if lst[i1] == lst[i2]: return True
    return False

def gen_gears():
    for G1 in Gears:
        for G4 in Gears:
            if G1 == G4: continue
            yield [G1, None, None, G4]
            for G2 in Gears:
                for G3 in Gears:
                    if equals_in_list([G1,G2,G3,G4]): continue
                    yield G1,G2,G3,G4
            
def find_setup(l, tol=1e-3):
    setups = []
    for screw in (True, False):
        for G in gen_gears():
            for L in Kletter.keys():
                for N in Knumber.keys():
                    if L == 'П' and N != 1: continue
                    if L == 'П': N = None
                    if G[0] > 45: continue
                    l_ = lead(G[0],G[1],G[2],G[3], L, N, screw)
                    if abs(l-l_) <= tol*l:
                        setups.append({'gears':G, 'letter':L, 'number':N, 'screw':screw, 'lead':l_})
    return setups

if __name__ == '__main__':
    print('gears:45,75,None,60; А 1; feed; lead =', lead(45,75,None,60, 'А', 1, False))
    print('gears:45,75,None,60; А 1; screw; lead =', lead(45,75,None,60, 'А', 1, True))
    print('gears:45,75,None,60; П; screw; lead =', lead(45,75,None,60, 'П', None, True))
    print('\n\tsetups for 5.5 +- 0.1% lead/feed:')
    for s in find_setup(5.5):
        if s['screw'] == True:
            print(s)
