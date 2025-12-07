#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Félix Rodríguez Díaz
7/12/25
--- Day 5: Cafeteria ---
As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.
You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" Resolute in your quest, you investigate.
"If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. You ask what's going on.
The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are fresh and which are spoiled. When you ask how it works, they give you a copy of their database (your puzzle input).
The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. For example:
3-5
10-14
16-20
12-18
1
5
8
11
17
32
The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.
The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:
    Ingredient ID 1 is spoiled because it does not fall into any range.
    Ingredient ID 5 is fresh because it falls into range 3-5.
    Ingredient ID 8 is spoiled.
    Ingredient ID 11 is fresh because it falls into range 10-14.
    Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
    Ingredient ID 32 is spoiled.
So, in this example, 3 of the available ingredient IDs are fresh.
Process the database file from the new inventory management system. How many of the available ingredient IDs are fresh?
"""

datos = open("dia05-input.txt").read().split("\n\n")

rangos = datos[0].splitlines()
ids = datos[1].splitlines()

frescos = 0

for id in ids:
    id = int(id)
    for rango in rangos:
        inicio, fin = map(int, rango.split("-"))
        if inicio <= id <= fin:
            frescos += 1
            break

print(frescos)

"""
--- Part Two ---
The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.
So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.
Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:
3-5
10-14
16-20
12-18
The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.
Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?
"""

rangos2 = []

for r in range(len(rangos)):
    inicio, fin = map(int, rangos[r].split("-"))
    rangos2.append([inicio, fin])

modificados = -1

while modificados != 0:
    nuevos_rangos = []
    modificados = 0

    for r in rangos2:
        inicio, fin = r
        if not nuevos_rangos:
            nuevos_rangos.append([inicio, fin])
            continue
        modificado = False
        for nr in nuevos_rangos:
            if inicio >= nr[0] and fin <= nr[1]:
                modificado = True
            elif inicio <= nr[0] and fin >= nr[1]:
                nr[0] = inicio
                nr[1] = fin
                modificado = True
            elif inicio < nr[0] and fin <= nr[1] and fin >= nr[0]:
                nr[0] = inicio
                modificado = True
            elif inicio >= nr[0] and fin > nr[1] and inicio <= nr[1]:
                nr[1] = fin
                modificado = True
        if not modificado:
            nuevos_rangos.append([inicio, fin])
        else:
            modificados += 1
    rangos2 = nuevos_rangos.copy()
    print(modificados)

#print(nuevos_rangos)
total_frescos = 0
for nr in nuevos_rangos:
    total_frescos += nr[1] - nr[0] + 1 

print(total_frescos)

# Respuesta incorrecta. ¿Se solaparan los rangos?
    
    




