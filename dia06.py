#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Félix Rodríguez Díaz
9/12/25

--- Day 6: Trash Compactor ---
After helping the Elves in the kitchen, you were taking a break and helping them re-enact a movie scene when you over-enthusiastically jumped into the garbage chute!
A brief fall later, you find yourself in a garbage smasher. Unfortunately, the door's been magnetically sealed.
As you try to find a way out, you are approached by a family of cephalopods! They're pretty sure they can get the door open, but it will take some time. While you wait, they're curious if you can help the youngest cephalopod with her math homework.
Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists of a list of problems; each problem has a group of numbers that need to be either added (+) or multiplied (*) together.
However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list. For example:
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces. The left/right alignment of numbers within each problem can be ignored.
So, this worksheet contains four problems:
    123 * 45 * 6 = 33210
    328 + 64 + 98 = 490
    51 * 387 * 215 = 4243455
    64 + 23 + 314 = 401
To check their work, cephalopod students are given the grand total of adding together all of the answers to the individual problems. In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.
Of course, the actual worksheet is much wider. You'll need to make sure to unroll it completely so that you can read the problems clearly.
Solve the problems on the math worksheet. What is the grand total found by adding together all of the answers to the individual problems?
"""

datos = open("dia06-input.txt", "r").read().splitlines()

datos_limpios = []

for d in datos:
    datos_limpios.append([e for e in d.split(" ") if e!=""])

resultado = 0

filas = len(datos_limpios)

for c in range(len(datos_limpios[0])):
    if datos_limpios[-1][c] == "+":
        r = 0
        for f in range(filas-1):
            r += int(datos_limpios[f][c])
    else:
        r = 1
        for f in range(filas-1):
            r *= int(datos_limpios[f][c])
    resultado += r

print(resultado)

# Resultado 6605396225322

"""
--- Part Two ---
The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.
Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)
Here's the example worksheet again:
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
Reading the problems right-to-left one column at a time, the problems are now quite different:
    The rightmost problem is 4 + 431 + 623 = 1058
    The second problem from the right is 175 * 581 * 32 = 3253600
    The third problem from the right is 8 + 248 + 369 = 625
    Finally, the leftmost problem is 356 * 24 * 1 = 8544
Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.
Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?
"""

datos2 = []

for d in datos:
    datos2.append(list(d))

for c in range(len(datos2[0])):
    espacios_vacios = True
    for f in range(filas-1):
        if datos2[f][c] == " ":
            espacios_vacios *= True
        else:
            espacios_vacios = False
    if espacios_vacios:
        for ff in range(filas-1):
            datos2[ff][c] = "v"

datos_limpios2 = []

for d in datos2[:-1]:
    datos_limpios2.append("".join(d).split("v"))

resultado2 = 0

for c in range(len(datos_limpios2[0])):
    if datos_limpios[-1][c] == "+":
        r2 = 0
        for z in range(len(datos_limpios2[0][c])):
            parcial = ""
            for f in range(filas-1):
                parcial += datos_limpios2[f][c][z]
            r2 += int(parcial)
    else:
        r2 = 1
        for z in range(len(datos_limpios2[0][c])):
            parcial = ""
            for f in range(filas-1):
                parcial += datos_limpios2[f][c][z]
            r2 *= int(parcial)
    resultado2 += r2

print(resultado2)

# Resultado 11052310600986