#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Félix Rodríguez Díaz
7/12/25

--- Day 4: Printing Department ---
You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).
Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.
"Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."
If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.
The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.
For example:
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.
In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?
"""

datos = open("dia04-input.txt", "r").read().splitlines()

nfilas = len(datos)
ncols = len(datos[0])

accessibles = 0

for f in range(nfilas):
    for c in range(ncols):
        if datos[f][c] != "@":
            continue
        adyacentes = 0
        # Derecha
        if c < ncols-1:
            if datos[f][c+1] == "@":
                adyacentes += 1
        # Izquierda
        if c > 0:
            if datos[f][c-1] == "@":
                adyacentes += 1
        # Arriba
        if f > 0:
            if datos[f-1][c] == "@":
                adyacentes += 1
        # Abajo
        if f < nfilas-1:
            if datos[f+1][c] == "@":
                adyacentes += 1
        # Arriba derecha
        if f > 0 and c < ncols-1:
            if datos[f-1][c+1] == "@":
                adyacentes += 1
        # Arriba izquierda
        if f > 0 and c > 0:
            if datos[f-1][c-1] == "@":
                adyacentes += 1
        # Abajo derecha
        if f < nfilas-1 and c < ncols-1:
            if datos[f+1][c+1] == "@":
                adyacentes += 1
        # Abajo izquierda
        if f < nfilas-1 and c > 0:
            if datos[f+1][c-1] == "@":
                adyacentes += 1
        if adyacentes < 4:
            accessibles += 1

print("Rollos accesibles:", accessibles)

# Solución: 1356

"""
--- Part Two ---
Now, the Elves just need help accessing as much of the paper as they can.
Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?
Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted @ to indicate that a roll of paper is about to be removed, and using x to indicate that a roll of paper was just removed:
Initial state:
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
Remove 13 rolls of paper:
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
Remove 12 rolls of paper:
.......x..
.@@.x.x.@x
x@@@@...@@
x.@@@@..x.
.@.@@@@.x.
.x@@@@@@.x
.x.@.@.@@@
..@@@.@@@@
.x@@@@@@@.
....@@@...
Remove 7 rolls of paper:
..........
.x@.....x.
.@@@@...xx
..@@@@....
.x.@@@@...
..@@@@@@..
...@.@.@@x
..@@@.@@@@
..x@@@@@@.
....@@@...
Remove 5 rolls of paper:
..........
..x.......
.x@@@.....
..@@@@....
...@@@@...
..x@@@@@..
...@.@.@@.
..x@@.@@@x
...@@@@@@.
....@@@...
Remove 2 rolls of paper:
..........
..........
..x@@.....
..@@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@x.
....@@@...
Remove 1 roll of paper:
..........
..........
...@@.....
..x@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
Remove 1 roll of paper:
..........
..........
...x@.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
Remove 1 roll of paper:
..........
..........
....x.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
Remove 1 roll of paper:
..........
..........
..........
...x@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
Stop once no more rolls of paper are accessible by a forklift. In this example, a total of 43 rolls of paper can be removed.
Start with your original diagram. How many rolls of paper in total can be removed by the Elves and their forklifts?
"""

accessibles = 0

while True:
    lista_accessibles = []
    for f in range(nfilas):
        for c in range(ncols):
            if datos[f][c] != "@":
                continue
            adyacentes = 0
            # Derecha
            if c < ncols-1:
                if datos[f][c+1] == "@":
                    adyacentes += 1
            # Izquierda
            if c > 0:
                if datos[f][c-1] == "@":
                    adyacentes += 1
            # Arriba
            if f > 0:
                if datos[f-1][c] == "@":
                    adyacentes += 1
            # Abajo
            if f < nfilas-1:
                if datos[f+1][c] == "@":
                    adyacentes += 1
            # Arriba derecha
            if f > 0 and c < ncols-1:
                if datos[f-1][c+1] == "@":
                    adyacentes += 1
            # Arriba izquierda
            if f > 0 and c > 0:
                if datos[f-1][c-1] == "@":
                    adyacentes += 1
            # Abajo derecha
            if f < nfilas-1 and c < ncols-1:
                if datos[f+1][c+1] == "@":
                    adyacentes += 1
            # Abajo izquierda
            if f < nfilas-1 and c > 0:
                if datos[f+1][c-1] == "@":
                    adyacentes += 1
            if adyacentes < 4:
                accessibles += 1
                lista_accessibles.append((f, c))
    if not lista_accessibles:
        break
    for (fila, col) in lista_accessibles:
        datos[fila] = datos[fila][:col] + "." + datos[fila][col+1:]

print("Rollos accesibles:", accessibles)

# Solución: 8713