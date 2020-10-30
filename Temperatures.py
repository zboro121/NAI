import sys
import math

# https://www.codingame.com/ide/puzzle/temperatures
# Pawel Zborowski
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temp = 5528
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    T = int(i)

    if abs(T)<abs(temp):
        temp = T

    elif abs(T)==abs(temp) and T>temp:
        temp = T
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
if n==0:
    print(0)
else:
    print(temp)