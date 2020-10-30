import sys
import math

# https://www.codingame.com/ide/puzzle/power-of-thor-episode-1
# Paweł Zborowski
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
AxisX = light_x - initial_tx
AxisY = light_y - initial_ty
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    kierunek = ""

    if AxisY < 0:
        kierunek += "N"
        AxisY += 1

    elif AxisY > 0:
        kierunek += "S"
        AxisY -= 1

    if AxisX < 0:
        kierunek += "W"
        AxisX += 1

    elif AxisX > 0:
        kierunek += "E"
        AxisX -= 1

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(kierunek)
